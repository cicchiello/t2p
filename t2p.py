#!/usr/bin/python

import os
import nfc
import nfc.snep
import threading
from collections import deque
import time
import datetime
import subprocess

PRINTER = "/dev/ttyUSB0"

#import logging
#log.info("Begin")
#logging.info("Begin") # silences a possible error from the nfc libraries
import logging
logging.basicConfig()
logger = logging.getLogger('logger')

done = False
q = deque()


def tstamp(level):
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime(level+'|'+'%Y-%m-%d %H:%M:%S|')
    return st


class PrintMgr(threading.Thread):
    def run(self):
        while not done:
            time.sleep(0.5)
            try:
                filename = q.popleft()

                #print "%sSimulating print of filename: %s" % (tstamp('DEBUG'), filename)
                print "%sprinting: %s" % (tstamp('INFO'), filename)
                file = open(filename, "r")

                print "%sSetting comm on %s" % (tstamp('INFO'),PRINTER)
                stat = subprocess.call(["stty", "-F", PRINTER, "9600", "parenb", "-parodd", "cs7"])

                dev = os.open(PRINTER, os.O_WRONLY)
                os.write(dev, file.read())
                os.close(dev)
                file.close()
                print "%sDone print of: %s" (tstamp('INFO'), filename)
                
            except:
                pass

class DefaultSnepServer(nfc.snep.SnepServer):
    def __init__(self, llc):
        nfc.snep.SnepServer.__init__(self, llc, "urn:nfc:sn:snep", 1024 * 1024)

    def put(self, ndef_message):
        print "%sClient has put an NDEF message" % tstamp('INFO')
        msg = ndef_message._records[0]._data.decode("utf-8")
        
        msgname = "/tmp/msg.txt"
        outf = open(msgname,"w")
        outf.write(msg)
        outf.close()
        q.append(msgname)
        
        return nfc.snep.Success

def startup(llc):
    global my_snep_server
    my_snep_server = DefaultSnepServer(llc)
    print '%sOnStartup' % tstamp('INFO')
    return llc

def connected(llc):
    my_snep_server.start()
    print '%sOnConnected' % tstamp('INFO')
    return True

clf = nfc.ContactlessFrontend('tty:S0:pn532')

# we're going to assume that the batgatpect file has already been loaded
#q.append("/home/pi/t2p/misc/bagtagpectab7-1-15.txt")

t = PrintMgr()
t.start()

my_snep_server = None

tries = 0
retry = True

print "%sBefore while loop" % tstamp('DEBUG')

while retry and (tries < 3):
    retry = False
    try: 
        clf.connect(llcp={'on-startup': startup, \
                          'on-connect': connected, \
                          'role': 'initiator' \
        })
        clf.close()
        print '%sDisconnect' % tstamp('INFO')
        print '%sNext Frame...\n\n\n' % tstamp('INFO')
        time.sleep(0.5)
    except:
        print '%sException caught' % tstamp('WARNING')
        tries = tries + 1
        time.sleep(2)
        retry = True

print "%sWaiting" % tstamp('INFO')
while len(q) > 0:
    time.sleep(2)
    print "%s Queue len: %d" % (tstamp('INFO'), len(q))

done = True
