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
url = 'http://galaxy-web.net/Project1/readme.txt'
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'User')
filename, headers = opener.retrieve(url, 'Project1/readme.txt')
print("Project1 successfully installed")
