"""
.. module:: manipulate_images.manipulate_images
   :synopsis: cut/crop/manipulate images.
"""
from PIL import Image
from loguru import logger

base_path = "images/"
zophie = "images/zophie.png"
cat_log = "images/catlogo.png"
SQUARE_FIT_SIZE = 300


def save_image(img: Image, file_name: str):
    try:
        img.save(file_name)
        logger.success(f"Image has been saved in {file_name}")
    except Exception as exc:
        logger.error(f"Error: {exc}")


def open_image(file_name) -> Image.open:
    return Image.open(file_name)


def crop_image(img: Image, save=False):
    cropped_img = img.crop((335, 345, 565, 560))
    return cropped_img


def copy_image(img: Image):
    return img.copy()


def paste_image(img: Image, img2: Image, x, y):
    return img.paste(img2, (x, y))


def paste_face_to_image():
    img = open_image(zophie)
    cat_copy = copy_image(img)
    face_img = crop_image(cat_copy)
    paste_image(cat_copy, face_img, 0, 0)
    paste_image(cat_copy, face_img, 400, 500)
    save_image(cat_copy, f"{base_path}pasted.png")


def resize(img: Image):
    width, height = img.size
    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to. if width > height:
        height = int((SQUARE_FIT_SIZE / width) * height)
        width = SQUARE_FIT_SIZE
    else:
        width = int((SQUARE_FIT_SIZE / height) * width)
        height = SQUARE_FIT_SIZE

    logger.info(f"Height: {height}, width: {width}")
    # Resize the image.
    return height, width


def paste_cat_logo_over_cat():
    img = open_image(zophie)
    img2 = open_image(cat_log)
    height, width = resize(img)
    height_logo, width_logo = resize(img2)
    img.paste(img2, (width - width_logo, height - height_logo), img2)
    save_image(img, f"{base_path}logo_over_cat.png")


if __name__ == "__main__":
    paste_cat_logo_over_cat()
