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
import pprint
from dotmap import DotMap
import re

# setup
pp = pprint.PrettyPrinter(indent=4)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)-8s %(message)s',
)

#constants
config_master_filename = './config_master.json'
config_ext_filename = 'config.json'

# get master config-master
with open(config_master_filename, 'r') as f:
    config = DotMap(json.load(f))

logging.debug("Received configuration:")
logging.debug(json.dumps(config, indent=4, sort_keys=True))

# from the master config we get the data_dir
# check for external config file in data dir
config_ext_fullpath = config.data_dir + config_ext_filename
config_file = Path(config_ext_fullpath)
if config_file.is_file():
    # file exists
    with open(config_ext_fullpath, 'r') as f:
        config_ext = DotMap(json.load(f))
    #merge master config and external config
    #note external configs overwrite master configs
    config = DotMap({**config.toDict(), **config_ext.toDict()})

# set logging level based on config
#   options: CRITICAL, ERROR, WARNING, INFO, DEBUG, NOTSET
logging.getLogger().setLevel(getattr(logging, config.log_level.upper()))

logging.info("Received configuration:")
logging.info(json.dumps(config, indent=4))

class ClassName(object):
    """docstring for ClassName"""
    def __init__(self, arg):
        super(ClassName, self).__init__()
        self.arg = arg
    

def main():
    logging.info("Starting")

if __name__ == '__main__':
    main()