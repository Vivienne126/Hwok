import os ,io,time , random, requests , mimetypes
from datetime import datetime
from PIL import Image,ImageDraw,ImageFont
from config import HF_API_KEY

MODEL = "facebook/detr-resnet-50"
API=f"https://api-inference.huggingface.co/models/{MODEL}"
allowded , max_mb = {".jpg",".jpeg",".png",".bmp",".gif",".webp",".tiff"}, 8
emoji= {"person":"🧍","car":"🚗","truck":"🚚","bus":"🚌","bicycle":"🚲","motorcycle":"🏍️","dog":"🐶","cat":"🐱","bird":"🐦","horse":"🐴","sheep":"🐑","cow":"🐮","bear":"🐻","giraffe":"🦒","zebra":"🦓","banana":"🍌","apple":"🍎","orange":"🍊","pizza":"🍕","broccoli":"🥦","book":"📘","laptop":"💻","tv":"📺","bottle":"🧴","cup":"🥤"}

def font(sz=18):
    for f in("DejaVuSans.ttf","arial.ttf"):
        try:
            return ImageFont.truetype(f,sz)
        except:
            pass
    return ImageFont.load_default()

