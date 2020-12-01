from io import BytesIO
from typing import Tuple

import cv2
import dlib
import numpy as np
from cynergy.attributes import arguments
from cynergy.config import Config

from detection.detector import FaceDetector


@arguments(model_location=Config("DOG_MODEL_LOCATION"))
class DogFaceDetector(FaceDetector):
    def __init__(self, model_location: str):
        self.detector = dlib.cnn_face_detection_model_v1(model_location)

    def detect(self, image: BytesIO) -> Tuple[int, int, int, int]:
        data = np.fromstring(image.getvalue(), dtype=np.uint8)
        cv2_image = cv2.imdecode(data, 1)
        locations = self.detector(cv2_image)
        for location in locations:
            rect = location.rect
            yield rect.top(), rect.right(), rect.bottom(), rect.left()
