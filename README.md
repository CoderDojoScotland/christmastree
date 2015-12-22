# CoderDojo Scotland Twitter-lit Christmas Tree 
A Twitter-responsive Christmas Tree (different coloured LEDs light up depending on what words are tweeted by people)

##Licence
This work is licensed under an [Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0) License] (http://creativecommons.org/licenses/by-nc-sa/3.0/)

## Equipment
* Raspberry Pi
* Breadboard
* 330 Ohm resistors
* White LEDs
* Coloured cellophane (e.g. from chocolate wrappers)
* Green electrical tape
* Male-to-female jumper wires
* Small Christmas tree

## Instructions

###Twitter stream

The setup of a Twitter connection (using Twython) on your Raspberry Pi is based on this tutorial by James Bruce: http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/  
(although our Christmas Tree program doesn't need to post to a Twitter account, it just reads the Twitter stream).

### Christmas LEDs

Next, set your LEDs out on a breadboard and wire them to the GPIO pins on the Raspberry Pi as follows: ![alt-text](http://glasgow.coderdojo.co/christmastree/xmastreeCircuit_colours_numbers.png "Initial circuit layout")

We used white LEDs with small sections of the cellophane wrappers from some chocolates placed over them and taped down with green electrical tape.  (Obviously this may involve eating some chocolates; we can only apologise for the added difficulties in this project).

![alt-text](http://glasgow.coderdojo.co/christmastree/redled.jpg "colouring LEDs with cellophane")

### Run the Code
Download christmastree.py to your Pi.  To run the program, open an LXTerminal, [navigate](https://www.raspberrypi.org/documentation/usage/terminal/) to where the program is and type 

`sudo python christmastree.py`

### Deck the Tree
Once you've got your LEDs working with your program you're ready to put the lights on your tree (or this would be a program called "christmasbreadboard.py" ;-) ). 

Take each LED from the breadboard circuit and connect each leg to a longer wire (so that it can reach your tree) like this: ![alt-text](http://glasgow.coderdojo.co/christmastree/onetreewire_bb.png "longer wire attached to LED")

We didn't have very long jumper wires so joined together two shorter (male-to-female) wires).  We also wrapped the jumper wires in green tape so that they weren't so obtrusive on the tree, but you might like to see your wires (a tech alternative to tinsel).

![alt-text](http://glasgow.coderdojo.co/christmastree/wires.jpg "making longer jumper wires")


### Remix the Tree
Remember, you don't have to stick with our selection - edit christmastree.py to make your tree light up for your chosen words!

