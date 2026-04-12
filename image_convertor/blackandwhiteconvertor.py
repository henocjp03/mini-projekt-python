from PIL import Image

def convertor(img_to_convert):
    img = Image.open(img_to_convert)
    img_bw = img.convert("L")

    name_result = input("Please enter the name of the converted file, example Burger.jpg ")
    while not name_result.endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif")):
        name_result = input("Please enter a valid filename, as this one does not have a valid image extension. Please enter a new one., example Burger.jpg ")
    return img_bw.save(name_result)

if __name__ == "__main__":
    bgu = convertor("image_convertor\chien.jpg")

    
