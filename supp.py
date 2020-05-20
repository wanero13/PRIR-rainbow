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
