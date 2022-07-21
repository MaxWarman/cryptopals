"""

Author: MaxWarman
Cryptopals - Set 1 - Challenge 1

"""
import time
def hexToBase64(h):
	baseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

	state = 0 # 0 - take first four; 1 - take two; 2 - take last 4;

	base64 = ""

	base = 0
	buffer = 0

	for digit in h:

		if state == 0:
			base = int(digit, 16)

		elif state == 1:
			buffer = int(digit, 16)

			base = (base << 2) | (buffer >> 2)

			base64 += baseChars[base]
			
			base = 0

		else:
			# Get rid of two left most bits
			buffer &= ~((1 << 3) | (1 << 2))

			buffer = (buffer << 4)

			base = buffer | int(digit, 16)

			base64 += baseChars[base]

			base = 0
			buffer = 0

		state += 1
		if state > 2:
			state = 0

	return base64

def main():
	
	txt = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

	b64 = hexToBase64(txt)

	print(f"Input: {txt}")
	print(f"Base64: {b64}")

	assert(hexToBase64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
			== "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t")

if __name__ == "__main__":
	main()