from io import BytesIO
from typing import Tuple

import face_recognition

from detection.detector import FaceDetector


class HumanFaceDetector(FaceDetector):
    def detect(self, image: BytesIO) -> Tuple[int, int, int, int]:
        yield from face_recognition.face_locations(face_recognition.load_image_file(image))
