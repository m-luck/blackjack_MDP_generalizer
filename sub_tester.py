import sys
import sub_parser as p
import sub_probability as pr
from typing import List

def test_read_args(args: List): 
    n,l,u = p.read_args(args)
    print(n, l, u)
    return n, l, u

def test_joint_of(events: List):
    prob = pr.joint_of(events)
    print(prob)

if __name__ == "__main__":
    n, l, u = test_read_args(sys.argv)
    test_joint_of([1,2,3])
