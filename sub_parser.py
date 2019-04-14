def read_args(args):
    try: 
        n, l, u = int(args[1]), int(args[2]), int(args[3])
    except:
        print("Error reading in the three arguments (NCards, LowerTarget, UpperTarget).")
    else: 
        return n, l, u
