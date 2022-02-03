@echo off

Rem https://stackoverflow.com/a/58530843
Rem https://stackoverflow.com/a/6362922
Rem https://stackoverflow.com/a/58882066

SET command=python C:\Users\pompeii\Source\Repos\SpiritasX\HTML__acs__parser\HTML__acs__parser\HTML__acs__parser.py %1

:repeat
SET var=
FOR /F "tokens=* USEBACKQ" %%F IN (`%command%`) DO (SET var=%%F)

IF "%var%" NEQ "" start /b C:\Users\pompeii\Source\Repos\SpiritasX\HTML__acs__parser\HTML__acs__parser\balloon.bat "%var%"
timeout /t 600 /nobreak > NUL
goto repeat