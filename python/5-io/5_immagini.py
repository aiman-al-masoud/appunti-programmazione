# pip install pillow
# pillow

from PIL import Image
from PIL import ImageFilter
import os

# ottengo path e apro immagine
path = os.path.join(os.path.split(__file__)[0], "paperoga.png") 
im : Image.Image = Image.open(path)

# converto immagine in scala grigi:
im2 : Image.Image = im.convert(mode="L")

# visualizzo immagine in nuova finestra
im2.show()

# immagine sfocata
im2 = im2.filter(ImageFilter.GaussianBlur(radius=2))
im2.show()

