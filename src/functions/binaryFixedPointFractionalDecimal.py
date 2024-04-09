from src.functions.binaryToDecimal import *
from src.functions.binaryToDecimalFractional import *
from src.functions.checkDotsQuantity import *

def convertBinaryFixedPointToFractionalDecimal(binaryNumberRaw: str):
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

        model = "S"
        for each in range(0, len(intPart)):
            model += "I"
        for each in range(0, len(fractionalPart)):
            model += "F"

        decimalFixedPoint = intPartDecimal + fractionalPartDecimal
        if (sign == True):
            return decimalFixedPoint * -1, model
        else:
            return decimalFixedPoint, model
    else:
        return "Erro na sinalização do ponto, coloque apenas um ponto!"