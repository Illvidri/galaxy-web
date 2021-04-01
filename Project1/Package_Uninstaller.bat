@echo off
echo Finding the path of 'pip.exe'; This may take a while
for /r %HOMEPATH%\AppData\Local\Programs %%a in (*) do if "%%~nxa"=="pip.exe" set p=%%~dpa
if defined p (
echo %p%
) else (
echo 'pip.exe' could not be located. This program will now end.
)
echo Successfully found 'pip.exe'. Now uninstalling packages
echo.
cd %p%
echo y | pip uninstall pyopengl
echo y | pip uninstall pygame
echo y | pip uninstall pyautogui
echo y | pip uninstall numpy
echo.
echo All packages have been successfully uninstalled.
timeout 3
