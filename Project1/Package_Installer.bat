@echo off
echo Finding the path of 'pip.exe'; This may take a while
for /r %HOMEPATH%\AppData\Local\Programs %%a in (*) do if "%%~nxa"=="pip.exe" set p=%%~dpa
if defined p (
echo %p%
) else (
echo 'pip.exe' could not be located. This program will now end.
)
echo Successfully found 'pip.exe'. Now commencing installation
echo.
cd %p%
pip install pyopengl
pip install pygame
pip install pyautogui
pip install numpy
echo.
echo All packages have been successfully installed.
timeout 3
