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
import warnings

from skytemple_files.common.ppmdu_config.script_data import Pmd2ScriptData, Pmd2ScriptObject
from skytemple_files.common.util import AutoString
from skytemple_files.script.ssa_sse_sss.position import SsaPosition


class SsaObject(AutoString):
    def __init__(self, scriptdata: Pmd2ScriptData, object_id, unk4, unk6, pos: SsaPosition, script_id, unk12):
        try:
            self.object = scriptdata.objects__by_id[object_id]
        except KeyError:
            warnings.warn(f"[{self.__class__.__name__}]: Unknown object id: {object_id}")
            self.object = Pmd2ScriptObject(object_id, 0, 0, 0, 'UNKNOWN')
        self.unk4 = unk4
        self.unk6 = unk6
        self.pos = pos
        self.script_id = script_id
        self.unk12 = unk12
