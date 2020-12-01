from cynergy import container
from cynergy.config import MemoryConfig

from detection.detector import FaceDetector
from detection.dog_face_detector import DogFaceDetector
from detection.human_face_detector import HumanFaceDetector
from face_modifiers.face_modifier import FaceModifier
from face_modifiers.skyrim_helmet_wearer import SkyrimHelmetWearer


def init(config: dict):
    container.initialize(MemoryConfig(config))

    container.register_many(FaceDetector, [HumanFaceDetector, DogFaceDetector])
    container.register_many(FaceModifier, [SkyrimHelmetWearer])
