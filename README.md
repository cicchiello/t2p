# Touch-2-print installation instructions

## To install the operating system on a microsd card:
You can use the following img if it's not too far out of date (as of 19-July-2018):
> Dropbox file: [hanelinus-t2p-base-20180719.img.gz](https://www.dropbox.com/s/wt8fi88yu19kj7b/hanelinus-t2p-base-20180719.img.gz?dl=0)
> https://www.dropbox.com/s/wt8fi88yu19kj7b/hanelinus-t2p-base-20180719.img.gz?dl=0

You will need to download, gunzip, then install on a micro sd card.  Follow instructions from [this Raspberry Pi Foundation](https://www.raspberrypi.org/documentation/installation/installing-images) support page.

I have been using 16Gb Class 10 micro sd cards.  I wouldn't recommend using slower than Class 10, as this will be the little computer's file system.  On ther other hand, you *can* probably get away with other sizes (anything from 8Gb on up), but those haven't been tried.

The username/password are the standard for new Raspbian installs: pi/raspberry (we will be changing the password later in this process).

If you find that you wish to start with stock Raspbian, the same web site will have the latest images, but you'll also need to wrestle with stuff like getting connected to a network, installing "git" and a few other miscellaneous things.

## After your micro sd card is ready -- on to the Touch-2-Print server setup

Before powering up the Raspberry Pi, please setup a phone WiFi hotspot for communicating with the print server later.  After installation, you will need to do a bit of printer setup (at least add a printer and choose the general properties).  A hotspot is the chosen mechanism so that Raspberry Pi does not actually have to remain on your corporate network.  The installation package is expecting the hotspot to be available as follows: 
> SSID: HANELINUS
> password: 0123456789

Now, put the sd card in the Raspbery Pi, plug in your network ethernet cable, and plug in USB power.  It will take about 30 seconds before it will respond.

First, login to your Raspberry Pi from your favorite shell or terminal tool (e.g. PuTTY):
> ssh pi@\<its-ip-address>

At the first command prompt:
> wget https://github.com/cicchiello/t2p/raw/master/install.bsh

You'll now have a single file at /home/pi/install.bsh to run:
> sudo /bin/bash -c ". ./install.bsh"

# Now, get a cup of coffee -- it will take about 5 minutes

# You'll need to take note of the LAN address(es) that will be made available for administration.

# Finally, move on to [Printer Administration](https://github.com/cicchiello/t2p/raw/master/PrinterAdmin.md) to setup your printer, using the urls provided at the end of the install script.
