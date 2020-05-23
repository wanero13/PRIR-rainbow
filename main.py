import hashlib
import mpi4py
import sys
from supp import Hasher
from supp import validateIfNumbers, validateInputValues

# UWAGA STALE HASLO
hasher = Hasher()
availableThreads = [2, 4, 8, 16, 32]
# Sprawdzenie i przypisanie wartosci parametrow do zmiennych
if len(sys.argv) > 1:
    if not validateIfNumbers(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]):
        sys.exit("Wrong input")
    if len(sys.argv) == 5:
        threadNumber = int(sys.argv[1])
        passLen = int(sys.argv[2])
        chainLen = int(sys.argv[3])
        chainNumber = int(sys.argv[4])
        if not validateInputValues(threadNumber, passLen, chainLen, chainNumber, availableThreads):
            sys.exit("Wrong input")
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
print(hasher.bluntHashPass(initPassArr[0], passLen))
