# This file has functions related to probability.

import random 
import sub_parser as p
from typing import Dict, List

def generateProb(me:int,other:int,ncards:int,l:int,u:int,prob:Dict):
    my_winning_prob = 0.0
    other_winning_prob = 0.0 # Note: this value is case-wise, while my_winning_prob monotonically increases in aggregate.
    for n in range(ncards,0,-1): # Draw a card.  
        if me+n > u:  # We drew too high, so we lost and the other won.
            other_winning_prob = 1.0
        elif me+n >= l: # We didn't draw too high and we also drew above the winning threshold, so we certainly won, and the other certainly lost.
            other_winning_prob = 0
        else: # We are still below the winning threshold, so the probability of the other winning is what is in the table from other perspective. 
            other_winning_prob = prob[other][me+n]; 
        my_winning_prob += (1.0-other_winning_prob)/ncards # Add this chance. This is because there is a 1/ncards chance of the card being drawn. 
    # After we add all these possibilities up, we can return the final chance of us winning.
    return my_winning_prob 

def generateProbArray(ncards:int,l:int,u:int):
    '''
    This populates the probability array for every permutation of score.
    Because they rely on each other, it starts from near endgame and generates in a staircase, symmetric manner until the whole array is fulfilled.
    '''
    prob_arr = {}
    for xt in range(l-1,0,-1):
        prob_arr[xt] = {}
        for yt in range(l-1,xt-1,-1):
            prob = generateProb(xt,yt,ncards,l,u,prob_arr)
            prob_arr[xt][yt] = prob
            prob = generateProb(yt,xt,ncards,l,u,prob_arr)
            prob_arr[yt][xt] = prob
    return prob_arr

