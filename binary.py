import sys
import re
def decToBin(num):
	return "{:0>8}".format(bin(num)[2:])

def binToDec(num):
	return int(num, 2)


def strToBin(message):
	result=[]
	for letter in message:
		result.append(decToBin( ord(letter)))
	return "".join(result)

def binToStr(message):
	if len(message)<8:
		return ""
	cur=message[:8]
	return chr(binToDec(cur))+binToStr(message[8:])



if __name__=="__main__":
	if len(sys.argv)>1:
		message=sys.argv[1]

	else:
		# message=raw_input("enter message: ")
		message="01110100011001010111001101110100"
	

	pattern=re.compile("^[01]+$")

	if pattern.match(message):
		print binToStr(message)
	else:
		print strToBin(message)