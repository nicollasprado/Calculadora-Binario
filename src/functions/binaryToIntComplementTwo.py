from functions.binaryToReal import convertBinaryToReal


def getComplementOne(binaryNumber: str):
    complementOne = binaryNumber.replace("0", "temporary")
    complementOne = complementOne.replace("1", "0")
    complementOne = complementOne.replace("temporary", "1")
    return complementOne

def checkComplementOneSuccessor(reversedComplementOne: str, nextDigitIndex):
    if (reversedComplementOne[nextDigitIndex] == "1"):
        return True

def sumOneInComplementOne(complementOne: str):
    if (complementOne.endswith("1")):
        bitsQuantity = len(complementOne)
        reversedComplementOne = complementOne[::-1]

        nextDigitIndex = 1
        for digit in reversedComplementOne:
            if (nextDigitIndex <= (bitsQuantity - 1)):
                # 0111
                # 1110
                # 1
                # 0001
                # print(reversedComplementOne)
                # if (digit == "0"):
                #     reversedComplementOne = reversedComplementOne.replace(digit, "1", 1)
                    
                # elif (checkComplementOneSuccessor(reversedComplementOne, nextDigitIndex) == True):
                #     reversedComplementOne = reversedComplementOne.replace(digit, "0", 1)
                # else:
                #     reversedComplementOne = reversedComplementOne.replace(digit, "1", 1)
                #     complementTwo = reversedComplementOne
                #     break
                # nextDigitIndex += 1
        return complementTwo

def convertBinaryToIntComplementTwo(binaryNumber: str):
    if (binaryNumber.startswith("0")):
        return (convertBinaryToReal(binaryNumber[::-1]))
    else:
        complementOne = getComplementOne(binaryNumber)
        print("C1:", complementOne)
        return sumOneInComplementOne(complementOne)