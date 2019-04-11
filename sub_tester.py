import sys
import sub_parser as p
from typing import List

def test_read_args(args: List): 
    n,l,u = p.read_args(args)
    print(n, l, u)

if __name__ == "__main__":
    n, l, u = test_read_args(sys.argv)