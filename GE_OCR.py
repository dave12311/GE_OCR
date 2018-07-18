from psd_tools import PSDImage
from PIL import Image
import pytesseract
import glob, os

for file in glob.glob("*.psd"):
	psd = PSDImage.load(file)

	for item in psd.layers:
		if item.name == "Background" or item.name == "Háttérszín":
			image = item.as_PIL()
			w, h = image.size
			cropped = image.crop((w-350,h-70,w,h))
			cropped = cropped.resize((1750,350), resample=Image.BILINEAR) #5x magnification
			text = pytesseract.image_to_string(cropped,config='GE')
			text = text.replace(" ", "")
			text = text.replace("-", "")
			#cropped.save(text + ".png")
			print(text)
			f = open(str(text)+".txt","w")
			f.write(str(file))
			f.close()
			try:
				os.rename(file, text + ".psd")
			except OSError:
				print("File ", file, " already exists with code ", text)
print("Done.")
os.system("pause")
