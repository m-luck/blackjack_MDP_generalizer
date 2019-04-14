# This file has functions related to high level player-decision heuristics and the game simulation.

import sub_probability as pr
from typing import Dict, List

def maybePass(my_score:int, other_score:int):
    '''
    Dictates if current player should perhaps pass, based on the previous player's decision and both player's scores.
    '''
    if my_score < other_score:
        return False # I am forced to draw, because if I pass, other will have a higher score and win.
    return True

def makeOptimalChoice(playProb:float,passProb:float):
    if playProb > passProb:
        return playProb,'DRAW'   
    return passProb, 'PASS'

def fillInElement(xt,yt,ncards,l,u,prob_arr,play_arr):
    playProb = pr.compute_prob(xt,yt,ncards,l,u,prob_arr)
    passProb = 1-playProb if maybePass(xt,yt) else 0
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
            prob_arr, play_arr = fillInElement(yt,xt,ncards,l,u,prob_arr,play_arr)
    return prob_arr, play_arr

# def nextTurnIs(h:List):
#     '''
#     Returns the player ID of whose turn is next.
#     '''
#     state = h[-1]
#     return other(state['turn'])

# def game_march(p:int,h:List):
#     '''
#     This will move the game forward by one time step with optimal players. 
#     Optimal move is determined by a game history state consisting of three parts:
#     Whether or not the player Y has just passed, X’s total points, and Y’s total points. '''
#     state = h[-1].copy()
#     state['turn'] = nextTurnIs(state)
#     score = state['val'][p]
#     if state['choice'] == 'draw':
#         newP = val + pr.draw()
#     state['val'][p] = newP

# def addHistory(h:List, s:Dict):
#     h.append(s)