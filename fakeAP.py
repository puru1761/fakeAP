#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import Dot11, Dot11Beacon, Dot11Elt, RadioTap, sendp, hexdump
import sys
import argparse
from logs.logger import log

def createAccessPoint(interface, ssid):
    
    dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff',
            addr2='22:22:22:22:22:22', addr3='33:33:33:33:33:33')
    beacon = Dot11Beacon(cap='ESS+privacy')
    essid = Dot11Elt(ID ='SSID', info=ssid, len=len(ssid))
    rsn = Dot11Elt(ID='RSNinfo', info=(
        '\x01\x00'
        '\x00\x0f\xac\x02'
        '\x02\x00'
        '\x00\x0f\xac\x04'
        '\x00\x0f\xac\x02'
        '\x01\x00'
        '\x00\x0f\xac\x02'
        '\x00\x00'))

    frame = RadioTap()/dot11/beacon/essid/rsn
    
    log.info("Beacon Frame created with SSID: '"+ssid+"'")
    log.info("Transmitting Beacon through interface '"+interface+"'")
    
    raw_input("\nPress Enter to start Access Point '"+ssid+"'\n")
    log.success("Access Point Created!")

    sendp(frame, iface=interface, inter=0.10, loop=1)

if __name__=="__main__":

    main_page = "\033[94m[X]\033[0m Fake Wifi Access Point Creator \033[94m[X]\033[0m\n"

    parser = argparse.ArgumentParser(description=main_page, epilog="\n\033[93m[*]\033[0m Author: 0xBADB01\n\n")
    
    parser.add_argument('-i', '--interface', help='Name of the interface to be used', required=True)
    parser.add_argument('--ssid', help='Name for your fake access point', default="fakeAP")

    args = parser.parse_args()

    createAccessPoint(args.interface, args.ssid)
