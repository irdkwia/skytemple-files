#  Copyright 2020 Parakoopa
#
#  This file is part of SkyTemple.
#
#  SkyTemple is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  SkyTemple is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with SkyTemple.  If not, see <https://www.gnu.org/licenses/>.
import logging
from enum import Enum, auto
from typing import Optional

try:
    from PIL import Image
except ImportError:
    from pil import Image

from skytemple_files.common.util import *
from skytemple_files.common.ppmdu_config.data import Pmd2Data
from skytemple_files.container.sir0.sir0_serializable import Sir0Serializable
MAGIC_NUMBER = b'WTE\0'
logger = logging.getLogger(__name__)

class ColorDepth(Enum):
    COLOR_NONE = 0x00, 'Palette Only', 0, False
    COLOR_2BPP = 0x02, '2 bits per pixel (4 colors)', 2, True
    COLOR_4BPP = 0x03, '4 bits per pixel (16 colors)', 4, True
    COLOR_8BPP = 0x04, '8 bits per pixel (256 colors)', 8, True
    
    def __new__(cls, *args, **kwargs):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(
            self, _: int, explanation: str, bpp: int, has_image: bool
    ):
        self.explanation = explanation
        self.bpp = bpp
        self.has_image = has_image

class Wte(Sir0Serializable, AutoString):
    def __init__(self, data: Optional[bytes], header_pnt: int):
        """Construts a Wte model. Setting data to None will initialize an empty model."""
        if data is None:
            self.color_depth = ColorDepth.COLOR_NONE
            self.actual_dim = 0
            self.unk10 = 0
            self.width = 0
            self.height = 0
            self.image_data = bytes()
            self.palette = []
            return

        if not isinstance(data, memoryview):
            data = memoryview(data)

        assert self.matches(data, header_pnt), "The Wte file must begin with the WTE magic number"
        pointer_image = read_uintle(data, header_pnt + 0x4, 4)
        image_length = read_uintle(data, header_pnt + 0x8, 4)
        self.actual_dim = read_uintle(data, header_pnt + 0xC, 1)
        self.color_depth = ColorDepth(read_uintle(data, header_pnt + 0xD, 1))
        self.unk10 = read_uintle(data, header_pnt + 0x10, 4)
        self.width = read_uintle(data, header_pnt + 0x14, 2)
        self.height = read_uintle(data, header_pnt + 0x16, 2)
        pointer_pal = read_uintle(data, header_pnt + 0x18, 4)
        number_pal_colors = read_uintle(data, header_pnt + 0x1C, 4)
        assert read_uintle(data, header_pnt + 0x20, 4) == 0

        self.image_data = self._read_image(data, pointer_image, image_length)
        self.palette = self._read_palette(data, pointer_pal, number_pal_colors)

    @staticmethod
    def matches(data, header_pnt):
        return data[header_pnt:header_pnt+len(MAGIC_NUMBER)] == MAGIC_NUMBER

    @classmethod
    def sir0_unwrap(cls, content_data: bytes, data_pointer: int,
                    static_data: Optional[Pmd2Data] = None) -> 'Sir0Serializable':
        return cls(content_data, data_pointer)

    def sir0_serialize_parts(self) -> Tuple[bytes, List[int], Optional[int]]:
        from skytemple_files.graphics.wte.writer import WteWriter
        return WteWriter(self).write()

    def actual_dimensions(self) -> Tuple[int, int]:
        return (8*(2**(self.actual_dim & 0x07)), 8*(2**((self.actual_dim>>3) & 0x07)))

    def adjust_actual_dimensions(self, canvas_width: int, canvas_height: int):
        width = 0
        while 8*(2**width)<canvas_width:
            width+=1
        height = 0
        while 8*(2**height)<canvas_height:
            height+=1
        if width>=8 or height>=8: # Max theoretical size: (2**(7+3), 2**(7+3)) = (1024, 1024)
            raise ValueError('Canvas size too large.')
        self.actual_dim = width + (height<<3)
    
    def get_mode(self) -> int:
        return self.actual_dim+(self.color_depth.value<<8)
    
    def has_image(self) -> bool:
        return self.color_depth.has_image
    def has_palette(self) -> bool:
        return len(self.palette)>0
    
    def max_variation(self) -> int:
        if self.color_depth.has_image:
            return (len(self.palette)//3)//(2**self.color_depth.bpp)
        else:
            return 1
    
    def to_pil_palette(self) -> Image.Image:
        if self.color_depth.bpp==0:
            colors_per_line : int = 16
        else:
            colors_per_line : int = 2**self.color_depth.bpp
        palette : List[int] = self.palette
        if not self.has_palette():
            palette = [min((i//3)*(256//colors_per_line), 255) for i in range(colors_per_line*3)]
        else:
            if len(palette)%(colors_per_line*3)!=0:
                palette += [0] * ((colors_per_line*3) - (len(palette)%(colors_per_line*3)))
        img = Image.frombytes(mode="RGB", data=bytes(palette), size=(colors_per_line, len(palette)//colors_per_line//3))
        return img
    
    def to_pil_canvas(self, variation: int) -> Image.Image:
        return self.to_pil(variation).crop(box=[0,0,self.width,self.height])
        
    def to_pil(self, variation: int) -> Image.Image:
        dimensions = self.actual_dimensions()
        pil_img_data = bytearray(dimensions[0] * dimensions[1])
        if not self.has_image():
            assert len(self.image_data) == 0
            im = self.to_pil_palette()
            return im.resize((im.width*16, im.height*16), resample=Image.NEAREST)
        
        byte_handler = None
        if self.color_depth==ColorDepth.COLOR_2BPP:
            byte_handler = iter_bytes_2bit_le
        elif self.color_depth==ColorDepth.COLOR_4BPP:
            byte_handler = iter_bytes_4bit_le
        elif self.color_depth==ColorDepth.COLOR_8BPP:
            byte_handler = lambda x:x
        
        for i, px in enumerate(byte_handler(self.image_data)):
            pil_img_data[i] = px
        im = Image.frombuffer('P', dimensions, pil_img_data, 'raw', 'P', 0, 1)
        if not self.has_palette():
            nb_colors = 2**self.color_depth.bpp
            im.putpalette([min((i//3)*(256//nb_colors), 255) for i in range(nb_colors*3)])
        else:
            im.putpalette(self.palette[3*(2**self.color_depth.bpp)*variation:])
        return im

    def from_pil(self, img: Optional[Image.Image], pal: Optional[Image.Image], depth: ColorDepth, discard_palette: bool) -> 'Wte':
        if img!=None:
            try:
                self.adjust_actual_dimensions(img.width, img.height)
            except ValueError as ve:
                raise ValueError('This image is too big to fit into a WTE file.')
            
            self.width = img.width
            self.height = img.height
            dimensions = self.actual_dimensions()
            self.color_depth = depth
        else:
            self.color_depth = ColorDepth.COLOR_NONE
        
        if pal==None:
            if img!=None:
                if not self.has_image():
                    img = img.convert(mode="RGB").quantize(dither=Image.NONE)
                    self.palette = [x for x in memoryview(img.palette.palette)]
                else:
                    img = img.convert(mode="RGB").quantize(colors=2**depth.bpp, dither=Image.NONE)
                    self.palette = [x for x in memoryview(img.palette.palette)[:(2**depth.bpp)*3]]
            else:
                raise AttributeError('At least one of these elements must be specified: image or palette.')
        else:
            self.palette = list(pal.convert(mode="RGB").tobytes())
            if self.color_depth.has_image:
                dummy_pal : Image.Image = Image.new(mode='P', size=(1,1))
                palette : List[int] = self.palette[:(2**depth.bpp)*3]
                # Copy the first color data to the invalid palette entries
                # This is to prevent the quantizer to use those
                # invalid entries
                dummy_pal.putpalette(palette+((768-len(palette))//3)*self.palette[:3])
                img = img.convert(mode="RGB").quantize(dither=Image.NONE, palette=dummy_pal)
        if self.has_image():
            raw_pil_image = img.tobytes('raw', 'P')
            
            self.image_data = bytearray(dimensions[0] // 8 * self.height * depth.bpp)
            i = 0
            pixels_per_byte = 8 // depth.bpp
            for pix in raw_pil_image:
                b = (i % pixels_per_byte)*depth.bpp
                x = i // pixels_per_byte
                self.image_data[x] += pix<<b
                i+=1
                if i%dimensions[0]==self.width:
                    i += dimensions[0] - self.width
        else:
            self.image_data = bytearray(0)
        if discard_palette:
            self.palette = []
        return self

    def _read_image(self, data: memoryview, pointer_image, image_length) -> memoryview:
        return data[pointer_image:pointer_image+image_length]

    def _read_palette(self, data: memoryview, pointer_pal, number_pal_colors) -> List[int]:
        pal = []
        data = data[pointer_pal:pointer_pal+(number_pal_colors*4)]
        for i, (r, g, b, x) in enumerate(iter_bytes(data, 4)):
            pal.append(r)
            pal.append(g)
            pal.append(b)
            assert x == 0x80
        return pal

    def __eq__(self, other):
        if not isinstance(other, Wte):
            return False
        return self.identifier == other.identifier and \
            self.unk10 == other.unk10 and \
            self.width == other.width and \
            self.height == other.height and \
            self.image_data == other.image_data and \
            self.palette == other.palette
