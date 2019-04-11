import random 
from typing import List

def conditional(a, givenB):
    pass

def junct_of(events: List, start: int, op):
    prob = start
    if events:
        for x in events:
            prob *= x
    else:
        prob = 0
    return prob

def joint_of(events: List):
    pass

def union_of(events: List):
    pass