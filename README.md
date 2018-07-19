# Touch-2-print installation instructions

## To install the operating system on a microsd card:
You can use the following image if it's not too far out of date:
> url to Cloudant where I've placed the image
You will need to gunzip, then install on a micro sd card.  Follow instructions from here https://www.raspberrypi.org/documentation/installation/installing-images

I have been using 16Gb Class 10 micro sd cards.  You can probably get away with 8Gb, but it hasn't been tried.

If you find that you wish to start with stock Raspbian, the same web site will have the latest images, but you'll also need to wrestle with stuff like getting connected to a network and installing "git".

## After your micro sd card is ready

Once you have your micro sd, you're ready to install all the t2p-specific code.

First, login to your Raspberry Pi from your favorite shell or terminal tool (e.g. PuTTY):
> ssh pi@<its-ip-address>

At the first command prompt:
> wget https://github.com/cicchiello/t2p/raw/master/install.bsh

You'll now have a single file at /home/pi/install.bsh
> sudo /bin/bash -c ". ./install.bsh"

# now, get a cup of coffee -- it will take a little while
