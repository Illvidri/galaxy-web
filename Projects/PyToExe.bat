@echo off
echo This program requires 'pip.exe' of Python. If you don't have Python installed, I don't even know why you are using this
pause
echo Finding the path of 'pip.exe'; This may take a while
for /r %HOMEPATH%\AppData\Local\Programs %%a in (*) do if "%%~nxa"=="pip.exe" set p=%%~dpa
if defined p (
echo %p%
) else (
echo 'pip.exe' could not be located. This program will now end.
)
echo Successfully found 'pip.exe'. Now uninstalling pyinstaller
echo.
%p%/pip install pyinstaller
set /p FILENAME=Input File Name (Do not include the extension; Must be a .py file; Case Sensitive):
set /p ICONPATH=File Icon (Include extension; Must be a .ico file; Case Sensitive; Include path if needed): 
%p%/pyinstaller --onefile %FILENAME%.py --icon=%ICONPATH%
pause