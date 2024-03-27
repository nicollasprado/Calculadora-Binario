from functions.binaryToReal import *
from functions.checkIfIsBinary import *
from functions.binaryToIntComplementTwo import *
from functions.binaryToSM import *


binaryNumber = input()
binaryNumberSplitted = list(binaryNumber)
reversedBinaryNumber = binaryNumber[::-1]

if (checkIfIsBinary(binaryNumberSplitted) == True):

    print("Real: ", convertBinaryToReal(reversedBinaryNumber))

    print("C'2: ", convertBinaryToIntComplementTwo(binaryNumber))

    print("S-M:", convertBinaryToSignMagnitude(binaryNumber))