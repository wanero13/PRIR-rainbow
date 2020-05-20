import hashlib
import mpi4py
import sys
from supp import Hasher


#UWAGA STALE HASLO
hasher = Hasher()
availableTreads = [2,4,8,16,32]
# Sprawdzenie i przypisanie wartosci parametrow do zmiennych
if len(sys.argv)>1:
    if len(sys.argv)==5:
        threadNumber = int(sys.argv[1])
        passLen = int(sys.argv[2])
        chainLen = int(sys.argv[3])
        chainNumber = int(sys.argv[4])
    else:
        print('Program must have 0 or 4 parameters')
else:
    threadNumber = 4
    passLen = 5
    chainLen = 1000
    chainNumber = 1000

initPassArr = []

for i in range(chainNumber):
    initPassArr.append(hasher.randomPass(passLen))

print(initPassArr)

