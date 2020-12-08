import sys
import numpy as np
Ofile = open("input/input16.txt")##input file
n, k = Ofile.readline().strip().split() ##read data in 1 line
n, k = [int(n), int(k)]
S = Ofile.readline().strip().split()## read 2 line
for i in range (len(S)):
    S[i]=int(S[i])  ##retype str to int
Ofile.close()


def maxsize(k, n, S):
    import itertools
    for i in range (n): ##find need lenght for answer
        plenties = itertools.combinations(S, n-i)##find all plenties in S with lenght n
        for subsets in plenties:
            if all((a + b) % k for (a, b) in itertools.combinations(subsets, 2)):##check to all subsets value in a pair met the requirements
                return n-i ## return lenght of massive S

        i = i+1

    return 0 ##if haven't answer when return 0


Cfile = open("output/output16.txt","w")##output file
Cfile.write(str(maxsize(k, n, S))) ## writ in file result of function
Cfile.close()
