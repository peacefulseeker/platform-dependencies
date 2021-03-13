from typing import Dict, List
import builtins
import keyword
import modulefinder

scores = {
    "builtin": 1,
    "keyword": 2,
    "module": 3,
}


def score_objects(objects: List[str], scores: Dict[str, int] = scores) -> int:
    score = 0

    for obj in objects:
        if keyword.iskeyword(obj):
            score += scores['keyword']

        if hasattr(builtins, obj):
            score += scores['builtin']

        try:
            __import__(obj)
            score += scores['module']
        except ModuleNotFoundError:
            pass

    return score
