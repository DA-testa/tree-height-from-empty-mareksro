# python3

import sys
import threading
import numpy as np

def compute_height(n, parents):
    # Write this function
    koks = np.empty((n,), dtype=object)
    for i in range (n):
        if parents [i] == -1:
            root = i
        else:
            if koks[parents[i]] is None:
                koks[parents[i]] = [i]
            else:
                koks[parents[i]].append(i)

    def height(node):
        if koks[node] is None:
            return 1
        heights = [height(berns) for berns in koks[node]]
        
        return max(heights) + 1
    
    return height(root)
    
    
def main():
    # implement input form keyboard and from files
    text=input("Ievadiet F vai I:\n")
    # text=()
    if "I" in text:
        n = input()
        parents = list(map(int, input().split()))
        print (compute_height(parents))
    elif "F" in text:
        fails = input()
        if "a" not in fails:
            with open("./test/" + fails, text ='r') as f:
                n = int(f.readLine().strip())
                parents = list(map(int, f.readLine().strip().split()))
    else:
        print("wrong command input")
        return
    print (compute_height(parents))




    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
