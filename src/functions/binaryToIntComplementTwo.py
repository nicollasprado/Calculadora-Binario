from src.functions.binaryToDecimal import convertBinaryToDecimal


def getComplementOne(binaryNumber: str):
    complementOne = binaryNumber.replace("0", "temporary")
    complementOne = complementOne.replace("1", "0")
    complementOne = complementOne.replace("temporary", "1")
    return complementOne

def sumOneInComplementOne(complementOne: str):
    intValueOfComplementOne = convertBinaryToDecimal(complementOne[::-1])
    complementTwo = (intValueOfComplementOne + 1) * -1
    return complementTwo

def convertBinaryToIntComplementTwo(binaryNumber: str):
    if (binaryNumber.startswith("0")):
        return (convertBinaryToDecimal(binaryNumber[::-1]))
    else:
        complementOne = getComplementOne(binaryNumber)
        return sumOneInComplementOne(complementOne)