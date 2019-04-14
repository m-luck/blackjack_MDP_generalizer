import sub_tester as t
import sys
'''
What it does:
    A with-replacement generalized game of blackjack with an inclusive winning-bracket instead of a single value. 
    
To run:
    python bj.py <NCards> <LTarget> <UTarget> [--concise]

(--concise option will print out details of the grid.)
'''
n, l, u, c = t.test_read_args(sys.argv) # Reads in terminal input.
probs, plays = t.test_gen_arrs(n,l,u,c) # Generates arrays and prints them.