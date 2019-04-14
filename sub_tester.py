# This file has unit tests and is also used in final shipment.

import sys
import sub_parser as p
import sub_probability as pr
import sub_decider as d
from typing import List

def test_read_args(args: List): 
    n,l,u,concise = p.read_args(args)
    if not concise: print("Have just read in NCards:",n, "| Lower Target:",l, "| Upper Target",u,"...")
    else: print("For input",n, l, u,)
    return n, l, u, concise

def test_compute_prob(x,y,ncards,l,u,prob):
    win = pr.computeProb(x,y,ncards,l,u,prob)
    print("Probability of winning after drawing given",x,y,"is",win)
    return win

def test_gen_arrs(n,l,u,c):
    probs, plays = d.generateArrays(n,l,u)
    p.printArrGrid(plays, 'play',c)
    p.printArrGrid(probs, 'prob',c)
    # p.printArr(probs)
    # p.printArr(plays)
    return probs, plays

if __name__ == "__main__":
    n, l, u = test_read_args(sys.argv)
    nlu = [n,l,u]
    probs = {}
    # test_gen_prob(l-1,l-1,*nlu,probs)
    probs, plays = test_gen_arrs(*nlu)
