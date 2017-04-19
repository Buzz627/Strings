import sys
code={
	"a":".-",
	"b":"-...",
	"c":"-.-.",
	"d":"-..",
	"e":".",
	"f":"..-.",
	"g":"--.",
	"h":"....",
	"i":"..",
	"j":".---",
	"k":"-.-",
	"l":".-..",
	"m":"--",
	"n":"-.",
	"o":"---",
	"p":".--.",
	"q":"--.-",
	"r":".-.",
	"s":"...",
	"t":"-",
	"u":"..-",
	"v":"...-",
	"w":".--",
	"x":"-..-",
	"y":"-.--",
	"z":"--..",
	"1":".----",
	"2":"..---",
	"3":"...--",
	"4":"....-",
	"5":".....",
	"6":"-....",
	"7":"--...",
	"8":"---..",
	"9":"----.",
	"0":"-----"
}

def strToMorse(s):
	res=[]
	s=s.lower()
	for letter in s:
		if letter in code:
			res.append(code[letter])
		else:
			res.append("#")
	return res



if __name__=="__main__":
	if len(sys.argv)<2:

		message="test"
		print message
	else:
		message=sys.argv[1]

	print strToMorse(message)
