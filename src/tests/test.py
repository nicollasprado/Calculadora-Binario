from functionstests.binaryToDecimal import *
from functionstests.checkIfIsBinary import *
from functionstests.binaryToIntComplementTwo import *
from functionstests.binaryToSM import *
from functionstests.decimalToBinary import *
from functionstests.decimalToBinComplementTwo import *


binaryNumber = input()
binaryNumberSplitted = list(binaryNumber)

if (checkIfIsBinary(binaryNumberSplitted) == True):

    print("Real: ", convertBinaryToDecimal(binaryNumber))

    print("C'2: ", convertBinaryToIntComplementTwo(binaryNumber))

    print("S-M:", convertBinaryToSignMagnitude(binaryNumber))


decimalNumber = input()
bitsQuantity = int(input())


if(decimalNumber.startswith("-")):
    decimalNumberAbsolute = int(decimalNumber) * -1
else:
    decimalNumberAbsolute = int(decimalNumber)
print(convertDecimalToBinary(decimalNumberAbsolute))

print("D -> C'2", convertDecimalToBinComplementTwo(decimalNumber, bitsQuantity))