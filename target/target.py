#!/usr/bin/python

import logging.config
import nfc

logger = logging.getLogger(__name__)

clf = nfc.ContactlessFrontend()
assert clf.open('tty:S0:pn532') is True  # open /dev/ttyUSB0 with arygon driver

print "Hello"
clf.close()
