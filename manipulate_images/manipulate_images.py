"""
.. module:: manipulate_images.manipulate_images
   :synopsis: cut/crop/manipulate images.
"""
from PIL import Image
from loguru import logger

base_path = "images/"
zophie = "images/zophie.png"


def save_image(img: Image, file_name: str):
    try:
        img.save(file_name)
        logger.success(f"Image has been saved in {file_name}")
    except Exception as exc:
        logger.error(f"Error: {exc}")


def open_image(file_name) -> Image.open:
    return Image.open(file_name)


def crop_image(save=False):
    img = open_image(zophie)
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


if __name__ == "__main__":
    paste_face_to_image()
