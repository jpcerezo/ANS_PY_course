#!/usr/bin/env python
import re
from ciscoconfparse import CiscoConfParse

cisco_cfg = CiscoConfParse("cisco_ipsec.txt")

cryptomaps = cisco_cfg.find_objects(r"^crypto map CRYPTO")

print('\n3: Print all nice CryptoMaps')
print('-'* 80)

for cmaps in cryptomaps:
    	print cmaps.text
    	for child in cmaps.children: 
        	print child.text

crypto_pf2 = cisco_cfg.find_objects_w_child(parentspec=r'crypto map CRYPTO', childspec=r'pfs group2')

print "\nCrypto Maps using PFS2:"

for cmaps_pf2 in crypto_pf2:
        print "{0} on line {1}".format(cmaps_pf2.text, cmaps_pf2.linenum)

crypto_AES = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO', childspec=r'AES')

print "\nCrypto maps NOT using AES:"
for entry in crypto_AES:
	for child in entry.children:
        	 if 'transform' in child.text:
              		match = re.search(r"set transform-set (.*)$", child.text)
              		encryption = match.group(1)
	print "  {0} |-->  {1}".format(entry.text.strip(), encryption)
print
