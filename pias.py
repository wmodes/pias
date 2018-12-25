# -*- coding: utf-8 -*-
"""pias - a Raspberry Pi Audio Sequencer

This python3 script takes a collection of audio files and plays them in sequence, looping infinitely, paused or resumed by input on the Pi's GPIO pins.

The script is useful in museum or gallery settings where a small microprocessor is required to generate a looped audio sequence."""

__author__ = "Wes Modes"
__copyright__ = "Copyright 2018, Wes Modes"
__credits__ = [""]
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Wes Modes"
__email__ = "wmodes@gmail.com"
__status__ = "Development"

import logging
from pathlib import Path
import json
from pprint import pformat
import os
import re
import pygame
import time
import curses

# setup
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(message)s',
)
# find out if we are running on the Raspi
rpi_system = bool(re.search('machine=\'arm', str(os.uname())))
logging.info("Running on pi: " + str(rpi_system))

#constants
config_master_filename = './config_master.json'
config_ext_filename = 'config.json'

# get master config-master
with open(config_master_filename, 'r') as f:
    config = json.load(f)

logging.debug("Received configuration:")
logging.debug(json.dumps(config, indent=4))

# from the master config we get the data_dir
# add trailing slash if necessary
if config['data_dir'][-1] != '/':
    config['data_dir'] += '/'
config_ext_fullpath = config['data_dir'] + config_ext_filename
# check for external config file in data dir
config_file = Path(config_ext_fullpath)
if config_file.is_file():
    # file exists
    with open(config_ext_fullpath, 'r') as f:
        config_ext = json.load(f)
    #merge master config and external config
    #note external configs overwrite master configs
    config = {**config, **config_ext}

# set logging level based on config
#   options: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logging.getLogger().setLevel(getattr(logging, config['log_level'].upper()))

logging.info("Received configuration:\n" + json.dumps(config, indent=4))

class CartPlayer(object):
    """responsible for sequencing and playing audio

    inputs:
        path: full path to audio files
        cart_list (optional): a list of filenames to be played
        """
    def __init__(self, path, cart_list=[]):
        # super(ClassName, self).__init__()
        self.path = path
        if cart_list:
            self.cart_list = cart_list
        else:
            self.cart_list = self.__get_cart_list()
        self.cart_index = 0
        self.play_loop = False
        logging.debug('Cart list:')
        logging.debug(pformat(self.cart_list, indent=4, width=1))
        pygame.mixer.init()
        pygame.mixer.music.set_volume(1.0)

    def __get_cart_list(self):
        logging.debug('No cart_list found. Looking in ' + self.path)
        cart_list = []
        for file in os.listdir(self.path):
            if re.match('^.*\.(mp3|wav)', file) and \
                    os.path.isfile(self.path + file):
                cart_list.append(file)
        cart_list.sort()
        return cart_list

    def __play_audio(self, fn):
        """play audio and wait for completion

        input: str -> filename (minus path)
        returns: bool -> true if completed"""
        pygame.mixer.music.load(self.path + fn)
        pygame.mixer.music.play()
        pygame.mixer.music.rewind()
        logging.debug("Audio started: " + fn)
        while (pygame.mixer.music.get_busy()):
            if not self.play_loop:
                pygame.mixer.music.stop()
                return False
            time.sleep(0.2)
            self.test_play_switch()
        logging.debug("Audio finished")
        return True

    def __loop_cart(self):
        """Loop through all of the audio in the cart_list"""
        while (True):
            self.test_play_switch()
            if self.play_loop:
                # play audio and check if completed
                if (self.__play_audio(self.cart_list[self.cart_index])):
                    # if completed, increment index
                    self.cart_index += 1
                    if self.cart_index >= len(self.cart_list):
                        self.cart_index = 0
            time.sleep(0.2)

    def start_loop(self):
        logging.debug('Starting loop')
        self.play_loop = False
        self.__loop_cart()

    def test_play_switch(self):
        """Toggle switch to play audio"""
        # different tests depending if we are on the Rpi or not
        if not rpi_system:
            if (scrn.getch() != -1):
                self.play_loop = not self.play_loop


def main():
    if 'cart_list' not in config:
        config['cart_list'] = []
    player = CartPlayer(config['data_dir'], config['cart_list'])
    player.start_loop()

if __name__ == '__main__':
    if rpi_system:
        main()
    else:
        try:
            scrn = curses.initscr()
            curses.noecho()
            scrn.nodelay(True)
            main()
        except KeyboardInterrupt:
            scrn.clear()
            scrn.refresh()
            curses.nocbreak()
            curses.endwin()