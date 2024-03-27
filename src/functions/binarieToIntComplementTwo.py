from src.functions.binarieToReal import convertBinarieToReal


def getComplementOne(binarieNumber: str):
    complementOne = binarieNumber.replace("0", "temporary")
    complementOne = complementOne.replace("1", "0")
    complementOne = complementOne.replace("temporary", "1")
    return complementOne

def checkComplementOneSuccessor(reversedComplementOne: str, nextDigitIndex):
    if (reversedComplementOne[nextDigitIndex] == "1"):
        return True

def sumOneInComplementOne(complementOne: str):
    if (complementOne.endswith("1")):
        bitesQuantity = len(complementOne)
        reversedComplementOne = complementOne[::-1]

        nextDigitIndex = 1
        for digit in reversedComplementOne:
            if (nextDigitIndex <= (bitesQuantity - 1)):
                # 0111
                # 1110
                # 1
                # 0001
                if (checkComplementOneSuccessor(reversedComplementOne, nextDigitIndex) == True):
                    reversedComplementOne = reversedComplementOne.replace(digit, "0", 1)
                else:
                    reversedComplementOne = reversedComplementOne.replace(digit, "1", 1)
                    complementTwo = reversedComplementOne[::-1]
                    break
                nextDigitIndex += 1
        return complementTwo

def convertBinarieToIntComplementTwo(binarieNumber: str):
    if (binarieNumber.startswith("0")):
        return (convertBinarieToReal(binarieNumber[::-1]))
    else:
        complementOne = getComplementOne(binarieNumber)
        print("C1:", complementOne)
        return sumOneInComplementOne(complementOne)