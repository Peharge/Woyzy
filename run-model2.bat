@echo off

set PYTHON_PATH=C:\Users\julia\PycharmProjects\Woyzy\.venv\Scripts\python.exe

set SCRIPT_PATH=C:\Users\julia\PycharmProjects\Woyzy\main4.py

if not exist "%PYTHON_PATH%" (
    echo Fehler: Python-Interpreter nicht gefunden: %PYTHON_PATH%
    exit /B 1
)

if not exist "%SCRIPT_PATH%" (
    echo Fehler: Skript nicht gefunden: %SCRIPT_PATH%
    exit /B 1
)

"%PYTHON_PATH%" "%SCRIPT_PATH%"

echo.
echo Das Skript main4.py wurde ausgefuehrt. Druecke eine Taste, um zu beenden.
pause
