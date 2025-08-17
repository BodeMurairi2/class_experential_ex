#!/usr/bin/env python3

from typing import List, Optional

def is_valid_walk(walk:List[str])->Optional[bool]:
    """check for valid walk"""
    if len(walk)!=10:
        return False
    count = {
        "n":0,
        "s":0,
        "e":0,
        "w":0
    }
    for direction in walk:
        count[direction] = count[direction] + 1

    if count["n"] == count["s"] and count["e"] == count["w"]:
        return True

    return False

print(is_valid_walk(walk=["n","s", "s","n","e","e", "w", "w", "n", "s"]))
