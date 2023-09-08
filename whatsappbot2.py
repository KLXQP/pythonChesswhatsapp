import io
import requests
from PIL import Image
import os
import linkGen
import pywhatkit as pwk
import time

def imageCreate(url):
	if not any(os.scandir("C:/Users/admin/Desktop/python chess/images")):
		print("empty")
	else:
		os.remove("C:/Users/admin/Desktop/python chess/images/images.png")
		os.remove("C:/Users/admin/Desktop/python chess/images/images.jpg")
	w, h = 456, 456
	filepath = "C:/Users/admin/Desktop/python chess/images/images.png"
	filepathjpg = "C:/Users/admin/Desktop/python chess/images/images.jpg"

	r = requests.get(url, stream=True)
	if r.status_code == 200:
	    img = Image.open(io.BytesIO(r.content))
	    img.save(filepath)
	    imgJpeg = img.convert("RGB")
	    imgJpeg.save(filepathjpg, "JPEG")
def SendPos(fen):
	url = linkGen.linkGen(str(fen))
	imageCreate(url)
	pwk.sendwhats_image("+212XXXXXXXXX", "C:/Users/admin/Desktop/python chess/images/images.jpg")

if __name__ == "__main__":
	SendPos('8/2n1BB1K/p1P5/1P6/3p1p2/R1pp4/pP1k2P1/8 w - - 0 1')