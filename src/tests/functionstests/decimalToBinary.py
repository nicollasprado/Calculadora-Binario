from functionstests.adjustToBitsQuantityChosen import *
from functionstests.checkIsRange import *

def convertDecimalToBinary(decNumber: str, bitsQuantity: int):
    binaryNumber = (bin(int(decNumber))[2:])
    checkRange, error = checkIsRange(decNumber, bitsQuantity, "DEC")
    if (checkRange != True):
        return error
    else:
        return adjustToBitsQuantityChosen(binaryNumber, bitsQuantity)