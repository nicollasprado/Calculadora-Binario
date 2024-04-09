from functionstests.checkDotsQuantity import *
from functionstests.decimalToBinary import *


def convertFractionalDecimalToFixedPointBinary(fractionalDecimalNumber: str, model: str):
    if (checkDotsQuantity(fractionalDecimalNumber) == 1):
        sign = False
        if (fractionalDecimalNumber.startswith("-")):
            sign = True
            fractionalDecimalNumber = fractionalDecimalNumber[1:]

        dotIndex = fractionalDecimalNumber.index(".")
        intPart = fractionalDecimalNumber[0:dotIndex]
        fractionalPart = fractionalDecimalNumber[(dotIndex + 1):len(fractionalDecimalNumber)]

        intPartBinary = convertDecimalToBinary(intPart, model.count("I"))
        fractionalPartBinary = convertDecimalToBinary(fractionalPart, model.count("F")) # working

        if (sign == True):
            return f"1{intPartBinary}{fractionalPartBinary}"
        else:
            return f"0{intPartBinary}{fractionalPartBinary}"
    else:
        return "Erro na sinalização do ponto, coloque apenas um ponto!"