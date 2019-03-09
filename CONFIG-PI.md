# Configuring the Raspberry Pi with pygame and pHAT DAC

I am using a Raspberry Pi Zero W with a pHAT DAC hat for audio out, so these config will be tailored for that.

## Write SD Card

Before buying SD Cards, check the compatibility of current Raspbian release here: https://elinux.org/RPi_SD_cards

Downloaded Raspbian Stretch from https://www.raspberrypi.org/downloads/raspbian/

    diskutil list
    diskutil unmountDisk /dev/disk2

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
    diskutil unmountDisk /dev/disk2
    sudo dd if=/dev/rdisk2 bs=4m | gzip > 2019-02-25-raspbian-python3-6.img.gz

Later if need be, you can restore this image to the card:

    diskutil unmountDisk /dev/disk2
    gzip -dc 2019-02-25-raspbian-python3-6.img.gz | sudo dd of=/dev/rdisk2 bs=4m
    diskutil eject /dev/disk2

## Install pygame

    sudo apt-get install python3-pygame


