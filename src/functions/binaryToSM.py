from src.functions.binaryToDecimal import *

def convertBinaryToSignMagnitude(binaryNumber: str):
    sign = ""
    if (binaryNumber[0] == "1"):
        sign = "-"
    else:
        sign = "+"

    binaryNumberWithoutFirstDigit = binaryNumber.replace(binaryNumber[0], "", 1)
    binaryNumberSM = convertBinaryToDecimal(binaryNumberWithoutFirstDigit[::-1])
    return (f"{sign}{binaryNumberSM}")