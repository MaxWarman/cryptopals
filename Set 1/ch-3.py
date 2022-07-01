"""

Author: MaxWarman
Cryptopals - Set 1 - Challenge 3

"""

def xor(txt):
	keys = "qwertyuiopasdfghjklzxcvbnm"

	for key in keys:
		xorResult = ""
		for i in range(0, len(txt), 2):
			byteChar = int(f"{txt[i]}{txt[i+1]}", 16)
			byteKey = ord(key)
			xorResult += chr(byteChar ^ byteKey)

		print(f"{xorResult}\n")

def analyze(txt):
	pass


def hexToASCII(txt):
	for i in range(0, len(txt), 2):
		print( chr( int( f"{txt[i]}{txt[i+1]}", 16)), end="")

def main():
	encoded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

	xor(encoded)

if __name__ == "__main__":
	main()