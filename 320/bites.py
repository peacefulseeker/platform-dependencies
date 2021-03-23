from dataclasses import dataclass
import enum
from typing import List  # TODO: can remove >= 3.9


# 1. make a BiteLevel enum class
# keys = INTRO BEGINNER INTERMEDIATE ADVANCED
# values = 1 2 3 4
# make sure they can be sorted by int value
class BiteLevel(enum.IntEnum):
    INTRO = 1
    BEGINNER = 2
    INTERMEDIATE = 3
    ADVANCED = 4


# 2. make a dataclass that can be ordered
# attributes: number (int), title (str), level (BiteLevel)
@dataclass(order=True)
class Bite:
    number: int
    title: str
    level: int = BiteLevel.BEGINNER


# 3. complete the function below

def create_bites(numbers: List[int], titles: List[str], levels: List[BiteLevel]):
    """Generate a generator of Bite dataclass objects"""
    return [Bite(*args) for args in zip(numbers, titles, levels)]
