import random
import string
import binascii
from Crypto.Cipher import DES
from Crypto import Random


class Hasher():
    def __init__(self):
        self.marks = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't',
                      'u', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O', 'P', 'R', 'S', 'T', 'U', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8',
                      '9']
        self.key = Random.get_random_bytes(8)

    def randomPass(self, passLen: int) -> str:
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join((random.choice(lettersAndDigits) for i in range(passLen)))

    def basicReduction(self, hash: str, passLen: int):
        return None

    def hashPass(self, passwd: str, passLen: int) -> tuple:
        return None
