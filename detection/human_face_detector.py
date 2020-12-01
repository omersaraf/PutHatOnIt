from io import BytesIO

import face_recognition


class HumanFaceDetector:
    @staticmethod
    def detect(image: BytesIO):
        yield from face_recognition.face_locations(face_recognition.load_image_file(image))

