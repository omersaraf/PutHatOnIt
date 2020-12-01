from io import BytesIO
from typing import List

from PIL import Image

from detection.detector import FaceDetector
from face_modifiers.face_modifier import FaceModifier


class HatService:
    def __init__(self, detectors: List[FaceDetector], face_modifiers: List[FaceModifier]):
        self.face_modifiers = face_modifiers
        self.detectors = detectors

    def put_hat_on_it(self, image: BytesIO):
        img = Image.open(image)

        for location in self._get_face_locations(image):
            for modifier in self.face_modifiers:
                img = modifier.modify(img, location)

        new_image = BytesIO()
        img.save(new_image, format="png")
        new_image.seek(0)
        return new_image

    def _get_face_locations(self, image: BytesIO):
        for detector in self.detectors:
            image.seek(0)
            yield from detector.detect(image)
