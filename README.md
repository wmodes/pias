# pias - a Raspberry Pi Audio Sequencer

This python3 script takes a collection of audio files and plays them in sequence, looping infinitely, paused or resumed by input on the Pi's GPIO pins.

The script is useful in museum or gallery settings where a small microprocessor is required to generate a looped audio sequence.

An optional transition sound is possible.

# Sequence List

By default the script will look for a file in the audio directory named sequence.list to order the audio sequence. If the file is not found, the script will sort the list of files and play in that order.

# Configuration

By default the script will look for a file in the run directory called config.cfg that configures the script. If the config file is not found, reasonable default will be tried.

# Requirements

* python3
* pyaudio

# Installation

