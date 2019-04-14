def read_args(args):
    try: 
        n, l, u = int(args[1]), int(args[2]), int(args[3])
    except:
        print("Error reading in the three arguments (NCards, LowerTarget, UpperTarget).")
    else: 
        return n, l, u

def printArr(arr, pre="p(draw"):
    for i, xt in enumerate(arr):
        xtVal = arr[xt]
        for j, yt in enumerate(xtVal):
            print("{pre}|[{xt},{yt}]) = {p} ".format(pre=pre,xt=xt, yt=yt, p=xtVal[yt]))

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def printArrGrid(arr, pre="p(draw"):
    for i, xt in enumerate(arr):
        xtVal = arr[xt]
        row = ""
        if is_float(xtVal[1]):
            for j, yt in enumerate(xtVal):
                row += "{p:.4f}\t".format(p=float(xtVal[yt]))
        else: 
            for j, yt in enumerate(xtVal):
                row += "{p}\t".format(p=xtVal[yt])
        print(row)