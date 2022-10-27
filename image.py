from PIL import Image

if __name__ == "__name__":
    im = Image.open("./img.jpg")
    out = im.resize((128,128))
    out.show()