
#Python Standard Library Import Sequence; If this fails, what on Earth is wrong with your Python??
import time
import subprocess

#OpenGL Import Sequence
OpenGLSuccess = False; OpenGLGLSuccess = False; OpenGLGLUTSuccess = False; OpenGLGLUSuccess = False
try: import OpenGL; print("Imported OpenGL"); OpenGLSuccess = True
except: print("Failed to import OpenGL")
try: from OpenGL.GL import *; print("Imported OpenGL.GL"); OpenGLGLSuccess = True
except: print("Failed to import OpenGL.GL")
try: from OpenGL.GLUT import *; print("Imported OpenGL.GLUT"); OpenGLGLUTSuccess = True
except: print("Failed to import OpenGL.GLUT")
try: from OpenGL.GLU import *; print("Imported OpenGL.GLU"); OpenGLGLUSuccess = True
except: print("Failed to import OpenGL.GLU")
if(OpenGLSuccess == True and OpenGLGLSuccess == True and OpenGLGLUTSuccess == True and OpenGLGLUSuccess == True): print("OpenGL has been successfully imported.")
else: print("OpenGL has failed to import; be sure to run the installation program before attempting to execute the program."); time.sleep(1)

#Pygame Import Sequence
PygameSuccess = False
try: import pygame as pg; from pygame.locals import *; PygameSuccess = True
except: print("Failed to import pygame")
if(PygameSuccess == True): print("Pygame has been successfully imported.")
else: print("Pygame has failed to import; be sure to run the installation program before attempting to execute the program."); time.sleep(1)

#PyAutoGUI Import Sequence
PAGSuccess = False
try: import pyautogui as pag; PAGSuccess = True
except: print("Failed to import PyAutoGUI")
if(PAGSuccess == True): print("PyAutoGUI has been successfully imported.")
else: print("PyAutoGUI has failed to import; be sure to run the installation program before attempting to execute the program."); time.sleep(1)

#NumPy Import Sequence
NumPySuccess = False
try: import numpy; NumPySuccess = True
except: print("Failed to import NumPy")
if(NumPySuccess == True): print("NumPy has been successfully imported.")
else: print("NumPy has failed to import; be sure to run the installation program before attempting to execute the program."); time.sleep(1)

time.sleep(2)

if(OpenGLSuccess == False or OpenGLGLSuccess == False or OpenGLGLUTSuccess == False or OpenGLGLUSuccess == False or PygameSuccess == False or PAGSuccess == False or NumPySuccess == False):
    getInstall = input("Would you like to install the packages (y/n): ")
    if(getInstall.lower() == 'y'):
        print("Installing Packages")
        subprocess.call([r'Package_Installer.bat'])
        print("Packages have been installed. If there were errors when installing, or if the program is not working, something may be wrong with 'pip.exe'\n\n")
    else:
        print("An input that was not 'y' or 'Y' was entered. The installation will not take place.\n\n")
        time.sleep(2)
        quit()
    #End
#End



