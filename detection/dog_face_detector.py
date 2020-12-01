from io import BytesIO

import cv2
import dlib
import numpy as np


class DogFaceDetector:
    def __init__(self):
        self.detector = dlib.cnn_face_detection_model_v1('dogHeadDetector.dat')

    def detect(self, image: BytesIO):
        data = np.fromstring(image.getvalue(), dtype=np.uint8)
        cv2_image = cv2.imdecode(data, 1)
        locations = self.detector(cv2_image)
        for location in locations:
            rect = location.rect
            yield rect.top(), rect.right(), rect.bottom(), rect.left()
