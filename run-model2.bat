@echo off
REM Dieses Skript startet das Python-Programm main3.py

REM Pfad zum Python-Interpreter
set PYTHON_PATH=C:\Users\julia\PycharmProjects\Woyzy\.venv\Scripts\python.exe

REM Pfad zum Python-Skript
set SCRIPT_PATH=C:\Users\julia\PycharmProjects\Woyzy\main4.py

REM Überprüfen, ob der Python-Interpreter existiert
if not exist "%PYTHON_PATH%" (
    echo Fehler: Python-Interpreter nicht gefunden: %PYTHON_PATH%
    exit /B 1
)

REM Überprüfen, ob das Skript existiert
if not exist "%SCRIPT_PATH%" (
    echo Fehler: Skript nicht gefunden: %SCRIPT_PATH%
    exit /B 1
)

REM Skript starten und Ausgaben anzeigen
"%PYTHON_PATH%" "%SCRIPT_PATH%"

REM Konsole offen halten, um die Ausgabe zu sehen
echo.
echo Das Skript main4.py wurde ausgefuehrt. Druecke eine Taste, um zu beenden.
pause
