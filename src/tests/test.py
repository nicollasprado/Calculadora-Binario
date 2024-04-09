from functionstests.binaryToDecimal import *
from functionstests.checkIfIsBinary import *
from functionstests.binaryToIntComplementTwo import *
from functionstests.binaryToSM import *
from functionstests.decimalToBinary import *
from functionstests.decimalToBinComplementTwo import *
from functionstests.decimalToBinSM import *
from functionstests.binaryToFixedPoint import *
from functionstests.fractionalDecimalToFixedPointBinary import *


binaryNumber = input("Digite um número binário\n")
binaryNumberSplitted = list(binaryNumber)

if (checkIfIsBinary(binaryNumberSplitted) == True):

    print("Real: ", convertBinaryToDecimal(binaryNumber))

    print("C'2: ", convertBinaryToIntComplementTwo(binaryNumber))

    print("S-M:", convertBinaryToSignMagnitude(binaryNumber))


decimalNumber = input("\nDigite um número decimal\n")
bitsQuantity = int(input("Digite a quantidade de bits\n"))

print("D -> BIN", convertDecimalToBinary(decimalNumber, bitsQuantity))
print("D -> C'2", convertDecimalToBinComplementTwo(decimalNumber, bitsQuantity))
print("D -> S-M", convertDecimalToBinSM(decimalNumber, bitsQuantity))

fractionalBinaryNumber = input("Digite um número binário no modelo: SinalPARTE INTEIRA.PARTE FRACIONARIA\n")
print("BIN -> Fixed Point", convertBinaryToFixedPoint(fractionalBinaryNumber))

# THIS FUNCTION BELOW ISNT COMPLETE ACTUALLY
# fractionalDecimalNumber = input("\nDigite um número decimal fracionário\n")
# model = input("Digite o modelo do ponto fixo, exemplo: siiff\n").upper()
# print("Fractional DEC -> Fixed Point BIN", convertFractionalDecimalToFixedPointBinary(fractionalDecimalNumber, model))