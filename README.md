# blackjack_MDP_generalizer
Author: Michael J. Lukiman. Combines adversarial lookahead and Markov Decision Processes to formulate a game of blackjack where card values can range from 1 to a chosen N (instead of 1 to 10 (Jack)) and winning values can be a window of some numbers L to U (instead of just 21).

## How to use: 

### What it does:

  A with-replacement generalized game of blackjack with an inclusive winning-bracket instead of a single value. 
    
### To run:
    python bj.py <NCards> <LTarget> <UTarget> [--concise]

(--concise option will print out grid without details, as in Davis' specification.)
Python 3.7. No external packages required.

##### For any discrepancies email mll469@nyu.edu. Thank you for checking it out. 
