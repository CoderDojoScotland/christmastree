#H1 twitter christmas tree 
A Twitter-responsive Christmas Tree (different coloured LEDs light up depending on what words are tweeted by people)

#H2 Authors
Claire Quigley

#Licence
![alt-text](http://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US)"Creative Commons License" This work is licensed under a [http://creativecommons.org/licenses/by-nc-sa/3.0/">Attribution-NonCommercial-ShareAlike 3.0 Unported (CC BY-NC-SA 3.0) License]

#H2 Equipment
* Raspberry Pi
* Breadboard
* 330 Ohm resistors
* White LEDs
* Coloured cellophane (e.g. from chocolate wrappers)
* Green electrical tape
* Male-to-female jumper wires
* Small Christmas tree



The setup of the Twitter connection (using Twython) is based on this tutorial by James Bruce: http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/  
(although this particular program doesn't need to post to a Twitter account, just read the Twitter stream).

To start with, set your LEDs out on a breadboard  and wire them to the GPIO pins on the Raspberry Pi as follows: ![alt-text](http://glasgow.coderdojo.co/christmastree/xmastreeCircuit_colours_numbers.png "Initial circuit layout")

Once you've got your LEDs working with your program you're ready to put the lights on your tree (or this would be a program called "christmasbreadboard.py" ;-) ). T

Take each LED from the breadboard circuit and connect each leg to a longer wire (so that it can reach your tree) like this: http://glasgow.coderdojo.co/christmastree/onetreewire_bb.png
(We didn't have very long jumper wires so joined together two shorter (male-to-female) wires).

Remember, you don't have to stick with our selection - edit christmastree.py to make your tree light up for your chosen words!

