from functionstests.decimalToBinary import *
from functionstests.adjustToBitsQuantityChosen import *
from functionstests.checkIsRange import *


def convertDecimalToBinSM(decimalNumber: str, bitsQuantity: int):
    rangeCheck, error = checkIsRange(decimalNumber, bitsQuantity, "SM")
    if (rangeCheck != True):
        return error
    else:
        sign = False        
        if (decimalNumber.startswith("-")):
            sign = True
            decimalNumber = decimalNumber[1:]
        binaryNumber = convertDecimalToBinary(decimalNumber, bitsQuantity)
        if (sign):
            return binaryNumber.replace(binaryNumber[0], "1", 1)
        else:
            return binaryNumber