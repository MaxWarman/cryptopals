"""

Author: MaxWarman
Cryptopals - Set 1 - Challenge 3

"""

import crypty

def xor(txt, key):
	xorResult = ""
	for i in range(0, len(txt), 2):
		byteChar = int(f"{txt[i]}{txt[i+1]}", 16)
		byteKey = ord(key)
		xorResult += chr(byteChar ^ byteKey)

	return xorResult

def analyze(txt):
	d = {
		'a':0.082, 'b':0.015, 'c':0.028, 'd':0.043, 'e':0.13, 'f':0.022, 'g':0.02,
		'h':0.061, 'i':0.07, 'j':0.0015, 'k':0.0077, 'l':0.04, 'm':0.024, 'n':0.067,
		'o':0.075, 'p':0.019, 'q':0.00095, 'r':0.06, 's':0.063, 't':0.091,
		'u':0.028, 'v':0.0098, 'w':0.024, 'x':0.0015, 'y':0.02, 'z':0.00074,
		' ':0.05
		}

	score = 0
	for char in txt:
		char = char.lower()
		if char in d.keys():
			score += d[char]
		else:
			score -= 10

	return score

def xorBruteForce(encodedBytes, resultList, keys = "qwertyuioplkjhgfdsazxcvbnm"):

	for key in keys:

		keyBytes = crypty.stringToBytes(key)
		xorResult = crypty.xorBytes(encodedBytes, keyBytes)
		entropy = crypty.getEntropy(xorResult)

		# List: [entropy, key(char), xorResult as string]
		resultList.append([entropy, key, crypty.bytesToString(xorResult)])

	return resultList

def printBestResults(results, n=3):
	for i in range(n):
		print(f"\nEntropy {results[i][0]} for key '{results[i][1]}':\n{results[i][2]}")
	

def main():
	encoded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	keys = "qwertyuioplkjhgfdsazxcvbnm"

	encodedBytes = crypty.hexToBytes(encoded)

	resultList = []
	
	resultList = xorBruteForce(encodedBytes, resultList)

	resultList.sort()

	printBestResults(resultList)

if __name__ == "__main__":
	main()