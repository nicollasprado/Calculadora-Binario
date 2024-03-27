from functions.binaryToReal import *

def convertBinaryToSignMagnitude(binaryNumber: str):
    sign = ""
    if (binaryNumber[0] == "1"):
        sign = "-"
    else:
        sign = "+"

    binaryNumberWithoutFirstDigit = binaryNumber.replace(binaryNumber[0], "", 1)
    binaryNumberSM = convertBinaryToReal(binaryNumberWithoutFirstDigit[::-1])
    return (f"{sign}{binaryNumberSM}")