; For use with ARMIPS
; 2021/04/20
; For Explorers of Sky EU Only
; ------------------------------------------------------------------------------
; Change the way stats are displayed
; ------------------------------------------------------------------------------


.relativeinclude on
.nds
.arm

.definelabel StartAccuracyPos, 0x45
.definelabel StartPowerPos, 0x51

.definelabel MoveDescStartID, 0x000027A4
.definelabel MoveDescEndID, 0x000029D3
.definelabel SureShotID, 0x000027A2
.definelabel NoDamageID, 0x000027A3

.definelabel SPrintF, 0x0200D6BC
.definelabel GetMoveActualAccuracy, 0x02013C38
.definelabel GetMoveBasePowerWithID, 0x02013C90
.definelabel SetStringAccuracy, 0x020245C0
.definelabel SetStringPower, 0x02024688
.definelabel StrCpyFromFile, 0x02025B84
.definelabel StrCat, 0x02089B44
.definelabel PrintSpecialChar, 0x0209A150
.definelabel NullString, 0x0209A274
.definelabel SpecialCharString, 0x0209A2A8
