# This file has functions related to high level player-decision heuristics and the game simulation.

import sub_probability as pr
from typing import Dict, List

def other(p:int):
    '''
    Returns the opposite player. 
    0 -> 1
    1-> 0
    '''
    return abs(p-1) # Player is 0 or 1 so this operation returns choice of 1 or 0 (other player)

def otherChoice(p:int,h:List):
    '''
    Returns the decision of the previous player.
    '''
    mostRecent = h[-1]
    choice = mostRecent['choice'][other(p)]
    return choice

def shouldDraw(p:int,h:List,probs:Dict):
    '''
    Dictates if current player should rationally draw, based on the previous player's decision and both player's scores.
    '''
    state = h[-1]
    my_score = state['val'][p]
    other_score = state['val'][other(p)]
    # If the current player has a score that is less than the other, and the other player has just passed, 
    # the current player is forced into a position to draw, since the rules say two passes in a row grant the victory to the highest score.
    if my_score < other_score and otherChoice(p,h) == 'passed':
        return True
    elif probs[my_score][other_score] > probs[other_score][my_score]: # If there is greater chance of winning by drawing (rather than forcing the other into drawing), then draw!
        return True 
    return False

def generatePlayArray(probs:Dict):
    play_arr = {}
    for i, xt in enumerate(probs):
        play_arr[xt] = {}
        xtVal = probs[xt]
        for j, yt in enumerate(probs[xt]):
            ytVal = xtVal[yt]
            artifical_history = [{
                'val': { 0: xt, 1: yt },
                'choice': {0: 'draw', 1: 'draw'}
                }]
            play_arr[xt][yt] = 'Play' if shouldDraw(0,artifical_history,probs) else 'Pass'
    return play_arr


def nextTurnIs(h:List):
    '''
    Returns the player ID of whose turn is next.
    '''
    state = h[-1]
    return other(state['turn'])

def game_march(p:int,h:List):
    '''
    This will move the game forward by one time step with optimal players. 
    Optimal move is determined by a game history state consisting of three parts:
    Whether or not the player Y has just passed, X’s total points, and Y’s total points. '''
    state = h[-1].copy()
    state['turn'] = nextTurnIs(state)
    score = state['val'][p]
    if state['choice'] == 'draw':
        newP = val + pr.draw()
    state['val'][p] = newP

def addHistory(h:List, s:Dict):
    h.append(s)