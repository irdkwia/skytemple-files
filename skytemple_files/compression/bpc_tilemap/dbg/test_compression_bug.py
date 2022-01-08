"""
Testing that something that was causing a bug can correctly be compressed by the algorithm now.
How this bug went unnoticed in 6+ months? I don't know!
"""
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
from skytemple_files.common.types.file_types import FileType

bug = bytearray(b'\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01 \x01 \x01 \x01 '
                b'\x010\x01@\x01 \x01@\x010\x01 \x01 \x01 \x01\x10\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01 \x01 '
                b'\x01 \x01@\x010\x01@\x010\x01@\x010\x01 \x01 \x010\x01@\x01 \x01@\x010\x01 '
                b'\x010\x010\x01@\x010\x01@\x010\x01@\x010\x01@\x010\x01 \x01\x10\x01\x00\x01 \x01\x00\x01\x10\x01 '
                b'\x01\x10\x01\x00\x01\x00\x01 \x01\x00\x01\x10\x01 \x01\x10\x01\x00\x01 \x01\x00\x01 \x01@\x010\x01 '
                b'\x010\x01@\x01 \x01@\x010\x010\x01 \x010\x01@\x01 \x01@\x010\x01 \x010\x01 \x01\x10\x01\x00\x01 '
                b'\x01\x00\x01\x10\x01 \x01 \x01 \x010\x01@\x010\x01@\x010\x01@\x01 \x01 \x01 '
                b'\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01\x10\x01 \x01 \x01 \x01\x00\x01 \x01\x00\x01\x10\x01 '
                b'\x01\x10\x01 \x01 \x01\x00\x01\x00\x01\x10\x01\x00\x01P\x01P\x01P\x01P\x01P\x01P\x010\x01@\x010'
                b'\x01P\x01P\x01P\x01P\x01P\x01P\x010\x01@\x010\x01@\x01`\x01@\x010\x01`\x010\x010\x01@\x01`\x01'
                b'@\x010\x01@\x010\x01@\x010\x01`\x01`\x01`\x01\x10\x01`\x01\x10\x01\x00\x01`\x01\x00\x01`\x01@\x010'
                b'\x01@\x010\x01@\x010\x01@\x010\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01`\x01\x00'
                b'\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01`\x01\x00\x01\x10\x01\x00\x010\x01`\x010\x01`\x01`\x01'
                b'`\x010\x01`\x010\x01\x00\x01\x10\x01\x00\x01`\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01\x00\x01'
                b'`\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01\x10\x01\x00\x01p\x01p\x01p\x01p\x01p\x01p\x01\x80\x01'
                b'\x80\x01\x80\x01 \x01p\x01p\x01 \x01p\x01p\x01 \x01\x80\x01\x80\x01p\x01 \x01p\x01p\x01 '
                b'\x01p\x01\x80\x01 \x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80\x01\x80'
                b'\x01 \x01\x80\x01\x80\x01 \x01\x80\x01\x80\x01 \x01\x80\x01\x80\x01\x80\x01 \x01\x80\x01\x80\x01 '
                b'\x01\x80\x01\x80\x01 \x01\x80\x01\x80\x01\x80\x01\x80\x01p\x01p\x01p\x01p\x01p\x01p\x01 '
                b'\x01\x80\x01\x80\x01 \x01p\x01p\x01 \x01 \x01 \x01\x80\x01\x80\x01\x80\x01p\x01p\x01p\x01 \x01 \x01 '
                b'\x01\x80\x01 \x01\x80\x01p\x01 \x01p\x01 \x01 \x01p')


# Sanity check generic NRL first
compressed = FileType.GENERIC_NRL.compress(bug)
decompressed = FileType.GENERIC_NRL.decompress(compressed, len(bug))[0]
print("---")
print(bug.hex())
print(decompressed.hex())
assert bug == decompressed

compressed = FileType.BPC_TILEMAP.compress(bug)
decompressed = FileType.BPC_TILEMAP.decompress(compressed, len(bug))
print("---")
print(bug.hex())
print(compressed.hex())
print(decompressed.hex())
assert bug == decompressed
