#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

intf = cisco_cfg.find_objects(r"^interface")

for i in intf:
    print i.text

fa4 = intf[4]

print fa4
print "just the namew ^^\n"

for child in fa4.children: 
    print child.text

print fa4.children
print "in RAW ^^\n"

crypto_pki = cisco_cfg.find_objects(r"^crypto pki certificate")

#crypto_pki = crypto_pki[0]
#crypto_pki.children 
#for child2 in crypto_pki.allchildren:
#    print child.text

ifaces_noip = cisco_cfg.find_objects_w_child(parentspec=r"^interface", childspec=r"no ip address")
print ifaces_noip

i
