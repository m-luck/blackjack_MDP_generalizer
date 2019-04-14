def read_args(args):
    try: 
        n, l, u = int(args[1]), int(args[2]), int(args[3])
    except:
        print("Error reading in the three arguments (NCards, LowerTarget, UpperTarget).")
    else: 
        concise = False
        if len(args) > 4:
            if args[4] == "--concise":
                concise = True
        return n, l, u, concise

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

def printArrGrid(arr,contentType:str,concise:bool):
    sortedArr = sorted(arr)
    title = "\nPlay" if contentType=='play' else "\nProb"
    print(title)
    if not concise:
        header = "  "
        for xt in sortedArr:
            header += str(xt) + "        "
        header += " X"
        print(header)
    for xt in sortedArr:
        xtVal = arr[xt]
        sortedXtval = sorted(arr[xt])
        if not concise: row = str(xt) + " "
        else: row = "\t"
        if is_float(xtVal[1]):
            for yt in sortedXtval:
                row += "{p:.4f}   ".format(p=float(xtVal[yt]))
        else: 
            if not concise:
                for yt in sortedXtval:
                    row += "{p}     ".format(p=xtVal[yt])
            else:
                for yt in sortedXtval:
                    shortp = ''
                    if xtVal[yt] == 'Draw': shortp = 'D'
                    else: shortp = 'P'
                    row += "{shortp} ".format(shortp=shortp)
        print(row)
    if not concise: print("Y")