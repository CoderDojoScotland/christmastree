# christmastree
A Twitter-responsive Christmas Tree (different coloured LEDs light up depending on what words are tweeted by people)

The setup of the Twitter connection (using Twython) is based on this tutorial by James Bruce: http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/  
(although this particular program doesn't need to post to a Twitter account, just read the Twitter stream).

To start with, the LEDs are wired up to the GPIO pins on the Raspberry Pi as follows: ![alt-text](http://glasgow.coderdojo.co/christmastree/xmastreeCircuit_colours_numbers.png "Initial circuit layout")

Once you've got your LEDs working with your program you're ready to put the lights on your tree (or this would be a program called "christmasbreadboard.py" ;-) ). T

Take each LED from the breadboard circuit and connect each leg to a longer wire (so that it can reach your tree) like this: http://glasgow.coderdojo.co/christmastree/onetreewire_bb.png
(We didn't have very long jumper wires so joined together two shorter (male-to-female) wires).

Remember, you don't have to stick with our selection - edit christmastree.py to make your tree light up for your chosen words!

