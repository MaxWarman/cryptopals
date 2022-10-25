"""

Author: MaxWarman
Cryptopals - Set 1 - Challenge 6

"""

import crypty

"""
def slowGetHammingDistance(bytes1, bytes2):

    if len(bytes1) != len(bytes2):
        raise ValueError("Byte sequences have unequal lenght!")

    hammingDistance = 0

    for i in range(len(bytes1)):
        xorByte = bytes1[i]^bytes2[i]
        for j in range(8):
            hammingDistance += (xorByte>>j) & 1

    return hammingDistance


def countBitsInInt(number1):

    count = 0
    while number1 > 0:
        count += number1 & 1
        number1 >>= 1

    return count
"""

def main():
    
    maxKeyLength = 40
    minKeyLength = 2
    
    minHammingDistance = None
    keySizes = []

    for keySize1 in range(minKeyLength, maxKeyLength-1):
        for keySize2 in range(keySize1+1, maxKeyLength):

            keySize1Bytes = crypty.intToBytes(keySize1)
            keySize2Bytes = crypty.intToBytes(keySize2)
            currentHammingDistance = crypty.getHammingDistance(keySize1Bytes, keySize2Bytes)
            
            if minHammingDistance == None or currentHammingDistance < minHammingDistance:
                minHammingDistance = currentHammingDistance
                keySizes.clear()
                keySizes.append(keySize1)
                keySizes.append(keySize2)

            elif currentHammingDistance == minHammingDistance:
                if keySize1 not in keySizes:
                    keySizes.append(keySize1)
                if keySize2 not in keySizes:
                    keySizes.append(keySize2)

    print(keySizes)
    
if __name__ == "__main__":
    main()