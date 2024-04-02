def adjustToBitsQuantityChosen(binaryNumber: str, bitsQuantity: int):
    bitsToAdd = ""
    for quantity in range(0, (bitsQuantity - len(binaryNumber))):
        bitsToAdd += "0"
    return (bitsToAdd + binaryNumber)