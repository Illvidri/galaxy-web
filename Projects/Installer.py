import urllib.request
import os

print("Creating Directory")
try:
    os.mkdir("Project1",0o666)
    print("Directory Created")
except:
    print("Directory already exists")
#End

print("Installing Project1...")
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'User')
url = 'http://galaxy-web.net/Project1/readme.txt'
filename, headers = opener.retrieve(url, 'Project1/readme.txt')
url = 'http://galaxy-web.net/Project1/main.py'
filename, headers = opener.retrieve(url, 'Project1/main.py')
url = 'http://galaxy-web.net/Project1/PackageImporter.py'
filename, headers = opener.retrieve(url, 'Project1/PackageImporter.py')
url = 'http://galaxy-web.net/Project1/Package_Installer.bat'
filename, headers = opener.retrieve(url, 'Project1/Package_Installer.bat')
url = 'http://galaxy-web.net/Project1/Package_Uninstaller.bat'
filename, headers = opener.retrieve(url, 'Project1/Package_Uninstaller.bat')
print("Project1 successfully installed")
