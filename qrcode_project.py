# -*- coding: utf-8 -*-


import qrcode

#qr encoder

link="https://www.linkedin.com/in/yugandhar-veesam-a549a71b5/"

img=qrcode.make(link)

img.save('E:\myqrcode.png')



#qr decoder

#pip install opencv-python

import cv2
d=cv2.QRCodeDetector()

val,points,st=d.detectAndDecode(cv2.imread('E:\myqrcode.png'))
print(val)

