import base64
import io
from io import BytesIO

from PIL import Image

from .exceptions import ImageRequiredException


# TODO: do thubnail (youtube video)

def prepare_image_coordinates(coords) -> tuple:
    x1 = coords.get('x')
    y1 = coords.get('y')
    width = coords.get('width')
    height = coords.get('height')

    x2 = x1 + width
    y2 = y1 + height

    return x1, y1, x2, y2


def resize_image(tmp_image, coords=()):
    if tmp_image is None:
        raise ImageRequiredException()

    buffer = io.BytesIO()

    image = Image.open(f'media/{tmp_image}')
    image = image.crop(coords)
    image.save(buffer, format='png', optimize=True, quality=30)
    image.close()

    buffer.seek(0)

    return buffer, None


def crop_image(tmp_image, coords=()):
    if tmp_image is None:
        raise ImageRequiredException()

    image_b = tmp_image.split(',')[1]
    imgdata = base64.b64decode(image_b)

    buffer = BytesIO()
    image = Image.open(io.BytesIO(imgdata))
    image = image.crop(coords)
    image.thumbnail((1700, 459))
    image.save(buffer, format='png', optimize=True, quality=30)
    image.close()

    buffer.seek(0)

    return buffer, None
