from functionstests.decimalToBinary import *
from functionstests.binaryToDecimal import *
from functionstests.getComplementOne import *
from functionstests.sumOneInComplementOne import *



def adjustToBitsQuantityChosen(binaryNumber: str, bitsQuantity):
    bitsToAdd = ""
    for quantity in range(0, (bitsQuantity - len(binaryNumber))):
        bitsToAdd += "0"
    return (bitsToAdd + binaryNumber)


def checkIsRange(decimalNumber: int, bitsQuantity: int):
    positiveRange = ((2 ** bitsQuantity) // 2) - 1
    negativeRange = ((2 ** bitsQuantity) // 2) * -1
    if decimalNumber in range(positiveRange, (negativeRange + 1), -1):
        return True, ""
    else:
        return False, (f"O número {decimalNumber} não pode ser representado em complemento de dois com {bitsQuantity} bits!")


def convertDecimalToBinComplementTwo(decimalNumber: str, bitsQuantity: int):
    if (bitsQuantity == None):
        bitsQuantity = 4
    elif (bitsQuantity < 4):
        return ("O valor minimo de bits é 4")
    
    rangeCheck, answer = checkIsRange(int(decimalNumber), bitsQuantity)
    if (rangeCheck != True):
        return answer
    else:
        sign = False
        if (decimalNumber.startswith("-")):
            sign = True
            decimalNumber = decimalNumber[1:]
    
        binaryNumber = convertDecimalToBinary(int(decimalNumber))
        binaryNumberAdjusted = adjustToBitsQuantityChosen(binaryNumber, bitsQuantity)

        complementOneBinary = getComplementOne(binaryNumberAdjusted)
        complementOneDecimal = convertBinaryToDecimal(complementOneBinary)

        complementTwoDecimal = sumOneInComplementOne(complementOneDecimal, False)

        result = convertDecimalToBinary(complementTwoDecimal)

        if (sign):
            complementOneSignedBinary = getComplementOne(result)
            complementOneSignedDecimal = convertBinaryToDecimal(complementOneSignedBinary)

            # In these functions we're working with an non signed number, so sign will be send as false
            complementTwoSignedDecimal = sumOneInComplementOne(complementOneSignedDecimal, False)
            complementTwoSignedBinary = convertDecimalToBinary(complementTwoSignedDecimal)

            return adjustToBitsQuantityChosen(complementTwoSignedBinary, bitsQuantity)
        else:
            return result