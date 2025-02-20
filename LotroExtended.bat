@echo off

rem LotroExtended.bat
rem by qtPyDev

echo ~~~~~ setting up LotroExtended ~~~~~

call :loadLotroExtended

echo ~~~~~ successfully loaded LotroExtended ~~~~~

exit

:loadLotroExtended
    echo ~~~~~ loading loadLotroExtended ~~~~~

    python lotro_extended.py

    exit /b
