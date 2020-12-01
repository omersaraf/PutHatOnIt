from typing import Tuple

from PIL import Image
from cynergy.attributes import arguments
from cynergy.config import Config

from face_modifiers.face_modifier import FaceModifier

IMAGE_SPACE_BUFFER = 1.3
HORNS_RATIONAL_SIZE = 0.25
HELMET_TOP_RATIONAL_POSITION = 0.4


@arguments(image_location=Config("SKYRIM_HELMET_LOCATION"))
class SkyrimHelmetWearer(FaceModifier):
    def __init__(self, image_location: str):
        self.helmet = Image.open(image_location)

    def modify(self, image: Image, face_location: Tuple[int, int, int, int]):
        top, right, bottom, left = face_location

        spaced_size_y = int((right - left) * IMAGE_SPACE_BUFFER)
        new_helmet_size = (int(self.helmet.size[0] * spaced_size_y / self.helmet.size[1]), spaced_size_y)
        temp = self.helmet.resize(new_helmet_size)

        image.paste(temp, (
            left - int(temp.size[0] * HORNS_RATIONAL_SIZE),
            top - int(temp.size[1] * HELMET_TOP_RATIONAL_POSITION)),
                    temp)

        return image
