from PIL import Image

def get_image_size(my_image):
    try:
        with Image.open(my_image) as img:
            return img.size
    except:
        print('Image file name error')

#####

imageFile = input('Type image file name: ')

print(get_image_size(imageFile))
