def convertBinarieToReal(binarieReversed: str):
    try:
        expoent = 0
        realNumberSum = 0
        for digit in binarieReversed:
            equivalentRealNumber = int(digit) * (2 ** expoent)
            realNumberSum += equivalentRealNumber
            expoent += 1
        return str(realNumberSum)
    except:
        raise Exception("Um Erro Aconteceu, por favor contate os criadores")   