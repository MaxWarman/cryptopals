"""

Author: MaxWarman
Cryptopals - Set 1 - Challenge 4

"""

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
			lowestEntropy = crypty.getEntropy(lineBytes)
			continue

		currentEntropy = crypty.getEntropy(lineBytes)

		if currentEntropy < lowestEntropy:
			lowestEntropy = currentEntropy
			resultLine = line

	print(f"{lowestEntropy}:\t'{crypty.hexToString(resultLine)}'")
	return resultLine

def fasterSolution():
	inputFilePath = "4.txt"
	encoded = getLineWithLowestEntropy(inputFilePath)
	encodedBytes = crypty.hexToBytes(encoded)

	resultList = []

	resultList = ch3.xorBruteForce(encodedBytes, resultList)

	resultList.sort()

	ch3.printBestResults(resultList)

def slowerSolution():
	inputFilePath = "4.txt"

	resultList = []
	for line in open(inputFilePath, "rt"):
		encoded = line.replace("\n", "")
		encodedBytes = crypty.hexToBytes(encoded)
		resultList = ch3.xorBruteForce(encodedBytes, resultList)

	resultList.sort()
	ch3.printBestResults(resultList, 5)


def main():

	#fasterSolution()
	slowerSolution()

if __name__ == "__main__":
	main()