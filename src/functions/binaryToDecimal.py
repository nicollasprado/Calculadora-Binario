def convertBinaryToDecimal(binaryReversed: str):
    try:
        expoent = 0
        decimalNumberSum = 0
        for digit in binaryReversed:
            equivalentDecimalNumber = int(digit) * (2 ** expoent)
            decimalNumberSum += equivalentDecimalNumber
            expoent += 1
        return decimalNumberSum
    except:
        raise Exception("Um Erro Aconteceu, por favor contate os criadores")   