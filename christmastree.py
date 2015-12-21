####################################################
#import some Python libraries we'll need
####################################################

#import the time library
import time

#import the Raspberry Pi GPIO library (General Purpose In Out)
import RPi.GPIO as GPIO

#import libraries that let us use Twython
from twython import TwythonStreamer
from twython import Twython


####################################################
# set up Twitter info
####################################################

# What we want to look for on Twitter
TERMS = 'jinglebells, caroling, tinsel, mistletoe, sleigh, christmastree, whitechristmas'

#add your own Twitter access keys here
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''


########################################################
#initialise all pins and set up for each colour of light
########################################################

print "Setting the mode of the Pi..."
# Set the mode of the board
GPIO.setmode(GPIO.BCM)


print "Setting pin 18 to output for Pink..."
# Setup pin number 18 as output and initialise to "off"
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)

print "Setting  pin 24 to output for Blue"
# Setup pin number 24 as output and initialise to "off"
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, False)

print "Setting pin 22 to output for Yellow..."
# Setup pin number 22 as output and initialise to "off"
GPIO.setup(22, GPIO.OUT)
GPIO.output(22, False)

print "Setting pin 25 to output for Red..."
# Setup pin number 25 as output and initialise to "off"
GPIO.setup(25, GPIO.OUT)
GPIO.output(25, False)

print "Setting pin 21 to output for Purple..."
# Setup pin number 21 as output and initialise to "off"
GPIO.setup(21, GPIO.OUT)
GPIO.output(21, False)

print "Setting pin 17 to output for Green..."
# Setup pin number 17 as output and initialise to "off"
GPIO.setup(17, GPIO.OUT)
GPIO.output(17, False)

print "Setting pin 5 to output for Orange..."
# Setup pin number 5 as output and initialise to "off"
GPIO.setup(5, GPIO.OUT)
GPIO.output(5, False)


######################################################################
# Setup what to do when the Twython Streamer finds a matching tweet 
#####################################################################
class BlinkStreamer(TwythonStreamer):
	def on_success(self, data):
		#if data contains something labelled 'text'
		if 'text' in data:
			if 'tinsel' in data['text'] or 'Tinsel' in data['text']:
				###########################
				# print it out prettily
				###########################
				print data['text'].encode('utf-8')
				print                    
				###########################
				#blink LED when tweet seen 
				###########################
				#let the user know what we're doing
				print "Pink on..."
				#set the output of pin 18 to be True
				GPIO.output(18, True)
				#sleep for 1 second
				time.sleep(2)
				
				#let the user know what we're doing
				print "Pink off..."
				#set the output of pin 18 to be False
				GPIO.output(18, False)
				#sleep for 1 second
				time.sleep(0.5)
			elif 'mistletoe' in data['text'] or 'Mistletoe' in data['text']:
				###########################
				# print it out prettily
				###########################
				print data['text'].encode('utf-8')
				print  	
				#let the user know what we're doing
				print "Blue on..."
				#set the output of pin 22 to be True
				GPIO.output(22, True)
				#sleep for 1 second
        time.sleep(2)
        #let the user know what we're doing
        print "Blue off..."
        #set the output of pin 22 to be False
        GPIO.output(22, False)
        #sleep for 1 second
        time.sleep(0.5)
			elif 'sleigh' in data['text'] or 'Sleigh' in data['text']:
				###########################
				# print it out prettily
				###########################
				print data['text'].encode('utf-8')
				print  	
				#let the user know what we're doing
				print "Yellow on..."
				#set the output of pin 24 to be True
				GPIO.output(24, True)
				#sleep for 1 second
				time.sleep(2)
				#let the user know what we're doing
				print "Yellow off..."
				#set the output of pin 24 to be False
				GPIO.output(24, False)
				#sleep for 1 second
				time.sleep(0.5)
			elif 'christmastree' in data['text'] or 'Christmastree' in data['text'] or 'ChristmasTree' in data['text']:
				###########################
				# print it out prettily
				###########################
				print data['text'].encode('utf-8')
				print 
				#let the user know what we're doing
				print "Red on..."
        #set the output of pin 25 to be True
        GPIO.output(25, True)
        #sleep for 1 second
        time.sleep(2)
        #let the user know what we're doing
        print "Red off..."
        #set the output of pin 25 to be False
        GPIO.output(25, False)
        #sleep for 1 second
        time.sleep(0.5)	
			elif 'whitechristmas' in data['text'] or 'WhiteChristmas' in data['text']:
				###########################
				# print it out prettily
				###########################
				print data['text'].encode('utf-8')
				print 
				#let the user know what we're doing
				print "Purple on..."
				#set the output of pin 21 to be True
				GPIO.output(21, True)
				#sleep for 1 second
				time.sleep(2)
				
				#let the user know what we're doing
				print "Purple off..."
				#set the output of pin 21 to be False
				GPIO.output(21, False)
				#sleep for 1 second
				time.sleep(0.5)
			elif 'jinglebells' in data['text'] or 'JingleBells' in data['text']:
				###########################
				# print it out prettily
				###########################
				print data['text'].encode('utf-8')
				print 
				#let the user know what we're doing
				print "Green on..."
				#set the output of pin 17 to be True
				GPIO.output(17, True)
				#sleep for 1 second
				time.sleep(2)
				#let the user know what we're doing
				print "Green off..."
				#set the output of pin 17 to be False
				GPIO.output(17, False)
				#sleep for 1 second
				time.sleep(0.5)
			elif 'caroling' in data['text'] or 'Caroling' in data['text']:
				###########################
				# print it out prettily
				###########################
				print data['text'].encode('utf-8')
				print 
				#let the user know what we're doing
				print "Orange on..."
				#set the output of pin 5 to be True
				GPIO.output(5, True)
				#sleep for 1 second
				time.sleep(2)
	      #let the user know what we're doing
	      print "Orange off..."
		    #set the output of pin 5 to be False
		    GPIO.output(5, False)
		    #sleep for 1 second
		    time.sleep(0.5)    
			else:	
				print "nothing"

				
	        
##################################################################################################
# Create a streamer to watch the twitter feed for tweets that contain the string in variable TERMS
##################################################################################################
try:
    stream = BlinkStreamer(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
    # we're only interested in the ones that contain TERMS so filter them out and 
    # discard any others
    stream.statuses.filter(track=TERMS)
# the following commands make sure the program cleans up
# before it stops running to avoid errors when it runs next
except KeyboardInterrupt:
	print("stopping")
	GPIO.cleanup()
finally:
	GPIO.cleanup()
