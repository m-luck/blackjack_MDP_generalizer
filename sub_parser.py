def read_args(args):
    try: 
        n, l, u = args[1], args[2], args[3]
    except:
        print("Error reading in the three arguments (NCards, LowerTarget, UpperTarget).")
    else: 
        return n, l, u
