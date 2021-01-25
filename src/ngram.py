from collections import defaultdict
from typing import DefaultDict, Tuple

from typing_extensions import Literal


def to_ngram(s: str, n: int = 2, mode: Literal["word", "char"] = "word"
             ) -> DefaultDict[Tuple[str, ...], int]:
    # split
    if mode == "word":
        grams = s.split()
    elif mode == "char":
        grams = list(s)
    else:
        raise NotImplementedError(f"mode {mode} is not implemented")

    # collect
    gram_dict = defaultdict(int)
    for i in range(len(grams)-n+1):
        gram_dict[tuple(grams[i:i+n])] += 1
    return gram_dict
