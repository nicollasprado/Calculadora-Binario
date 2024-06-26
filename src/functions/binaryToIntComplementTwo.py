from src.functions.binaryToDecimal import *
from src.functions.getComplementOne import *
from src.functions.sumOneInComplementOne import *


def convertBinaryToIntComplementTwo(binaryNumber: str):
    if (binaryNumber.startswith("0")):
        return (convertBinaryToDecimal(binaryNumber))
    else:
        complementOne = getComplementOne(binaryNumber)
        intValueOfComplementOne = convertBinaryToDecimal(complementOne)
        return sumOneInComplementOne(intValueOfComplementOne, True)