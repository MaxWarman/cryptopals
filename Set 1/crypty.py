"""

Author: MaxWarman

Cryptopals turbo crypto module

"""

def hexToBase64(h):
	baseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

	# 0 - take first four bits; 1 - take two bits; 2 - take last four bits;
	state = 0

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


if __name__ == "__main__":
	print("MaxWarman's Cryptopals functions module")