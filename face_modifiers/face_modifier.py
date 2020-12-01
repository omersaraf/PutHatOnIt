from typing import Tuple

from PIL import Image


class FaceModifier:
    def modify(self, image: Image, face_location: Tuple[int, int, int, int]):
        raise NotImplementedError
