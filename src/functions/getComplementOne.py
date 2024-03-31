def getComplementOne(binaryNumber: str):
    complementOne = binaryNumber.replace("0", "temporary")
    complementOne = complementOne.replace("1", "0")
    complementOne = complementOne.replace("temporary", "1")
    return complementOne