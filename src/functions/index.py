from src.functions.binarieToReal import *
from src.functions.checkIfIsBinarie import *
from src.functions.binarieToIntComplementTwo import *


def binarieConversions(binarieNumber: str):
        binarieNumberSplitted = list(binarieNumber)
        reversedBinarieNumber = binarieNumber[::-1]

        if (checkIfIsBinarie(binarieNumberSplitted) == True):

                return convertBinarieToReal(reversedBinarieNumber)