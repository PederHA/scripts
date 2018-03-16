@echo off

for /F "usebackq tokens=1,2 delims==" %%i in (`wmic os get LocalDateTime /VALUE 2^>NUL`) do if '.%%i.'=='.LocalDateTime.' set ldt=%%j
set ldt=%ldt:~0,4%-%ldt:~4,2%-%ldt:~6,2%-%ldt:~8,2%-%ldt:~10,2%

copy "C:\Program Files (x86)\World of Warcraft\Logs\WoWCombatLog.txt" "C:\Program Files (x86)\World of Warcraft\Logs\Archive\WoWCombatLog%ldt%.txt"

forfiles /p "C:\Program Files (x86)\World of Warcraft\Logs" /m WoWCombatLog.txt /d -2 /c "cmd /c del @path"
forfiles /p "C:\Program Files (x86)\World of Warcraft\Logs\Archive" /m WoWCombatLog*.txt /d -7 /c "cmd /c del @path"
