from src.functions.binaryToReal import *
from src.functions.checkIfIsBinary import *
from src.functions.binaryToIntComplementTwo import *


def binaryConversions(binaryNumber: str):
        binaryNumberSplitted = list(binaryNumber)
        reversedBinaryNumber = binaryNumber[::-1]

        if (checkIfIsBinary(binaryNumberSplitted) == True):

                return convertBinaryToReal(reversedBinaryNumber)