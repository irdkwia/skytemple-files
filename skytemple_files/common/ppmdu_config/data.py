"""
Main static configuration for SkyTemple itself and a ROM.
For now, the documentation of fields is in the pmd2data.xml.
"""
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
from typing import List, Dict

from skytemple_files.common.ppmdu_config.script_data import Pmd2ScriptData
from skytemple_files.common.util import AutoString


GAME_VERSION_EOT = 'EoT'
GAME_VERSION_EOD = 'EoD'
GAME_VERSION_EOS = 'EoS'

GAME_REGION_US = 'US'
GAME_REGION_EU = 'EU'
GAME_REGION_JP = 'JP'


LANG_JP = 'japanese'
LANG_EN = 'english'
LANG_FR = 'french'
LANG_DE = 'german'
LANG_IT = 'italian'
LANG_SP = 'spanish'


class Pmd2GameEdition(AutoString):
    def __init__(self, id: str, gamecode: str, region: str, arm9off14: int, defaultlang: str, issupported: bool):
        self.id = id
        self.gamecode = gamecode
        self.region = region
        self.arm9off14 = arm9off14
        self.defaultlang = defaultlang
        self.issupported = issupported


class Pmd2BinaryBlock(AutoString):
    def __init__(self, name: str, begin: int, end: int):
        self.name = name
        self.begin = begin
        self.end = end
        self.parent = None

    def add_parent(self, parent: 'Pmd2Binary'):
        self.parent = parent

    @property
    def begin_absolute(self):
        return self.parent.loadaddress + self.begin


class Pmd2BinaryFunction(AutoString):
    def __init__(self, name: str, begin: int):
        self.name = name
        self.begin = begin
        self.parent = None

    def add_parent(self, parent: 'Pmd2Binary'):
        self.parent = parent

    @property
    def begin_absolute(self):
        return self.parent.loadaddress + self.begin


class Pmd2BinaryPointer(AutoString):
    def __init__(self, name: str, begin: int):
        self.name = name
        self.begin = begin
        self.parent = None

    def add_parent(self, parent: 'Pmd2Binary'):
        self.parent = parent

    @property
    def begin_absolute(self):
        return self.parent.loadaddress + self.begin


class Pmd2Binary(AutoString):
    def __init__(self, filepath: str, loadaddress: int, blocks: List[Pmd2BinaryBlock], functions: List[Pmd2BinaryFunction], pointers: List[Pmd2BinaryPointer]):
        self.filepath = filepath
        self.loadaddress = loadaddress
        self.blocks = {x.name: x for x in blocks}
        self.functions = {x.name: x for x in functions}
        self.pointers = {x.name: x for x in pointers}


class Pmd2Language(AutoString):
    def __init__(self, filename: str, name: str, locale: str):
        self.filename = filename
        self.name = name
        self.locale = locale


class Pmd2StringBlock(AutoString):
    def __init__(self, name: str, begin: int, end: int):
        self.name = name
        self.begin = begin
        self.end = end


class Pmd2StringIndexData(AutoString):
    def __init__(self, languages: List[Pmd2Language], string_blocks: List[Pmd2StringBlock]):
        self.languages = languages
        self.string_blocks: Dict[str, Pmd2StringBlock] = {blk.name: blk for blk in string_blocks}


class Pmd2Data(AutoString):
    def __init__(self,
                 game_edition: str,
                 game_editions: List[Pmd2GameEdition],
                 game_constants: Dict[str, int],
                 binaries: List[Pmd2Binary],
                 string_index_data: Pmd2StringIndexData,
                 script_data: Pmd2ScriptData):
        self.game_edition = game_edition
        self.game_version = game_edition.split('_')[0]
        self.game_region = game_edition.split('_')[1]
        self.game_editions: Dict[str, Pmd2GameEdition] = {edi.id: edi for edi in game_editions}
        self.game_constants = game_constants
        self.binaries: Dict[str, Pmd2Binary] = {x.filepath: x for x in binaries}
        self.string_index_data = string_index_data
        # asm patches constants currently not used
        self.script_data = script_data
