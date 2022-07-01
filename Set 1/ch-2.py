"""

Author: MaxWarman
Cryptopals - Set 1 - Challenge 2

"""

def xorHex(h1, h2):
	if len(h1) != len(h2):
		print("Hex string lenghts do not match!")
		exit()

	xorValue = ""
	for i in range(len(h1)):
		# [2:] used to cut out '0x' prefix
		xorValue += hex(int(h1[i], 16) ^ int(h2[i], 16))[2:]

	return xorValue

def main():
	h1 = "1c0111001f010100061a024b53535009181c"
	h2 = "686974207468652062756c6c277320657965"

	xor = xorHex(h1, h2)
	print(f"h1 = {h1}")
	print(f"h2 = {h2}")
	print(f"h1^h2 = {xor}")

	assert(xor == "746865206b696420646f6e277420706c6179")

if __name__ == "__main__":
	main()