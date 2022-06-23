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
from __future__ import annotations

import typing

from range_typed_integers import u16

from skytemple_files.graphics.bpa.handler import BpaHandler
from skytemple_files.graphics.bpa.protocol import (BpaFrameInfoProtocol,
                                                   BpaProtocol)
from skytemple_files.graphics.test.mocks.bpl_mock import SIMPLE_DUMMY_PALETTE
from skytemple_files.test.case import SkyTempleFilesTestCase, fixpath, romtest


class BpaTestCase(SkyTempleFilesTestCase[BpaHandler, BpaProtocol[BpaFrameInfoProtocol]]):
    handler = BpaHandler

    def setUp(self) -> None:
        self.one = self._load_main_fixture(self._fix_path1())
        self.assertIsNotNone(self.one)
        self.two = self._load_main_fixture(self._fix_path2())
        self.assertIsNotNone(self.two)

    def test_metadata(self) -> None:
        self.assertEqual(6, self.one.number_of_frames)
        self.assertEqual(12, self.one.number_of_tiles)
        self.assertEqual([bytearray(b'\x88\x88DH\x84DB\x14FDH\x14F\x84$\x14dHB\x12\x86H"\x12\x86DBd\x86D\x84\x18'), bytearray(b'A\xdd\xda\x00c\xd4\xdd\x00k\xd4\xad\x00\x1b\xd2\xad\x00\xbb\xde\xad\x00\xbb\xe5\xdd\x00\xbb\xe4\xad\x00\xb3\xd8\xae\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'a\x86\x88hf\x88D\x16f\x86\x841fa\x16\xb1fa\x113f\x11c\xccXQS\xc5D1\xb3\xbc'), bytearray(b'\xbb\xd4\xae\x00\xb3\xa5J\x00\xbbE$\x00\xbcA\x82\x00\xcc\x81\x88\x00\xbbch\x00\\\x11f\x00\xcc\x13a\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x86\x16\xb1\xcb\xa4b\xb1\xcc\x88\x12\xc5\xcbF"\xc5\xcc\x84"\xcb\\BfS;\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\xcb\x1b\x11\x00\xbck\x11\x00\xbc\x13\x16\x00\x15\x16\x16\x00\x11aa\x00\x11\x11\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x88\x88\x84\x84\x84D\x82\x84FDHVF\x84\x84\xb5dH\x82\xb5\x86H"\x12\x86DBT\x86D\x84X'), bytearray(b'\xa8\xda\xdd\x00\xa8\xda\xdd\x00\x81\xaa\xae\x00\x81\xaa\xad\x00\x81\xaa\xad\x00\xbb\xe5\xdd\x00\xb5\xe4\xad\x00\x9f\xd8\xae\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'a\x86\x88Uf\x88D\xbbf\x86\x84\xbbfa\x16\xfffa\x11\xfbf\x11\xf3\x9fXQ\xf3\x99D1\xf3\x99'), bytearray(b'\xf9\xd9\xae\x00\x99\xafJ\x00\x99I$\x00\x9fO\x82\x00\x9f\x89\x88\x00\x99oh\x00\x99\x1ff\x00\xfb\x1ca\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x86\x16\xb1\xfc\xa4b\xb1\xfb\x88\x12\xf5\xfbF"\xb5\xff\x84"\xbb\xbfBfS;\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\xff\x1b\x11\x00\xcbk\x11\x00\xbc\x13\x16\x00\x1b\x16\x16\x00\x11aa\x00\x11\x11\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x88\x88\x84\x84\x84D\x82\x84FDHVF\x84\x84\xb5dH\x82\xb5\x86H"\x12\x86DBT\x86D\x84X'), bytearray(b'\xa8\xda\xdd\x00\xa8\xda\xdd\x00\x81\xaa\xae\x00\x81\xaa\xad\x00\x81\xaa\xad\x00\xbb\xe5\xdd\x00\xb5\xe4\xad\x00\x9f\xd8\xae\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'a\x86\x88Uf\x88D\xbbf\x86\x84\xbbfa\x16\xfffa\x11\xfbf\x11\xf3\x9fXQ\xf3\x99D1\xf3\x99'), bytearray(b'\xf9\xd9\xae\x00\x99\xafJ\x00\x99I$\x00\x9fO\x82\x00\x9f\x89\x88\x00\x99oh\x00\x99\x1ff\x00\xfb\x1ca\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x86\x16\xb1\xfc\xa4b\xb1\xfb\x88\x12\xf5\xfbF"\xb5\xff\x84"\xbb\xbfBfS;\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\xff\x1b\x11\x00\xcbk\x11\x00\xbc\x13\x16\x00\x1b\x16\x16\x00\x11aa\x00\x11\x11\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x88\x88\x88\x88\x88\x88\x84\x84\x84D\x88\x84DBDVDB\x84\xb5\x88(\xb2\x9bH*XUD"8\xf5'), bytearray(b'\xa4\xdd~\x00\xa4\xed\xde\x00\xa8\xda\xdd\x00\x81\xaa\xde\x00\x81\xaa\xdd\x00e\xed\xaa\x00_\xe6\xdd\x00\xb9\xd3\xad\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'H\x86Q\x95\x88\x18\xb5\x9b\x86\x16\xb3\x9bfQ\xf5\xff\x11\xb6\xbb\xff1S\xff\x99\x13\xfb\x9f\x99\x11\xb3\x9f\xb9'), bytearray(b'\x9f\xab\xae\x00\xf9OM\x00\x99k"\x00\xf9;H\x00\x99?f\x00\xf9\x1bf\x00\xf9[\x16\x00\xcf?c\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'h\xb3\xcb\xff\x8aQ\xbb\xbf\x8aQ\xbf\xcf"V\xfb\xbfD\x14\xfb;\x84\x18S3\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\xbf\x15a\x00\xbc\x15\x81\x00\x1bch\x00\x1baf\x00\x111\x11\x00\x11\x11\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x88\x88\x84\x84\x84D\x82\x84FDHVF\x84\x84\xb5dH\x82\xb5\x86H"\x12\x86DBT\x86D\x84X'), bytearray(b'\xa8\xda\xdd\x00\xa8\xda\xdd\x00\x81\xaa\xae\x00\x81\xaa\xad\x00\x81\xaa\xad\x00\xbb\xe5\xdd\x00\xb5\xe4\xad\x00\x9f\xd8\xae\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'a\x86\x88Uf\x88D\xbbf\x86\x84\xbbfa\x16\xfffa\x11\xfbf\x11\xf3\x9fXQ\xf3\x99D1\xf3\x99'), bytearray(b'\xf9\xd9\xae\x00\x99\xafJ\x00\x99I$\x00\x9fO\x82\x00\x9f\x89\x88\x00\x99oh\x00\x99\x1ff\x00\xfb\x1ca\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x86\x16\xb1\xfc\xa4b\xb1\xfb\x88\x12\xf5\xfbF"\xb5\xff\x84"\xbb\xbfBfS;\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\xff\x1b\x11\x00\xcbk\x11\x00\xbc\x13\x16\x00\x1b\x16\x16\x00\x11aa\x00\x11\x11\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x88\x88DH\x84DB\x14FDH\x14F\x84$\x14dHB\x12\x86H"\x12\x86DBd\x86D\x84\x18'), bytearray(b'A\xdd\xda\x00c\xd4\xdd\x00k\xd4\xad\x00\x1b\xd2\xad\x00\xbb\xde\xad\x00\xbb\xe5\xdd\x00\xbb\xe4\xad\x00\xb3\xd8\xae\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'a\x86\x88hf\x88D\x16f\x86\x841fa\x16\xb1fa\x113f\x11c\xccXQS\xc5D1\xb3\xbc'), bytearray(b'\xbb\xd4\xae\x00\xb3\xa5J\x00\xbbE$\x00\xbcA\x82\x00\xcc\x81\x88\x00\xbbch\x00\\\x11f\x00\xcc\x13a\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x86\x16\xb1\xcb\xa4b\xb1\xcc\x88\x12\xc5\xcbF"\xc5\xcc\x84"\xcb\\BfS;\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\xcb\x1b\x11\x00\xbck\x11\x00\xbc\x13\x16\x00\x15\x16\x16\x00\x11aa\x00\x11\x11\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'), bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')], self.one.tiles)
        self.assertEqual(6, self.two.number_of_frames)
        self.assertEqual(12, self.two.number_of_tiles)
        self.assertEqual([bytearray(b'\xaa\xbb\xba\xaa*\xaa\xaa\xab\xba\xba\xba:\xba\xab\xab\xba\xaa\xbb\xaa;*\xba\xaa\xbb\xa2\xa3\xb3\xb3\xa3\xaa\xab:'), bytearray(b'\xa3\xaa\xaa\xba;\xaa\xbb\xbb\xbb\xab\xbb3\xbb3\xba\xa3;\xbb\xa3\xab\xbb3;237#\xa23;#\xac'), bytearray(b'wwwwwwwwwwwwwwwwwwwwwwwwswwwswww'), bytearray(b'\xba\xaa\xa3:\xaa\xab\xba\xa3\xaa*\xaa\xba\xbb\xaa\xaa\xba\xab+\xaa\xba\xab\xba\xaa\xa2\xbb\xab\xab\xaa3\xbb\xaa\xaa'), bytearray(b'\xb3s#,;7\'\xcc;w\'\xcc37\xa3\xcc3\xb3+\xc2\xba\xbb\xab\xcc\xbb3*\xc2\xba\xb3"\xcc'), bytearray(b'wwwwwww7uw\xb77sw73{w\xb3\xbbsw\xaa\xbbu7\xbb\xbb5s\xa3\xba'), bytearray(b'3\xbb\xab\xaaw:\xab\xaa;\xbb\xa3\xaaw\xba\xbb[s333z7;\xbawS\xaass\xa3\xaa\xbb'), bytearray(b'\xa2*\xc2\xcc\xa2""\xcc"\xa2\xcc\xccRR\xc5\\"\xc2\xcc\xcc*\xc2\xcc\xcc\xa7\xc2\xcc\xcc\'\xc5\xcc\xcc'), bytearray(b'2\xb7\xaa\xaa\xb2\xbb\xaa\xaa\xa2\xab+\xaa"\xaa\xaa\xaa"\xa2"\xaa,"\xaa\xa2\xac"\xa2""*\xaa\xa2'), bytearray(b'3\xba7:;w;\xb3{w7733ws;3s\xba\xaa\xaa\xba\xa5\xa5\xaa\xa5\xaaUUZ\xaa'), bytearray(b'w\xc5\xcc%w\xcc\\"\xaaR,"*""""""""""""\xa2","""\xc2'), bytearray(b'**\xa2\xaa\xa2\xa2\xaa*""""*""""\xc2""\xc2\xcc""",,"""""'), bytearray(b'\xaa\xbb\xba\xaa*\xaa\xaa\xab\xba\xba\xba:\xba\xab\xab\xba\xaa\xbb\xaa;*\xba\xaa\xbb\xa2\xa3\xb3\xb3\xa3\xaa\xab:'), bytearray(b'\xa3\xaa\xaa\xba;\xaa\xbb\xbb\xbb\xab\xbb3\xbb3\xba\xa3;\xbb\xb3;\xbb\xb3\xb3{3\xb7\xb3{3;Z\xb2'), bytearray(b'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'), bytearray(b'\xba\xaa\xa3:\xaa\xab\xba\xa3\xaa*\xaa\xba\xbb\xaa\xaa\xba\xab+\xaa\xba\xab\xba\xaa\xa2\xbb\xab\xab\xaa3\xbb\xaa\xaa'), bytearray(b"\xb3\xb3\xc5\xb2;\xb7\xc5\xb2;w\'\xcc37S\xc53\xb3[\xcc\xba\xbbU\xcc\xbb3\xcc\xcc\xba\xb3\xcc\xcc"), bytearray(b'wwwwwww7uw\xb77sw73{w\xb3\xbb|w\xaa\xbb|7\xbb\xbb<s\xa3\xba'), bytearray(b'3\xbb\xab\xaaw:\xab\xaa;\xbb\xa3\xaaw\xba\xbb[s333z7;\xbawS\xaass\xa3\xaa\xbb'), bytearray(b'\xa2*\xcc\xcc\xa2"\xcc\xcc"\xc2\xcc\xccR\xc2\xcc\xcc"\xc2\xcc\xcc*\xc2\xcc\xcc\xa7\xc2\xcc\xcc\'\xc5\xcc\xcc'), bytearray(b'<\xb7\xaa\xaa\xbc\xbb\xaa\xaa\xac\xab+\xaa,\xaa\xaa\xaa,\xa2"\xaa,"\xaa\xa2\xac"\xa2""*\xaa\xa2'), bytearray(b'3\xba7:;w;\xb3{w7733ws;3s\xba\xaa\xaa\xba\xa5\xa5\xaa\xa5\xaaUUZ\xaa'), bytearray(b'w\xc5\xcc,w\xcc\xcc"\xaaR,"*""""""""""""\xa2","""\xc2'), bytearray(b'**\xa2\xaa\xa2\xa2\xaa*""""*""""\xc2""\xc2\xcc""",,"""""'), bytearray(b'\xaa\xbb\xba\xaa*\xaa\xaa\xab\xba\xba\xba:\xba\xab\xab\xba\xaa\xbb\xaa;*\xba\xaa\xbb\xa2\xa3\xb3\xb3\xa3\xaa\xab:'), bytearray(b'\xa3\xaa\xaa\xba;\xaa\xbb\xbb\xbb\xab\xbb3\xbb3\xba\xa3;\xbb\xb3;\xbb3;;373\xbb3;#\xac'), bytearray(b'wwwwwwwwwwwwwwwwwwwwwwwwwwwwswww'), bytearray(b'\xba\xaa\xa3:\xaa\xab\xba\xa3\xaa*\xaa\xba\xbb\xaa\xaa\xba\xab+\xaa\xba\xab\xba\xaa\xa2\xbb\xab\xab\xaa3\xbb\xaa\xaa'), bytearray(b'\xb3s\xa3%;7[,;w\xcc\\3\xb7U\xc53\xb3R\xcc\xba+U\xcc\xbbR\xcc\xcc\xaa"\xcc\xcc'), bytearray(b'{www{ww7zw\xb77\xa5w73,w\xb3\xbb\xccw\xaa\xbb\xcc3\xbb\xbb\xccz\xa3\xba'), bytearray(b'3\xbb\xab\xaaw:\xab\xaa;\xbb\xa3\xaaw\xba\xbb+s33#z7;\xbawS\xaass\xa3\xaa\xbb'), bytearray(b'"U\xcc\xcc\xa2\xcc\xcc\xcc"\xc5\xcc\xcc\xc2\xcc\xcc\xcc"\xcc\xcc\xcc*\xcc\xcc\xcc+\xc5\xcc\xcc+\xc5\xcc\xcc'), bytearray(b'\xcc\xb2\xaa\xaa\xcc\xb2\xaa\xaa\xcc\xa2+\xaa\xcc\xa5\xaa\xaa\xcc""\xaa\\"\xaa\xa2\\"\xa2""*\xaa\xa2'), bytearray(b'3\xba7:;w;\xb3{w7733ws;3s\xba\xaa\xaa\xba\xa5\xa5\xaa\xa5\xaaUUZ\xaa'), bytearray(b'\xa7\xc5\xcc\xccw\xc2\xcc"\xaa"%"*""""""""""""\xa2","""\xc2'), bytearray(b'**\xa2\xaa\xa2\xa2\xaa*""""*""""\xc2""\xc2\xcc""",,"""""'), bytearray(b'\xaa\xbb\xba\xaa*\xaa\xaa\xab\xba\xba\xba:\xba\xab\xab\xba\xaa\xbb\xaa;*\xba\xaa\xbb\xa2\xa3\xb3\xb3\xa3\xaa\xab:'), bytearray(b'\xa3\xaa\xaa\xba;\xaa\xbb\xbb\xbb\xab\xbb3\xbb3\xba\xa3;\xbb\xb3;\xbb3;;373\xbb3;#\xac'), bytearray(b'wwwwwwwwwwwwwwwwwwwwwwwwwwwwswww'), bytearray(b'\xba\xaa\xa3:\xaa\xab\xba\xa3\xaa*\xaa\xba\xbb\xaa\xaa\xba\xab+\xaa\xba\xab\xba\xaa\xa2\xbb\xab\xab\xaa3\xbb\xaa\xaa'), bytearray(b'\xb3s\xa3%;7[,;w\xcc\\3\xb7U\xc53\xb3R\xcc\xba+U\xcc\xbbR\xcc\xcc\xaa"\xcc\xcc'), bytearray(b'{www{ww7zw\xb77\xa5w73,w\xb3\xbb\xccw\xaa\xbb\xcc3\xbb\xbb\xccz\xa3\xba'), bytearray(b'3\xbb\xab\xaaw:\xab\xaa;\xbb\xa3\xaaw\xba\xbb+s33#z7;\xbawS\xaass\xa3\xaa\xbb'), bytearray(b'"U\xcc\xcc\xa2\xcc\xcc\xcc"\xc5\xcc\xcc\xc2\xcc\xcc\xcc"\xcc\xcc\xcc*\xcc\xcc\xcc+\xc5\xcc\xcc+\xc5\xcc\xcc'), bytearray(b'\xcc\xb2\xaa\xaa\xcc\xb2\xaa\xaa\xcc\xa2+\xaa\xcc\xa5\xaa\xaa\xcc""\xaa\\"\xaa\xa2\\"\xa2""*\xaa\xa2'), bytearray(b'3\xba7:;w;\xb3{w7733ws;3s\xba\xaa\xaa\xba\xa5\xa5\xaa\xa5\xaaUUZ\xaa'), bytearray(b'\xa7\xc5\xcc\xccw\xc2\xcc"\xaa"%"*""""""""""""\xa2","""\xc2'), bytearray(b'**\xa2\xaa\xa2\xa2\xaa*""""*""""\xc2""\xc2\xcc""",,"""""'), bytearray(b'\xaa\xbb\xba\xaa*\xaa\xaa\xab\xba\xba\xba:\xba\xab\xab\xba\xaa\xbb\xaa;*\xba\xaa\xbb\xa2\xa3\xb3\xb3\xa3\xaa\xab:'), bytearray(b'\xa3\xaa\xaa\xba;\xaa\xbb\xbb\xbb\xab\xbb3\xbb3\xba\xa3;\xbb\xb3;\xbb\xb3\xb3{3\xb7\xb3{3;Z\xb2'), bytearray(b'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww'), bytearray(b'\xba\xaa\xa3:\xaa\xab\xba\xa3\xaa*\xaa\xba\xbb\xaa\xaa\xba\xab+\xaa\xba\xab\xba\xaa\xa2\xbb\xab\xab\xaa3\xbb\xaa\xaa'), bytearray(b"\xb3\xb3\xc5\xb2;\xb7\xc5\xb2;w\'\xcc37S\xc53\xb3[\xcc\xba\xbbU\xcc\xbb3\xcc\xcc\xba\xb3\xcc\xcc"), bytearray(b'wwwwwww7uw\xb77sw73{w\xb3\xbb|w\xaa\xbb|7\xbb\xbb<s\xa3\xba'), bytearray(b'3\xbb\xab\xaaw:\xab\xaa;\xbb\xa3\xaaw\xba\xbb[s333z7;\xbawS\xaass\xa3\xaa\xbb'), bytearray(b'\xa2*\xcc\xcc\xa2"\xcc\xcc"\xc2\xcc\xccR\xc2\xcc\xcc"\xc2\xcc\xcc*\xc2\xcc\xcc\xa7\xc2\xcc\xcc\'\xc5\xcc\xcc'), bytearray(b'<\xb7\xaa\xaa\xbc\xbb\xaa\xaa\xac\xab+\xaa,\xaa\xaa\xaa,\xa2"\xaa,"\xaa\xa2\xac"\xa2""*\xaa\xa2'), bytearray(b'3\xba7:;w;\xb3{w7733ws;3s\xba\xaa\xaa\xba\xa5\xa5\xaa\xa5\xaaUUZ\xaa'), bytearray(b'w\xc5\xcc,w\xcc\xcc"\xaaR,"*""""""""""""\xa2","""\xc2'), bytearray(b'**\xa2\xaa\xa2\xa2\xaa*""""*""""\xc2""\xc2\xcc""",,"""""'), bytearray(b'\xaa\xbb\xba\xaa*\xaa\xaa\xab\xba\xba\xba:\xba\xab\xab\xba\xaa\xbb\xaa;*\xba\xaa\xbb\xa2\xa3\xb3\xb3\xa3\xaa\xab:'), bytearray(b'\xa3\xaa\xaa\xba;\xaa\xbb\xbb\xbb\xab\xbb3\xbb3\xba\xa3;\xbb\xa3\xab\xbb3;237#\xa23;#\xac'), bytearray(b'wwwwwwwwwwwwwwwwwwwwwwwwswwwswww'), bytearray(b'\xba\xaa\xa3:\xaa\xab\xba\xa3\xaa*\xaa\xba\xbb\xaa\xaa\xba\xab+\xaa\xba\xab\xba\xaa\xa2\xbb\xab\xab\xaa3\xbb\xaa\xaa'), bytearray(b'\xb3s#,;7\'\xcc;w\'\xcc37\xa3\xcc3\xb3+\xc2\xba\xbb\xab\xcc\xbb3*\xc2\xba\xb3"\xcc'), bytearray(b'wwwwwww7uw\xb77sw73{w\xb3\xbbsw\xaa\xbbu7\xbb\xbb5s\xa3\xba'), bytearray(b'3\xbb\xab\xaaw:\xab\xaa;\xbb\xa3\xaaw\xba\xbb[s333z7;\xbawS\xaass\xa3\xaa\xbb'), bytearray(b'\xa2*\xc2\xcc\xa2""\xcc"\xa2\xcc\xccRR\xc5\\"\xc2\xcc\xcc*\xc2\xcc\xcc\xa7\xc2\xcc\xcc\'\xc5\xcc\xcc'), bytearray(b'2\xb7\xaa\xaa\xb2\xbb\xaa\xaa\xa2\xab+\xaa"\xaa\xaa\xaa"\xa2"\xaa,"\xaa\xa2\xac"\xa2""*\xaa\xa2'), bytearray(b'3\xba7:;w;\xb3{w7733ws;3s\xba\xaa\xaa\xba\xa5\xa5\xaa\xa5\xaaUUZ\xaa'), bytearray(b'w\xc5\xcc%w\xcc\\"\xaaR,"*""""""""""""\xa2","""\xc2'), bytearray(b'**\xa2\xaa\xa2\xa2\xaa*""""*""""\xc2""\xc2\xcc""",,"""""')], self.two.tiles)

        self.one.number_of_frames = u16(2)
        self.one.frame_info = self.one.frame_info[:2]
        self.one.number_of_tiles = u16(3)
        tiles = [bytearray(32)] * 6
        self.one.tiles = list(tiles)
        saved = self._save_and_reload_main_fixture(self.one)
        self.assertEqual(2, saved.number_of_frames)
        self.assertEqual(3, saved.number_of_tiles)
        self.assertEqual(tiles, saved.tiles)

    def test_frame_info(self) -> None:
        self.assertEqual(6, len(self.one.frame_info))
        for i in range(0, 6):
            self.assertEqual(10, self.one.frame_info[i].duration_per_frame)
            self.assertEqual(0, self.one.frame_info[i].unk2)
        self.assertEqual(6, len(self.two.frame_info))
        for i in range(0, 6):
            if i in (0, 1, 4, 5):
                self.assertEqual(5, self.two.frame_info[i].duration_per_frame)
            else:
                self.assertEqual(10, self.two.frame_info[i].duration_per_frame)
            self.assertEqual(0, self.two.frame_info[i].unk2)

        self.one.frame_info[0].duration_per_frame = u16(1)
        self.one.frame_info[1].duration_per_frame = u16(2)
        self.one.frame_info[2].duration_per_frame = u16(3)
        self.one.frame_info[3].duration_per_frame = u16(4)

        saved = self._save_and_reload_main_fixture(self.one)
        for i in range(0, 6):
            self.assertEqual(0, saved.frame_info[i].unk2)
        self.assertEqual(1, saved.frame_info[0].duration_per_frame)
        self.assertEqual(2, saved.frame_info[1].duration_per_frame)
        self.assertEqual(3, saved.frame_info[2].duration_per_frame)
        self.assertEqual(4, saved.frame_info[3].duration_per_frame)
        self.assertEqual(10, saved.frame_info[4].duration_per_frame)
        self.assertEqual(10, saved.frame_info[5].duration_per_frame)

    def test_get_tile(self) -> None:
        self.assertEqual(bytes(b'\x88\x88DH\x84DB\x14FDH\x14F\x84$\x14dHB\x12\x86H"\x12\x86DBd\x86D\x84\x18'), self.one.get_tile(0, 0))
        self.assertEqual(bytes(b'\xbb\xd4\xae\x00\xb3\xa5J\x00\xbbE$\x00\xbcA\x82\x00\xcc\x81\x88\x00\xbbch\x00\\\x11f\x00\xcc\x13a\x00'), self.one.get_tile(4, 0))
        self.assertEqual(bytes(b'\x88\x88\x84\x84\x84D\x82\x84FDHVF\x84\x84\xb5dH\x82\xb5\x86H"\x12\x86DBT\x86D\x84X'), self.one.get_tile(0, 1))
        self.assertEqual(bytes(b'\xf9\xd9\xae\x00\x99\xafJ\x00\x99I$\x00\x9fO\x82\x00\x9f\x89\x88\x00\x99oh\x00\x99\x1ff\x00\xfb\x1ca\x00'), self.one.get_tile(4, 2))
        self.assertEqual(bytes(b'\xaa\xbb\xba\xaa*\xaa\xaa\xab\xba\xba\xba:\xba\xab\xab\xba\xaa\xbb\xaa;*\xba\xaa\xbb\xa2\xa3\xb3\xb3\xa3\xaa\xab:'), self.two.get_tile(0, 0))
        self.assertEqual(bytes(b"\xb3s#,;7'\xcc;w'\xcc37\xa3\xcc3\xb3+\xc2\xba\xbb\xab\xcc\xbb3*\xc2\xba\xb3\"\xcc"), self.two.get_tile(4, 0))
        self.assertEqual(bytes(b'\xaa\xbb\xba\xaa*\xaa\xaa\xab\xba\xba\xba:\xba\xab\xab\xba\xaa\xbb\xaa;*\xba\xaa\xbb\xa2\xa3\xb3\xb3\xa3\xaa\xab:') , self.two.get_tile(0, 1))
        self.assertEqual(bytes(b'\xb3s\xa3%;7[,;w\xcc\\3\xb7U\xc53\xb3R\xcc\xba+U\xcc\xbbR\xcc\xcc\xaa"\xcc\xcc'), self.two.get_tile(4, 2))

    def test_tiles_to_pil(self) -> None:
        self.assertImagesEqual(self._fix_path_expected(("joined", "one.png")), self.one.tiles_to_pil(SIMPLE_DUMMY_PALETTE[1]))
        self.assertImagesEqual(self._fix_path_expected(("joined", "two.png")), self.two.tiles_to_pil(SIMPLE_DUMMY_PALETTE[1]))

    def test_tiles_to_pil_separate(self) -> None:
        for i, image in enumerate(self.one.tiles_to_pil_separate(SIMPLE_DUMMY_PALETTE[0], 1)):
            self.assertImagesEqual(self._fix_path_expected(("separate", "one", f"{i}.png")), image)
        for i, image in enumerate(self.two.tiles_to_pil_separate(SIMPLE_DUMMY_PALETTE[0], 1)):
            self.assertImagesEqual(self._fix_path_expected(("separate", "two", f"{i}.png")), image)

    def test_pil_to_tiles(self) -> None:
        self.one.pil_to_tiles(self._load_image(self._fix_path_joined()))
        saved = self._save_and_reload_main_fixture(self.one)
        self.assertImagesEqual(self._fix_path_joined(), saved.tiles_to_pil(SIMPLE_DUMMY_PALETTE[0]))

    def test_pil_to_tiles_separate(self) -> None:
        imgs = [
            self._load_image(self._fix_path_separate(0)),
            self._load_image(self._fix_path_separate(1)),
            self._load_image(self._fix_path_separate(2)),
            self._load_image(self._fix_path_separate(3)),
            self._load_image(self._fix_path_separate(4)),
            self._load_image(self._fix_path_separate(5)),
            self._load_image(self._fix_path_separate(6)),
        ]
        self.one.pil_to_tiles_separate(imgs)
        saved = self._save_and_reload_main_fixture(self.one)
        for source, img in zip(imgs, saved.tiles_to_pil_separate(SIMPLE_DUMMY_PALETTE[0], 1)):
            self.assertImagesEqual(source, img)
        self.assertImagesEqual(self._fix_path_joined(), saved.tiles_to_pil(SIMPLE_DUMMY_PALETTE[0]))

    def test_tiles_for_frame(self) -> None:
        self.assertEqual([b'\x88\x88DH\x84DB\x14FDH\x14F\x84$\x14dHB\x12\x86H"\x12\x86DBd\x86D\x84\x18', b'A\xdd\xda\x00c\xd4\xdd\x00k\xd4\xad\x00\x1b\xd2\xad\x00\xbb\xde\xad\x00\xbb\xe5\xdd\x00\xbb\xe4\xad\x00\xb3\xd8\xae\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'a\x86\x88hf\x88D\x16f\x86\x841fa\x16\xb1fa\x113f\x11c\xccXQS\xc5D1\xb3\xbc', b'\xbb\xd4\xae\x00\xb3\xa5J\x00\xbbE$\x00\xbcA\x82\x00\xcc\x81\x88\x00\xbbch\x00\\\x11f\x00\xcc\x13a\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x86\x16\xb1\xcb\xa4b\xb1\xcc\x88\x12\xc5\xcbF"\xc5\xcc\x84"\xcb\\BfS;\x00\x00\x00\x00\x00\x00\x00\x00', b'\xcb\x1b\x11\x00\xbck\x11\x00\xbc\x13\x16\x00\x15\x16\x16\x00\x11aa\x00\x11\x11\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'], self.one.tiles_for_frame(0))
        self.assertEqual([b'\x88\x88\x84\x84\x84D\x82\x84FDHVF\x84\x84\xb5dH\x82\xb5\x86H"\x12\x86DBT\x86D\x84X', b'\xa8\xda\xdd\x00\xa8\xda\xdd\x00\x81\xaa\xae\x00\x81\xaa\xad\x00\x81\xaa\xad\x00\xbb\xe5\xdd\x00\xb5\xe4\xad\x00\x9f\xd8\xae\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'a\x86\x88Uf\x88D\xbbf\x86\x84\xbbfa\x16\xfffa\x11\xfbf\x11\xf3\x9fXQ\xf3\x99D1\xf3\x99', b'\xf9\xd9\xae\x00\x99\xafJ\x00\x99I$\x00\x9fO\x82\x00\x9f\x89\x88\x00\x99oh\x00\x99\x1ff\x00\xfb\x1ca\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x86\x16\xb1\xfc\xa4b\xb1\xfb\x88\x12\xf5\xfbF"\xb5\xff\x84"\xbb\xbfBfS;\x00\x00\x00\x00\x00\x00\x00\x00', b'\xff\x1b\x11\x00\xcbk\x11\x00\xbc\x13\x16\x00\x1b\x16\x16\x00\x11aa\x00\x11\x11\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'], self.one.tiles_for_frame(1))
        self.assertEqual([b'\xaa\xbb\xba\xaa*\xaa\xaa\xab\xba\xba\xba:\xba\xab\xab\xba\xaa\xbb\xaa;*\xba\xaa\xbb\xa2\xa3\xb3\xb3\xa3\xaa\xab:', b'\xa3\xaa\xaa\xba;\xaa\xbb\xbb\xbb\xab\xbb3\xbb3\xba\xa3;\xbb\xa3\xab\xbb3;237#\xa23;#\xac', b'wwwwwwwwwwwwwwwwwwwwwwwwswwwswww', b'\xba\xaa\xa3:\xaa\xab\xba\xa3\xaa*\xaa\xba\xbb\xaa\xaa\xba\xab+\xaa\xba\xab\xba\xaa\xa2\xbb\xab\xab\xaa3\xbb\xaa\xaa', b'\xb3s#,;7\'\xcc;w\'\xcc37\xa3\xcc3\xb3+\xc2\xba\xbb\xab\xcc\xbb3*\xc2\xba\xb3"\xcc', b'wwwwwww7uw\xb77sw73{w\xb3\xbbsw\xaa\xbbu7\xbb\xbb5s\xa3\xba', b'3\xbb\xab\xaaw:\xab\xaa;\xbb\xa3\xaaw\xba\xbb[s333z7;\xbawS\xaass\xa3\xaa\xbb', b'\xa2*\xc2\xcc\xa2""\xcc"\xa2\xcc\xccRR\xc5\\"\xc2\xcc\xcc*\xc2\xcc\xcc\xa7\xc2\xcc\xcc\'\xc5\xcc\xcc', b'2\xb7\xaa\xaa\xb2\xbb\xaa\xaa\xa2\xab+\xaa"\xaa\xaa\xaa"\xa2"\xaa,"\xaa\xa2\xac"\xa2""*\xaa\xa2', b'3\xba7:;w;\xb3{w7733ws;3s\xba\xaa\xaa\xba\xa5\xa5\xaa\xa5\xaaUUZ\xaa', b'w\xc5\xcc%w\xcc\\"\xaaR,"*""""""""""""\xa2","""\xc2', b'**\xa2\xaa\xa2\xa2\xaa*""""*""""\xc2""\xc2\xcc""",,"""""'], self.two.tiles_for_frame(0))
        self.assertEqual([b'\xaa\xbb\xba\xaa*\xaa\xaa\xab\xba\xba\xba:\xba\xab\xab\xba\xaa\xbb\xaa;*\xba\xaa\xbb\xa2\xa3\xb3\xb3\xa3\xaa\xab:', b'\xa3\xaa\xaa\xba;\xaa\xbb\xbb\xbb\xab\xbb3\xbb3\xba\xa3;\xbb\xb3;\xbb\xb3\xb3{3\xb7\xb3{3;Z\xb2', b'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww', b'\xba\xaa\xa3:\xaa\xab\xba\xa3\xaa*\xaa\xba\xbb\xaa\xaa\xba\xab+\xaa\xba\xab\xba\xaa\xa2\xbb\xab\xab\xaa3\xbb\xaa\xaa', b"\xb3\xb3\xc5\xb2;\xb7\xc5\xb2;w'\xcc37S\xc53\xb3[\xcc\xba\xbbU\xcc\xbb3\xcc\xcc\xba\xb3\xcc\xcc", b'wwwwwww7uw\xb77sw73{w\xb3\xbb|w\xaa\xbb|7\xbb\xbb<s\xa3\xba', b'3\xbb\xab\xaaw:\xab\xaa;\xbb\xa3\xaaw\xba\xbb[s333z7;\xbawS\xaass\xa3\xaa\xbb', b'\xa2*\xcc\xcc\xa2"\xcc\xcc"\xc2\xcc\xccR\xc2\xcc\xcc"\xc2\xcc\xcc*\xc2\xcc\xcc\xa7\xc2\xcc\xcc\'\xc5\xcc\xcc', b'<\xb7\xaa\xaa\xbc\xbb\xaa\xaa\xac\xab+\xaa,\xaa\xaa\xaa,\xa2"\xaa,"\xaa\xa2\xac"\xa2""*\xaa\xa2', b'3\xba7:;w;\xb3{w7733ws;3s\xba\xaa\xaa\xba\xa5\xa5\xaa\xa5\xaaUUZ\xaa', b'w\xc5\xcc,w\xcc\xcc"\xaaR,"*""""""""""""\xa2","""\xc2', b'**\xa2\xaa\xa2\xa2\xaa*""""*""""\xc2""\xc2\xcc""",,"""""'], self.two.tiles_for_frame(1))

    @romtest(file_ext='bpa', path='MAP_BG/')
    def test_using_rom(self, _, file):
        bpa_before = self.handler.deserialize(file)
        bpa_after = self._save_and_reload_main_fixture(bpa_before)

        self.assertEqual(bpa_before.number_of_tiles, bpa_after.number_of_tiles)
        self.assertEqual(bpa_before.number_of_frames, bpa_after.number_of_frames)
        self.assertEqual(bpa_before.tiles, bpa_after.tiles)
        self.assertEqual(len(bpa_before.frame_info), len(bpa_after.frame_info))
        for frame_before, frame_after in zip(bpa_before.frame_info, bpa_after.frame_info):
            self.assertEqual(frame_before.duration_per_frame, frame_after.duration_per_frame)
            self.assertEqual(frame_before.unk2, frame_after.unk2)

    @typing.no_type_check
    @classmethod
    @fixpath
    def _fix_path1(cls):
        return '..', '..', 'test', 'fixtures', 'MAP_BG', 'coco1.bpa'

    @typing.no_type_check
    @classmethod
    @fixpath
    def _fix_path2(cls):
        return '..', '..', 'test', 'fixtures', 'MAP_BG', 'coco2.bpa'

    @typing.no_type_check
    @classmethod
    @fixpath
    def _fix_path_expected(cls, subpath):
        return 'fixtures', 'expected', *subpath

    @typing.no_type_check
    @classmethod
    @fixpath
    def _fix_path_separate(cls, number):
        return 'fixtures', 'separate', f'{number}.png'

    @typing.no_type_check
    @classmethod
    @fixpath
    def _fix_path_joined(cls):
        return 'fixtures', 'joined.png'
