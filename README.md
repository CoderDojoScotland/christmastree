# christmastree
A Twitter-responsive Christmas Tree (different coloured LEDs light up depending on what words are tweeted by people)

The setup of the twitter connection (using Twython) is based on this tutorial by James Bruce: http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/  
(although this particular program doesn't need to post to a twitter account).

The LEDs are wired up to the GPIO pins on the Raspberry Pi as follows: http://glasgow.coderdojo.co/christmastree/xmastreeCircuit_colours_numbers.png

Once you've got your LEDs working with your program and are happy with the words it's looking for take each LED from the breadboard circuit and connect each leg to a longer wire (so that it can reach your tree) like this: http://glasgow.coderdojo.co/christmastree/onetreewire_bb.png
We didn't have very long jumper wires so joined together two shorter (male-to-female) wires.

Remember, you don't have to stick with our selection - edit christmastree.py to make your tree light up for your chosen words!

