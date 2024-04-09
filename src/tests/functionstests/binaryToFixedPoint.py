from functionstests.binaryToDecimal import *
from functionstests.binaryToDecimalFractional import *
from functionstests.checkDotsQuantity import *

def convertBinaryToFixedPoint(binaryNumberRaw: str):
    if (checkDotsQuantity(binaryNumberRaw) == True):
        sign = False
        if (binaryNumberRaw.startswith("1")):
            sign = True

        binaryNumber = binaryNumberRaw[1:]
        dotIndex = binaryNumber.index(".")
        intPart = binaryNumber[0:dotIndex]
        fractionalPart = binaryNumber[(dotIndex+1):len(binaryNumber)]
        intPartDecimal = convertBinaryToDecimal(intPart)
        fractionalPartDecimal = convertBinaryToDecimalFractional(fractionalPart)

        decimalFixedPoint = intPartDecimal + fractionalPartDecimal
        if (sign == True):
            return decimalFixedPoint * -1
        else:
            return decimalFixedPoint
    else:
        return "Erro na sinalização do ponto, coloque apenas um ponto!"