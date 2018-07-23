#!/usr/bin/python

import nfc
import nfc.snep

class DefaultSnepServer(nfc.snep.SnepServer):
    def __init__(self, llc):
        nfc.snep.SnepServer.__init__(self, llc, "urn:nfc:sn:snep", 1024 * 1024)

    def put(self, ndef_message):
        print "client has put an NDEF message"
        print ndef_message.pretty()
        dev = os.open("/dev/ttyUSB0",O_WRONLY)
        l = os.write(dev,ndef_message)
        if l not len(ndef_message):
            print "ERROR: Wrong number of bytes written:",l,len(ndef_message)
        os.close(dev)
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

my_snep_server = None
clf = nfc.ContactlessFrontend('tty:S0:pn532')
while True: #Replace with something that doesn't make it impossible to exit
    clf.connect(llcp={'on-startup': startup, 'on-connect': connected})
    print 'Disconnect'
