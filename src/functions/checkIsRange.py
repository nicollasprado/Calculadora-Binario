def checkIsRange(decimalNumber: str, bitsQuantity: int, numType: str):
    if (numType == "CTWO"):
        positiveRange = (2 ** (bitsQuantity - 1)) - 1
        negativeRange = (2 ** (bitsQuantity - 1)) * -1
        if int(decimalNumber) in range(positiveRange, (negativeRange + 1), -1):
            return True, ""
        else:
            return False, (f"O número {decimalNumber} não pode ser representado em complemento de dois com {bitsQuantity} bits!")
    elif (numType == "SM"):
        positiveRange = (2 ** (bitsQuantity - 1)) - 1
        negativeRange = ((2 ** (bitsQuantity - 1)) -1) * -1
        if int(decimalNumber) in range(positiveRange, (negativeRange), -1):
            return True, ""
        else:
            return False, (f"O número {decimalNumber} não pode ser representado em sinal magnitude com {bitsQuantity} bits!")
    elif (numType == "DEC"):
        maxNumber = (2 ** bitsQuantity) - 1
        if int(decimalNumber) in range(0, (maxNumber)):
            return True, ""
        else:
            return False, (f"O número {decimalNumber} não pode ser representado em binário com {bitsQuantity} bits!")