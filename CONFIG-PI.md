# Configuring the Raspberry Pi

I am using a Raspberry Pi Zero W with a Phat DAC hat for audio out, so these config will be tailored for that.

## Write SD Card

Downloaded Raspbian Stretch from https://www.raspberrypi.org/downloads/raspbian/

    $ diskutil list
    $ diskutil unmountDisk /dev/disk5
    $ sudo dd if=2018-11-13-raspbian-stretch.img of=/dev/rdisk5 bs=1m

## Initial Configuration

Boot the Raspi and do the following:

1. Open a terminal
1. Run raspi-config as sudo
1. Change hostname to pias
1. Configure wifi connection
1. Enable SSH (under Interfacing Options)
1. Enable Serial (also under Interfacing Options)
1. Reboot

## Enable Serial Connection

Ref: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/overview

You already enabled Serial logon in the last step. Now install the appropriate driver for your desktop/laptop.

Connect the leads of the serial cable as per the diagram on the above page.

Test & Configure

I was unable to do this because the serial drivers didn't seem to be working with MacOS Mojave.

