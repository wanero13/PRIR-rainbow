import hashlib
from mpi4py import MPI
import sys
from supp import Hasher
from validator import Validator

hasher = Hasher()
validator = Validator()

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

if rank == 0:
    if len(sys.argv) > 1:
        if len(sys.argv) == 4 and validator.validateParams(size, sys.argv[1], sys.argv[2], sys.argv[3]):
            passLen = int(sys.argv[2])
            chainLen = int(sys.argv[3])
            chainNumber = int(sys.argv[4])
        else:
            print('Program must have 0 or 4 parameters in certain value range')
            sys.exit()
    else:
        threadNumber = 4
        passLen = 5
        chainLen = 1000
        chainNumber = 1000
    inputValuesToSend = [passLen, chainLen, chainNumber]
    for i in range(1, size):
        comm.send(inputValuesToSend, dest=i)
else:
    inputToRecv = comm.recv(source=0)
    passLen = inputToRecv[0]
    chainLen = inputToRecv[1]
    chainNumber = inputToRecv[2]

chainsToDo = int(chainNumber / size)
generatedPasswords = []
for i in range(1, chainsToDo):
    generatedPasswords.append(hasher.randomPass(passLen))

print(generatedPasswords)

for i in range(0, chainsToDo - 1):
    chainStart = generatedPasswords[i]
    currentPasswordProcessed = chainStart
    for j in range(1, chainLen - 1):
        _, currentPasswordProcessed = hasher.bluntHashPass(currentPasswordProcessed, passLen)
    chainEnd = hasher.hashPassDes(currentPasswordProcessed)
    print(chainStart)
    print(chainEnd)
    # Tu zapisik do pliku danego łańcucha
