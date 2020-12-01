import os
from io import BytesIO

from PIL import Image

from detection.dog_face_detector import DogFaceDetector
from detection.human_face_detector import HumanFaceDetector
from wearer.skyrim_helmet_wearer import SkyrimHelmetWearer

HELMET_PATH = 'skyrim.png'

detectors = [HumanFaceDetector(), DogFaceDetector()]
wearer = SkyrimHelmetWearer(HELMET_PATH)


def put_hat_on_it(image: BytesIO):
    img = Image.open(image)

    for location in _get_face_locations(image):
        img = wearer.wear(img, location)

    new_image = BytesIO()
    img.save(new_image, format=HELMET_PATH.split(os.path.extsep)[-1])
    new_image.seek(0)
    return new_image


def _get_face_locations(image: BytesIO):
    for detector in detectors:
        image.seek(0)
        yield from detector.detect(image)
