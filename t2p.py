#!/usr/bin/python

import os
import nfc
import nfc.snep
import threading
from collections import deque
import time

PRINTER = "/dev/ttyUSB0"

done = False
q = deque()

class PrintMgr(threading.Thread):
    def run(self):
        while not done:
            time.sleep(0.5)
            try:
                filename = q.popleft()

                #print "simulating print of filename:",filename
                print "printing:",filename
                file = open(filename, "r")
                dev = os.open(PRINTER, os.O_WRONLY)
                os.write(dev, file.read())
                os.close(dev)
                file.close()
                print "done print of:",filename
                
            except:
                pass

class DefaultSnepServer(nfc.snep.SnepServer):
    def __init__(self, llc):
        nfc.snep.SnepServer.__init__(self, llc, "urn:nfc:sn:snep", 1024 * 1024)

    def put(self, ndef_message):
        print "client has put an NDEF message"
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
    print 'Startup'
    return llc

def connected(llc):
    my_snep_server.start()
    print 'Connected'
    return True

clf = nfc.ContactlessFrontend('tty:S0:pn532')

# we're going to assume that the batgatpect file has already been loaded
#q.append("/home/pi/t2p/misc/bagtagpectab7-1-15.txt")

t = PrintMgr()
t.start()

my_snep_server = None

tries = 0
retry = True
while retry and (tries < 3):
    retry = False
    try: 
        clf.connect(llcp={'on-startup': startup, 'on-connect': connected})
        clf.close()
        print 'Disconnect'
        time.sleep(0.5)
    except:
        tries = tries + 1
        time.sleep(2)
        retry = True

print "waiting"
while len(q) > 0:
    time.sleep(2)
    print len(q)

done = True
