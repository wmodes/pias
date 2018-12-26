# pias - a Raspberry Pi Audio Sequencer

This python3 script takes a collection of audio files and plays them in sequence, looping infinitely, paused or resumed by input on the Pi's GPIO pins.

The script is useful in museum or gallery settings where a small microprocessor is required to generate a looped audio sequence.

An optional transition sound is possible.

# Sequence List

By default the script will look for a file in the audio directory named sequence.list to order the audio sequence. If the file is not found, the script will sort the list of files and play in that order.

# Configuration

By default the script will look for a file in the run directory called config.json that configures the script. If the config file is not found, reasonable default will be tried.

# Requirements

* python3
* pygame (http://www.pygame.org/docs/ref/music.html)
* gpiozero

# Installation

## Setup and Configure Raspberry Pi

See [CONFIG-pi.md](https://github.com/wmodes/pias/blob/master/CONFIG-PI.md) for full hints on preparing your Rpi

## Clone Repository

    cd ~
    git clone git@github.com:wmodes/pias.git

## Setup pHAT DAC

Ref: https://learn.pimoroni.com/tutorial/phat/raspberry-pi-phat-dac-install

    curl https://get.pimoroni.com/phatdac | bash

We can use a test from the repo:

    cd ~/pias/experiments
    python3 pygame-test.py

You should hear audio through the pHAT DAC external audio port.

## Attach play switch

Connect your normally open switch to Ground at pin 6 and GPIO2/SDA1 12C at pin 3.

![Attach switch to pins 3 and 6](https://raw.githubusercontent.com/wmodes/pias/master/images/rpi-and-phat-dac.png "Attach switch to pins 3 and 6")

## Test script

Run the script:

    cd ~/pias
    python3 pias.py

The script should be waiting for you to depress the play switch.

If you are testing on a machine other than the Rpi, the keyboard will activate and deactivate the audio loop.

## Configure your audio Sequencer

Add audio files to ```~/pias/data```

Configure ```~/data/config.py``` adding an optional cart_list to order the audio files.

    "cart_list" : [
        "02_test.mp3",
        "03_test.mp3",
        "01_test.mp3"
    ]

without cart_list, the script will create its own based on a sorted list of files in ```~/pias/data```

## Add to rc.local

If you need the script to run when the Rpi is booted, add the following to ```/etc/rc.local```

    # start pias script
    /usr/bin/python3 /home/pi/pias/pias.py &>> /var/log/pias.log

