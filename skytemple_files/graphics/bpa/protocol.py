#  Copyright 2020-2022 Capypara and the SkyTemple Contributors
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
from abc import abstractmethod
from typing import Protocol, Optional, Tuple, TypeVar, Iterable, Union, Iterator, List, Sequence, runtime_checkable

from PIL import Image


@runtime_checkable
class BpaFrameInfoProtocol(Protocol):
    duration_per_frame: int
    unk2: int

    @abstractmethod
    def __init__(self, duration_per_frame: int, unk2: int): ...


T = TypeVar('T', bound=BpaFrameInfoProtocol)


@runtime_checkable
class BpaProtocol(Protocol[T]):
    number_of_tiles: int
    number_of_frames: int
    tiles: List[bytearray]
    frame_info: List[T]

    @abstractmethod
    def __init__(self, data: bytes): ...

    @abstractmethod
    def get_tile(self, tile_idx: int, frame_idx: int) -> bytes:
        """Returns the tile data of tile no. tile_idx for frame frame_idx."""
        ...

    @abstractmethod
    def tiles_to_pil_separate(self, palette: List[int], width_in_tiles: int = 20) -> List[Image.Image]:
        """
        Exports the BPA as an image, where each row of 8x8 tiles is the
        animation set for a single tile. The 16 color palette passed is used to color the image.
        """
        ...

    @abstractmethod
    def pil_to_tiles(self, image: Image.Image) -> None:
        """
        Converts a PIL image back to the BPA.
        The format is expected to be the same as tiles_to_pil. This means, that
        each rows of tiles is one image set and each column is one frame.
        """
        ...

    @abstractmethod
    def pil_to_tiles_separate(self, images: List[Image.Image]) -> None:
        ...

    @abstractmethod
    def tiles_for_frame(self, frame: int) -> Sequence[bytearray]:
        """Returns the tiles for the specified frame. Strips the empty dummy tile image at the beginning."""
        ...
