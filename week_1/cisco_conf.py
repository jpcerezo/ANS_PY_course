#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse
cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

cryptomaps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

for cmaps in cryptomaps:
    print cmaps.text
    for child in cmaps.children: 
        print child.text

crypto_pf2 = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO',
childspec=r'pfs group2')

print "\nCrypto Maps using PFS2:"

for cmaps_pf2 in crypto_pf2:
        print "{0} on line {1}".format(cmaps_pf2.text, cmaps_pf2.linenum
            )

