#!/usr/bin/env python

'''
snmpwalk -Os -c galileo -v 1 50.242.94.227:8061 1.3.6.1.2.1.2




import snmp_helper
from datetime import datetime
import time


if __name__ == "__main__":
   
	IP='50.242.94.227'

	a_user='pysnmp'
	auth_key='galileo1'
	encrypt_key='galileo1'

	snmp_user = (a_user, auth_key, encrypt_key)

	pynet_rtr1 = (IP, 7961)
	pynet_rtr2 = (IP, 8061)

	base_ifInOctets_fa4 = 15789123

	etc...

	'''