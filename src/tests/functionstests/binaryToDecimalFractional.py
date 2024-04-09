def convertBinaryToDecimalFractional(binaryNumber: str):
    binaryNumberSplitted = list(map(int, binaryNumber))
    numSum = 0
    baseExpoent = -1
    for num in binaryNumberSplitted:
        numSum += (num * (2 ** baseExpoent))
        baseExpoent -= 1
    return numSum