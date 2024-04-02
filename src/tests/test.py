from functionstests.binaryToDecimal import *
from functionstests.checkIfIsBinary import *
from functionstests.binaryToIntComplementTwo import *
from functionstests.binaryToSM import *
from functionstests.decimalToBinary import *
from functionstests.decimalToBinComplementTwo import *
from functionstests.decimalToBinSM import *


binaryNumber = input()
binaryNumberSplitted = list(binaryNumber)

if (checkIfIsBinary(binaryNumberSplitted) == True):

    print("Real: ", convertBinaryToDecimal(binaryNumber))

    print("C'2: ", convertBinaryToIntComplementTwo(binaryNumber))

    print("S-M:", convertBinaryToSignMagnitude(binaryNumber))


decimalNumber = input()
bitsQuantity = int(input())

print("D -> BIN", convertDecimalToBinary(decimalNumber, bitsQuantity))
print("D -> C'2", convertDecimalToBinComplementTwo(decimalNumber, bitsQuantity))
print("D -> S-M", convertDecimalToBinSM(decimalNumber, bitsQuantity))