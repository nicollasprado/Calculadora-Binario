from functionstests.decimalToBinary import *
from functionstests.binaryToDecimal import *
from functionstests.getComplementOne import *
from functionstests.sumOneInComplementOne import *
from functionstests.adjustToBitsQuantityChosen import *
from functionstests.checkIsRange import *




def convertDecimalToBinComplementTwo(decimalNumber: str, bitsQuantity: int):
    rangeCheck, answer = checkIsRange(decimalNumber, bitsQuantity, "CTWO")
    if (rangeCheck != True):
        return answer
    else:
        sign = False
        if (decimalNumber.startswith("-")):
            sign = True
            decimalNumber = decimalNumber[1:]
    
        binaryNumber = convertDecimalToBinary(decimalNumber, bitsQuantity)

        complementOneBinary = getComplementOne(binaryNumber)
        complementOneDecimal = convertBinaryToDecimal(complementOneBinary)

        complementTwoDecimal = sumOneInComplementOne(complementOneDecimal, False)

        result = convertDecimalToBinary(complementTwoDecimal, bitsQuantity)

        if (sign != True):
            complementOneSignedBinary = getComplementOne(result)
            complementOneSignedDecimal = convertBinaryToDecimal(complementOneSignedBinary)

            # In these functions we're working with an non signed number, so sign will be send as false
            complementTwoSignedDecimal = sumOneInComplementOne(complementOneSignedDecimal, False)
            return convertDecimalToBinary(complementTwoSignedDecimal, bitsQuantity)
        else:
            return result