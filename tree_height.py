# python3

import sys
import threading
import numpy as np



def compute_height(n, parents):
    # Write this function
    koks = np.empty((n,), dtype=object)
    root=-1
    for i in range (len(parents)):
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
    #text=input("Enter I or F:\n")
    text=input()
    if "I" in text:
        count = int(input())
        vert = input()
        vert = np.array(list(map(int, vert.split())))
        #print (compute_height(n, parents))
    if "F" in text:
        fails = input()
        if "a" in fails:
            print("wrong file name")
            return
        
        with open("./test/" + fails,'r') as f:
                count = int(f.readline().strip())
                vert = f.readline()
                vert= np.array(list(map(int, vert.split())))
                #print (compute_height(n, parents))
    #else:
           # print("wrong input type")
           # return
    
    print (compute_height(count, vert))

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
