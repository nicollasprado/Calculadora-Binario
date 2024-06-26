from src.functions.checkIfIsBinary import *
from src.functions.binaryToDecimal import *
from src.functions.binaryToIntComplementTwo import *
from src.functions.binaryToSM import *
from src.functions.binaryFixedPointFractionalDecimal import *
from src.functions.decimalToBinary import *
from src.functions.decimalToBinComplementTwo import *
from src.functions.decimalToBinSM import *


def binaryConversions(binaryNumber: str, optionChosen: int):
        binaryNumberSplitted = list(binaryNumber)

        if (checkIfIsBinary(binaryNumberSplitted) == True):
                # match optionChosen:
                #         case 1: return str(convertBinaryToDecimal(binaryNumber))
                #         case 2: return convertBinaryToSignMagnitude(binaryNumber)
                #         case 3: return convertBinaryToIntComplementTwo(binaryNumber)
                if (optionChosen == 1):
                        return str(convertBinaryToDecimal(binaryNumber))
                elif (optionChosen == 2):
                        return convertBinaryToSignMagnitude(binaryNumber)   
                elif (optionChosen == 3):
                        return convertBinaryToIntComplementTwo(binaryNumber)     
                elif (optionChosen == 4):
                        return convertBinaryFixedPointToFractionalDecimal(binaryNumber)              
        else:
                return (f'O valor {binaryNumber} não é binário!')
        

def decimalConversions(decimalNumber: str, optionChosen: int, bitsQuantity: int):
        # match optionChosen:
        #         case 1: return convertDecimalToBinary(decimalNumber)
        if (optionChosen == 1):
                return convertDecimalToBinary(decimalNumber, bitsQuantity)
        elif (optionChosen == 2):
                return convertDecimalToBinComplementTwo(decimalNumber, bitsQuantity)
        elif (optionChosen == 3):
                return convertDecimalToBinSM(decimalNumber, bitsQuantity)