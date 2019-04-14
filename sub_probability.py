import random 
from typing import Dict, List

def junct_of(events: List, start: int, op):
    prob = start
    if op=="con":
            for x in events: prob *= x 
    elif op=="dis":
            for x in events: prob += x
    return prob

def joint_of(events: List):
    return junct_of(events, 1, "con")

def union_of(events: List):
    return junct_of(events, 0, "dis")

def generateProb(x:int,y:int,ncards:int,l:int,u:int,prob:Dict):
    x_winning_prob = 0.0
    y_winning_prob = 0.0
    for n in range(ncards,0,-1): 
        print("Attempting",n)
        if x+n > u: 
            y_winning_prob = 1.0
        elif x+n >= l:
            y_winning_prob = 0
        else:
            y_winning_prob = prob[y][x+n]; 
        x_winning_prob += (1.0-y_winning_prob)/n; 
    return x_winning_prob 

def generateProbArray(ncards:int,l:int,u:int):
    prob_arr = {}
    for xt in range(l,0,-1):
        prob_arr[xt] = {}
        for yt in range(l,0,-1):
            prob = generateProb(xt,yt,ncards,l,u,prob_arr)
            prob_arr[xt][yt] = prob
            print(prob_arr)
    return prob_arr

