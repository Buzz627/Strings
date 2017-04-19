from pyautogui import *
from morse import *
import time
import sys

def blink(sec):
	# for i in range(4):
		keyDown('capslock')
		# print  "down"
		keyUp('capslock')
		# print "up"
		time.sleep(sec)
		keyDown('capslock')
		# print  "down"
		keyUp('capslock')
		# print "up"
		# time.sleep(.5)

	# fcntl.ioctl(os.open('/dev/console',os.O_NOCTTY),19250)

def sendLetter(letter):

	for c in letter:
		if c==".":
			blink(0)
		elif c=="-":
			blink(.5)
		elif c=="#":
			time.sleep(.5)
	time.sleep(.5)

def sendMessage(mosreStr):
	for letter in mosreStr:

		sendLetter(letter)

if len(sys.argv)<2:

	message="test"
	print message
else:
	message=sys.argv[1]

print strToMorse(message)


sendMessage(strToMorse(message))