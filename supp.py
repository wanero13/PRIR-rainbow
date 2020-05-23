import random
import string
import hashlib
from Crypto.Cipher import DES
from Crypto import Random
import codecs
import base64


class Hasher():
    def __init__(self):
        self.BASE62 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = Random.get_random_bytes(8)

    def randomPass(self, passLen: int) -> str:
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join((random.choice(lettersAndDigits) for i in range(passLen)))

    def basicReduction(self, hashedPass: str, passLen: int):
        return hashedPass[0:passLen]

    def bluntHashPass(self, passwd: str, passLen: int) -> tuple:
        lack = 8 - len(passwd) % 8
        passwd = passwd + lack * '0'
        cipher = DES.new(self.key, DES.MODE_ECB)
        hashedPass = cipher.encrypt(passwd.encode())
        hashedPass = hashlib.sha3_512(hashedPass).hexdigest()
        hashedPass = codecs.encode(codecs.decode(hashedPass, 'hex'), 'base64').decode()
        hashedPass = list(hashedPass)
        for i in range(len(hashedPass)):
            if hashedPass[i] == '\n':
                hashedPass[i] = '0'
            if hashedPass[i] == '=':
                hashedPass[i] = '1'
            if hashedPass[i] == '/':
                hashedPass[i] = '2'

        hashedPass = ''.join(hashedPass)
        newPass = self.basicReduction(hashedPass, passLen)
        return hashedPass, newPass


def validateIfNumbers(threadNumber: str, passLen: str, chainLen: str, chainNumber: str):
    if not threadNumber.isnumeric():
        print("Wrong input in number of threads. (1st parameter)")
        return False
    if not passLen.isnumeric():
        print("Wrong input in password length. (2nd parameter)")
        return False
    if not chainLen.isnumeric():
        print("Wrong input in chain length. (3rd parameter)")
        return False
    if not chainNumber.isnumeric():
        print("Wrong input in number of chains. (4th parameter)")
        return False
    return True


def validateInputValues(threadNumber: int, passLen: int, chainLen: int, chainNumber: int, availableThreads):
    if threadNumber not in availableThreads:
        print("Wrong number of threads. (Only available: 2,4,8,16,32")
        return False
    if not 3 <= passLen <= 15:
        print("Wrong password length. (3-15)")
        return False
    if not 10 <= chainLen <= 10000:
        print("Wrong chain length. (10-10000)")
        return False
    if not 1 <= chainNumber <=10000:
        print("Wrong number of chains")
        return False
    return True
