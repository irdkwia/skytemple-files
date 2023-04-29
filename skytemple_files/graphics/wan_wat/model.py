#  Copyright 2020-2023 Capypara and the SkyTemple Contributors
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
from __future__ import annotations

from typing import List, Tuple

from PIL import Image, ImageOps
from skytemple_rust.pmd_wan import (  # pylint: disable=no-name-in-module,no-member,import-error
    FragmentBytes,
    FrameStore,
    WanImage,
    Frame,
    Animation
)


class MetaFramePositioningSpecs:
    def __init__(
        self, img: Image.Image, width: int, height: int, x_offset: int, y_offset: int
    ):
        self.img = img
        self.width = width
        self.height = height
        self.x_offset = x_offset
        self.y_offset = y_offset
        # This will be filled and contain the offset on the image specs generated by process.
        self.final_relative_x = None
        self.final_relative_y = None

    @classmethod
    def process(
        cls, items: List["MetaFramePositioningSpecs"]
    ) -> Tuple[int, int, int, int]:
        """
        Returns the full image dimensions and the image's center point and set's
        the final_relative_x/y attributes of all entries

        -> (width, height, center x, center y)
        """
        if len(items) < 1:
            return 0, 0, 0, 0
        smallest_x = 9999999
        smallest_y = 9999999
        biggest_x = -9999999
        biggest_y = -9999999

        for frame in items:
            smallest_x = min(smallest_x, frame.x_offset)
            smallest_y = min(smallest_y, frame.y_offset)
            biggest_x = max(biggest_x, frame.x_offset + frame.width)
            biggest_y = max(biggest_y, frame.y_offset + frame.height)

        for frame in items:
            frame.final_relative_x = frame.x_offset - smallest_x  # type: ignore
            frame.final_relative_y = frame.y_offset - smallest_y  # type: ignore

        return (
            (biggest_x - smallest_x),
            (biggest_y - smallest_y),
            abs(smallest_x),
            abs(smallest_y),
        )


class Wan:
    def __init__(self, data):
        self.model: WanImage = WanImage(data)  # type: ignore

    @property
    def frames(self) -> List[Frame]:
        return self.model.frame_store.frames

    @property
    def anim_groups(self) -> List[List[Animation]]:
        return self.model.animation_store.anim_groups

    def render_frame(
        self, frame: Frame
    ) -> Tuple[Image.Image, Tuple[int, int]]:
        """Returns the frame group as an image and it's center position as a tuple."""
        specs: List[MetaFramePositioningSpecs] = []
        for fragment in frame.fragments:
            fragment_bytes: FragmentBytes = self.model.fragment_bytes_store.fragment_bytes[
                fragment.fragment_bytes_index
            ]

            im = Image.frombuffer(
                "RGBA",
                (fragment.resolution.x, fragment.resolution.y),
                bytearray(
                    fragment_bytes.to_image(self.model.palette, fragment)
                ),
                "raw",
                "RGBA",
                0,
                1,
            )
            if fragment.flip.flip_h:
                im = ImageOps.mirror(im)
            if fragment.flip.flip_v:
                im = ImageOps.flip(im)

            specs.append(
                MetaFramePositioningSpecs(
                    im,
                    fragment.resolution.x,
                    fragment.resolution.y,
                    fragment.offset_x,
                    fragment.offset_y,
                )
            )

        w, h, cx, cy = MetaFramePositioningSpecs.process(specs)

        final_img = Image.new("RGBA", (w, h), (255, 0, 0, 0))
        for spec_frame in specs:
            final_img.paste(
                spec_frame.img,
                (
                    spec_frame.final_relative_x,
                    spec_frame.final_relative_y,
                    spec_frame.final_relative_x + spec_frame.width,  # type: ignore
                    spec_frame.final_relative_y + spec_frame.height,  # type: ignore
                ),
                spec_frame.img,
            )

        return final_img, (cx, cy)
