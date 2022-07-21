"""

Author: MaxWarman
Cryptopals - Set 1 - Challenge 4

"""

from unittest import result
import crypty
import ch3

def getLineWithLowestEntropy(inputFilePath):
	
	lowestEntropy = None
	resultLine = None

	for line in open(inputFilePath, "rt"):
		line = line.replace("\n", "")
		lineBytes = crypty.hexToBytes(line)
		
		if lowestEntropy == None and resultLine == None:
			resultLine = line
			lowestEntropy = crypty.getShannonEntropy(lineBytes)
			continue

		currentEntropy = crypty.getShannonEntropy(lineBytes)

		if currentEntropy < lowestEntropy:
			lowestEntropy = currentEntropy
			resultLine = line

	print(lowestEntropy)
	return resultLine

def xorBruteForce(encodedBytes, resultList):

	for key in range(256):
		keyByte = crypty.hexToBytes(hex(key)[2:])
		xorResult = crypty.xorBytes(encodedBytes, keyByte)
		score = crypty.getEnglishScore(xorResult)

		# List: [entropy, key(char), xorResult as string]
		resultList.append([score, crypty.bytesToString(keyByte), crypty.bytesToString(xorResult)])

	return resultList

def fasterSolution():
	inputFilePath = "4.txt"
	encoded = getLineWithLowestEntropy(inputFilePath)
	encodedBytes = crypty.hexToBytes(encoded)

	resultList = []

	resultList = xorBruteForce(encodedBytes, resultList)

	resultList.sort()

	ch3.printBestResults(resultList)

def slowerSolution():
	inputFilePath = "4.txt"

	resultList = []
	for line in open(inputFilePath, "rt"):
		encoded = line.replace("\n", "")
		encodedBytes = crypty.hexToBytes(encoded)
		resultList = xorBruteForce(encodedBytes, resultList)

	resultList.sort()
	ch3.printBestResults(resultList)

def main():

	fasterSolution()
	#print("----------------------")
	#slowerSolution()

if __name__ == "__main__":
	main()