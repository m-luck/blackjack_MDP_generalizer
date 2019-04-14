# This file has functions related to high level player-decision heuristics and the game simulation.

import sub_probability as pr
from typing import Dict, List

def maybePass(my_score:int, other_score:int):
    '''
    Dictates if current player should perhaps pass, based on both player's scores and assuming a previous play.
    '''
    if my_score < other_score:
        return False # I am forced to draw, because if I pass, the other will have a higher score and win.
    return True

def makeOptimalChoice(playProb:float,passProb:float):
    if playProb >= passProb:
        return playProb,'Draw' # When comparing to pass or draw, we are slightly more inclusive of drawing (matches output). 
    return passProb, 'Pass'

def fillInElement(xt,yt,ncards,l,u,prob_arr,play_arr):
    playProb = pr.compute_prob(xt,yt,ncards,l,u,prob_arr)
    passProb = 1-pr.compute_prob(yt,xt,ncards,l,u,prob_arr) if maybePass(xt,yt) else 0 # Only computes other if passing may be optimal. 
    prob, choice = makeOptimalChoice(playProb, passProb)
    prob_arr[xt][yt] = prob
    play_arr[xt][yt] = choice
    return prob_arr, play_arr

def generateArrays(ncards:int,l:int,u:int):
    '''
    This populates the probability and play for every permutation of score.
    Because they rely on each other, it starts from near endgame and generates in a staircase, symmetric manner until the whole array is fulfilled.
    '''
    prob_arr = {}
    play_arr = {}
    for xt in range(l-1,-1,-1):
        prob_arr[xt] = {}
        play_arr[xt] = {}
        for yt in range(l-1,xt-1,-1):
            prob_arr, play_arr = fillInElement(xt,yt,ncards,l,u,prob_arr,play_arr)
            prob_arr, play_arr = fillInElement(yt,xt,ncards,l,u,prob_arr,play_arr) # Fills in inverse as well!
    return prob_arr, play_arr