from src.functions.binarieToReal import *
from src.functions.checkIfIsBinarie import *
from src.functions.binarieToIntComplementTwo import *


binarieNumber = input()
binarieNumberSplitted = list(binarieNumber)
reversedBinarieNumber = binarieNumber[::-1]

if (checkIfIsBinarie(binarieNumberSplitted) == True):

    print(convertBinarieToReal(reversedBinarieNumber))
                
    print(convertBinarieToIntComplementTwo(binarieNumber))

    #