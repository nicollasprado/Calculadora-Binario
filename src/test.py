# from functions.binaryToDecimal import *
# from functions.checkIfIsBinary import *
# from functions.binaryToIntComplementTwo import *
# from functions.binaryToSM import *
from functions.decimalToBinary import *


# binaryNumber = input()
# binaryNumberSplitted = list(binaryNumber)
# reversedBinaryNumber = binaryNumber[::-1]

# if (checkIfIsBinary(binaryNumberSplitted) == True):

#     print("Real: ", convertBinaryToDecimal(reversedBinaryNumber))

#     print("C'2: ", convertBinaryToIntComplementTwo(binaryNumber))

#     print("S-M:", convertBinaryToSignMagnitude(binaryNumber))

intNumber = int(input())
print(convertDecimalToBinary(intNumber))