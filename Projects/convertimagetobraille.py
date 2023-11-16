import imageio.v2 as imageio
import os
import time
def main():
  image=imageio.imread(input("Image Path: "))
  contrastval=int(input("Contrast Percentage: "))
  addgrey=input("Generate with grey? (y/n): ")
  out2txt=input("Output to .txt? (y/n): ")
  grey=False
  o2txt=False
  starttime=time.time()
  if(addgrey.lower()=='y'):
    grey=True
  if(out2txt.lower()=='y'):
    o2txt=True
  with open("output.txt","w", encoding="utf-8") as txt:
    printout=""
    for i in range(int(image.shape[0]/3)):
      for j in range(int(image.shape[1]/2)):
        encochar=0
        if(rgb2dec(image[i*3,j*2])<=(0xFFFFFF*(contrastval/100))):
          encochar+=1
        if(rgb2dec(image[i*3+1,j*2])<=(0xFFFFFF*(contrastval/100))):
          encochar+=2
        if(rgb2dec(image[i*3+2,j*2])<=(0xFFFFFF*(contrastval/100))):
          encochar+=4
        if(rgb2dec(image[i*3,j*2+1])<=(0xFFFFFF*(contrastval/100))):
          encochar+=8
        if(rgb2dec(image[i*3+1,j*2+1])<=(0xFFFFFF*(contrastval/100))):
          encochar+=16
        if(rgb2dec(image[i*3+2,j*2+1])<=(0xFFFFFF*(contrastval/100))):
          encochar+=32
        if(encochar==0 and grey):
          if(rgb2dec(image[i*3,j*2])<=(0xFFFFFF*(contrastval/100))*1.5 and rgb2dec(image[i*3,j*2])<=(0xFFFFFF*0.95)):
            encochar=30
          elif(rgb2dec(image[i*3,j*2])<=(0xFFFFFF*(contrastval/100))*2 and rgb2dec(image[i*3,j*2])<=(0xFFFFFF*0.95)):
            encochar=42
          elif(rgb2dec(image[i*3,j*2])<=(0xFFFFFF*(contrastval/100))*3 and rgb2dec(image[i*3,j*2])<=(0xFFFFFF*0.95)):
            encochar=12
          elif(rgb2dec(image[i*3,j*2])<=(0xFFFFFF*(contrastval/100))*6 and rgb2dec(image[i*3,j*2])<=(0xFFFFFF*0.95)):
            encochar=8
        printout+=encochar2braille(encochar)
      printout+='\n'
    if(o2txt):
      txt.write(printout)
    else:
      print(printout)
  endtime=time.time()
  print(f"Completed in {endtime-starttime:.3f} seconds.")
def rgb2dec(rgbval):
  try:
    len(rgbval)
    return (rgbval[0]*0x10000)+(rgbval[1]*0x100)+(rgbval[2])
  except:
    return (rgbval*0x10000)+(rgbval*0x100)+(rgbval)
  
def encochar2braille(encochar):
  charlist=" ⠁⠂⠃⠄⠅⠆⠇⠈⠉⠊⠋⠌⠍⠎⠏⠐⠑⠒⠓⠔⠕⠖⠗⠘⠙⠚⠛⠜⠝⠞⠟⠠⠡⠢⠣⠤⠥⠦⠧⠨⠩⠪⠫⠬⠭⠮⠯⠰⠱⠲⠳⠴⠵⠶⠷⠸⠹⠺⠻⠼⠽⠾⠿"
  return charlist[encochar]

while(1):
  try:
    main()
    os.system('PAUSE')
  except Exception as e:
    print(e)
