from Log_Writer.logger import App_Logger
from PIL import Image
import io
import re
import base64
logger=App_Logger()

def decodeImage(base64_string):
    try:
        base64_string=re.sub("^data:image/.+;base64,", '',base64_string)
        imgdata=base64.b64decode(base64_string)
        image = Image.open(io.BytesIO(imgdata))
        logger.log("Base64 String Converted/Decoded to Image")
        return image
    except Exception as e:
        logger.log(f"ERROR : Error occurred in decoding base64 string\n")
        logger.log(f"ERROR : {e} \n")
        return print(e)
