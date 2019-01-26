# Configuring the Raspberry Pi with pygame and pHAT DAC

I am using a Raspberry Pi Zero W with a pHAT DAC hat for audio out, so these config will be tailored for that.

## Write SD Card

Downloaded Raspbian Stretch from https://www.raspberrypi.org/downloads/raspbian/

    diskutil list
    diskutil unmountDisk /dev/disk5

## Initial Configuration

Boot the Raspi and do the following:

1. Open a terminal
1. Run raspi-config as sudo
1. Change hostname to pias
1. Configure wifi connection
1. Enable SSH (under Interfacing Options)
1. Enable Serial (also under Interfacing Options)
1. Reboot

## Update your Raspberry Pi

    sudo apt-get update
    sudo apt-get upgrade
    sudo reboot

## Backup SD Card

It can be useful to backup your SD Card at this point, in case you hose it somehow.

    diskutil list
    diskutil unmountDisk /dev/disk5
    sudo dd if=/dev/rdisk5 bs=1m | gzip > 2018-11-13-raspbian-python3-6.img.gz

Later if need be, you can restore this image to the card:

    diskutil unmountDisk /dev/disk5
    gzip -dc 2018-11-13-raspbian-python3-6.img.gz | sudo dd of=/dev/rdisk5 bs=1m

## Install pygame

    sudo apt-get install python3-pygame


