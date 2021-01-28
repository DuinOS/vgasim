from PIL import Image 
import sys
import os
 
n = len(sys.argv)
print(n)
if (n < 2) or (n > 3):
   print("Use: python convert.py imagefile.ext memfile.hex .\n")
   exit(1)

fimagname = ""
if n >= 2:
   fimagname = sys.argv[1]

if n == 3:
   fhexname = sys.argv[2]
else:
   fhexname = os.path.splitext(fimagname)[0] + '.hex'

img = Image.open(fimagname) 
 
ihex = img.tobytes("hex", "rgb") 
ihexline = ihex.splitlines()
fhex = ""
ccount = 0
for line in ihexline:
   ncount = 0
   for bt in line:
      ncount += 1
      if ncount == 1:
         fhex += "00"
         ncount += 2
      
      fhex += chr(bt)
      
      if ncount == 8:
         fhex += ' '
         ncount = 0
         ccount += 1
         if ccount == 4:
            fhex += '\n'
            ccount = 0
      
      
f = open(fhexname,'w')
f.write(fhex)
f.close()

print(fhex)
print(img)
