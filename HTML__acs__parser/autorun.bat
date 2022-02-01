@echo off

Rem https://stackoverflow.com/a/58530843
Rem https://stackoverflow.com/a/6362922
Rem https://stackoverflow.com/a/58882066

SET command=python C:\Users\pompeii\Source\Repos\SpiritasX\HTML__acs__parser\HTML__acs__parser\HTML__acs__parser.py %1

FOR /F "tokens=* USEBACKQ" %%F IN (`%command%`) DO (SET var=%%F)

start /b C:\Users\pompeii\Source\Repos\SpiritasX\HTML__acs__parser\HTML__acs__parser\balloon.bat "%var%"
