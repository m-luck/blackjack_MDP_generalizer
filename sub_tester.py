import sys
import sub_parser as p
import sub_probability as pr
from typing import List

def test_read_args(args: List): 
    n,l,u = p.read_args(args)
    print("Just read in",n, l, u)
    return n, l, u

def test_joint_of(events: List):
    prob = pr.joint_of(events)
    print("Joint of", *events, "is",prob)
    return prob

def test_gen_prob(x,y,ncards,l,u,prob):
    win = pr.generateProb(x,y,ncards,l,u,prob)
    print("Probability of winning given",x,y,"is",win)
    return win

def test_gen_prob_arr(ncards,l,u):
    prob = pr.generateProbArray(ncards,l,u)

if __name__ == "__main__":
    n, l, u = test_read_args(sys.argv)
    nlu = [n,l,u]
    assert test_joint_of([1,2,3]) == 6
    prob = {}
    assert test_gen_prob(5,5,1,2,2,prob) == 1.0
    prob = test_gen_prob_arr(*nlu)
