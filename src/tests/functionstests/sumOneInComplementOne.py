def sumOneInComplementOne(intValueOfComplementOne: int, sign: bool):
    if sign:
        complementTwo = (intValueOfComplementOne + 1) * -1
    else:
        complementTwo = (intValueOfComplementOne + 1)
    return complementTwo