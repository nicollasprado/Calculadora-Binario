from src.functions.binaryToDecimal import *
from src.functions.checkIfIsBinary import *
from src.functions.binaryToIntComplementTwo import convertBinaryToIntComplementTwo
from src.functions.binaryToSM import *
from src.functions.decimalToBinary import *
from src.functions.decimalToBinComplementTwo import convertDecimalToBinComplementTwo


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
        else:
                return (f'O valor {binaryNumber} não é binário!')
        

def decimalConversions(decimalNumber: int, optionChosen: int):
        # match optionChosen:
        #         case 1: return convertDecimalToBinary(decimalNumber)
        if (optionChosen == 1):
                return convertDecimalToBinary(decimalNumber)
        
def decimalToBinComplementTwo(decimalNumber: str, bitsQuantity: int):
        return convertDecimalToBinComplementTwo(decimalNumber, bitsQuantity)