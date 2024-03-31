from functionstests.binaryToDecimal import *
from functionstests.getComplementOne import *
from functionstests.sumOneInComplementOne import *


def convertBinaryToIntComplementTwo(binaryNumber: str):
    if (binaryNumber.startswith("0")):
        return (convertBinaryToDecimal(binaryNumber))
    else:
        complementOne = getComplementOne(binaryNumber)
        intValueOfComplementOne = convertBinaryToDecimal(complementOne)
        return sumOneInComplementOne(intValueOfComplementOne, True)