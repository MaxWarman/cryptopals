"""

Author: MaxWarman
Cryptopals - Set 1 - Challenge 3

"""

import crypty

def xorBruteForce(encodedBytes, resultList):

	for key in range(256):
		keyByte = crypty.hexToBytes(hex(key)[2:])
		xorResult = crypty.xorBytes(encodedBytes, keyByte)
		score = crypty.getEnglishScore(xorResult)

		# List: [entropy, key(char), xorResult as string]
		resultList.append([score, crypty.bytesToString(keyByte), crypty.bytesToString(xorResult)])

	return resultList

def printBestResults(results, n=3):
	for i in range(n):
		print(f"\nEntropy {results[i][0]} for key '{results[i][1]}':\n{results[i][2]}")
	

def main():
	encoded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

	encodedBytes = crypty.hexToBytes(encoded)

	resultList = []
	
	resultList = xorBruteForce(encodedBytes, resultList)

	resultList.sort()

	printBestResults(resultList, 3)

if __name__ == "__main__":
	main()