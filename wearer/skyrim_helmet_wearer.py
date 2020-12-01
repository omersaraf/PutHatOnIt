from typing import Tuple

from PIL import Image

IMAGE_SPACE_BUFFER = 1.3
HORNS_RATIONAL_SIZE = 0.25
HELMET_TOP_RATIONAL_POSITION = 0.4


class SkyrimHelmetWearer:
    def __init__(self, image_location):
        self.helmet = Image.open(image_location)

    def wear(self, image: Image, location: Tuple[int, int, int, int]):
        top, right, bottom, left = location

        spaced_size_y = int((right - left) * IMAGE_SPACE_BUFFER)
        new_helmet_size = (int(self.helmet.size[0] * spaced_size_y / self.helmet.size[1]), spaced_size_y)
        temp = self.helmet.resize(new_helmet_size)

        image.paste(temp, (
            left - int(temp.size[0] * HORNS_RATIONAL_SIZE),
            top - int(temp.size[1] * HELMET_TOP_RATIONAL_POSITION)),
                    temp)

        return image
