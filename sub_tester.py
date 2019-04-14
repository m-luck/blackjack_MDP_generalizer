import sys
import sub_parser as p
import sub_probability as pr
import sub_decider as d
from typing import List

def test_read_args(args: List): 
    n,l,u = p.read_args(args)
    print("Just read in",n, l, u)
    return n, l, u

def test_gen_prob(x,y,ncards,l,u,prob):
    win = pr.generateProb(x,y,ncards,l,u,prob)
    print("Probability of winning after drawing given",x,y,"is",win)
    return win

def test_gen_prob_arr(ncards,l,u):
    probs = pr.generateProbArray(ncards,l,u)
    p.printArr(probs)
    return probs

def test_gen_play_arr(probs):
    plays = d.generatePlayArray(probs)
    p.printArr(plays, pre="Choice")
    return plays

if __name__ == "__main__":
    n, l, u = test_read_args(sys.argv)
    nlu = [n,l,u]
    # assert test_joint_of([1,2,3]) == 6
    probs = {}
    # test_gen_prob(l-1,l-1,*nlu,probs)
    probs = test_gen_prob_arr(*nlu)
    plays = test_gen_play_arr(probs)
