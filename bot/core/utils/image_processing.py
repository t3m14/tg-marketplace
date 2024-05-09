

def convert_telegram_image_to_bytes(image):
    image_bytes = image.get_file().download_as_bytearray()
    return image_bytes