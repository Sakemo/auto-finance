from PIL import Image

def Load_Image(image_path : str, resize_size : tuple):
    return Image.open(image_path).resize(resize_size)