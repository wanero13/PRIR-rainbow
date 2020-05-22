class Validator():
    def __init__(self):
        self.threadRange = [2, 4, 8, 16, 32]
        pass

    def validateParams(self, threadNumber, passLen, chainLen, chainNumber):
        try:
            threadNumber = int(threadNumber)
            passLen = int(passLen)
            chainLen = int(chainLen)
            chainNumber = int(chainNumber)
        except:
            return False
        if not threadNumber in self.threadRange:
            return False
        if not 2 < passLen < 16:
            return False
        if not 9 < chainLen < 10001:
            return False
        if not 0 < chainNumber < 10001:
            return False
        return True
