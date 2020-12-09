import sys
import numpy as np
Ofile = open("input/input16.txt")##input file
n, k = Ofile.readline().strip().split() ##read data in 1 line
n, k = [int(n), int(k)]
S = Ofile.readline().strip().split()## read 2 line
for i in range(len(S)):
    S[i] = int(S[i])  ##retype str to int
Ofile.close()

'''
def maxsize(k, n, S):
    import itertools
    for i in range (n): ##find need lenght for answer
        plenties = itertools.combinations(S, n-i)##find all combo in S with lenght n
        for subsets in plenties:
            if all((a + b) % k for (a, b) in itertools.combinations(subsets, 2)):##check to all value in a pair met the requirements
                return n-i ## return lenght of massive S

        i = i+1

    return 0 ##if havn't answer when return 0

'''
mods = [0]*k
##O(n) из теории https://medium.com/@mrunankmistry52/non-divisible-subset-problem-comprehensive-explanation-c878a752f057

def maxsize (k,n,S):
    for x in S:
        mods[x % k] += 1
        '''
        total = min(1, mods[0])## может быть только 1 значение для 0 % k
        if (k % 2== 0): ##если k четное, то может быть только 1 значение для k/2 % k
            total += min(1, mods[k/2])
        for i in range (1, (k)//2): ## для остальных значений
            total += max(mods[i], mods[k-i])
       '''
        total = 0
        for i in range (k//2+1):
            if i == 0 or k == i*2: ## для значений 0 или если k четное
                total += bool(mods[i])
            else:## для остальных значений
                total += max([mods[i], mods[k-i]])
    return total


##print (maxsize(k, n, S))
Cfile = open("output/output16.txt","w")##output file
Cfile.write(str(maxsize(k, n, S))) ## writ in file result of function
Cfile.close()
