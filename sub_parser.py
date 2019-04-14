def read_args(args):
    try: 
        n, l, u = int(args[1]), int(args[2]), int(args[3])
    except:
        print("Error reading in the three arguments (NCards, LowerTarget, UpperTarget).")
    else: 
        return n, l, u

def printArr(probs, pre="p(draw"):
    for i, xt in enumerate(probs):
        xtVal = probs[xt]
        for j, yt in enumerate(xtVal):
            print("{pre}|[{xt},{yt}]) = {p} ".format(pre=pre,xt=xt, yt=yt, p=xtVal[yt]))
