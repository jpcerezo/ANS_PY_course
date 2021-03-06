
#!/usr/bin/env python

import telnetlib
import time
import socket
import sys 

# maybe this need to be installed. Better, using pip install pysnmp
import pysnmp

# check with pysnmp.version insstrucion

'''
check OID 1.3.6.1.2.1.1.1  (plus the .0 at the end as is an scalar):

snmpget -v 1 -c galileo 184.105.247.70 1.3.6.1.2.1.1.1.0
snmpwalk -v 1 -c galileo 184.105.247.70 1.3.6.1.2.1.1
'''

COMMUNITY_STRING='galileo'
SNMP_PORT=161
IP='184.105.247.70'

#tuple:
a_device=(IP, COMMUNITY_STRING, SNMP_PORT)
# a_device[0], etc. 

from snmp_helper import snmp_get_oid,snmp_extract

# or alternatively do 
#import snmp_helper
# but you will have to PRECEDE all snmp funciotns with snmp_helper(dot).



OID='1.3.6.1.2.1.1.1.0'

snmp_data=snmp_get_oid(a_device, oid=OID)

'''
>>> print snmp_data
[ObjectType(ObjectIdentity(ObjectName('1.3.6.1.2.1.1.1.0')), DisplayString(subtypeSpec=ConstraintsIntersection(ConstraintsIntersection(ConstraintsIntersection(ConstraintsIntersection(), ValueSizeConstraint(0, 65535)), ValueSizeConstraint(0, 255)), ValueSizeConstraint(0, 255)), hexValue='436973636f20494f5320536f6674776172652c204338383020536f667477617265202843383830444154412d554e4956455253414c4b392d4d292c2056657273696f6e2031352e3428322954312c2052454c4541534520534f4654574152452028666333290d0a546563686e6963616c20537570706f72743a20687474703a2f2f7777772e636973636f2e636f6d2f74656368737570706f72740d0a436f707972696768742028632920313938362d3230313420627920436973636f2053797374656d732c20496e632e0d0a436f6d70696c6564205468752032362d4a756e2d31342031343a31352062792070726f645f72656c5f7465616d'))]
'''

# human-readable format...
output=snmp_extract(snmp_data)

'''
>>> print output
Cisco IOS Software, C880 Software (C880DATA-UNIVERSALK9-M), Version 15.4(2)T1, RELEASE SOFTWARE (fc3)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2014 by Cisco Systems, Inc.
Compiled Thu 26-Jun-14 14:15 by prod_rel_team

'''

OID='1.3.6.1.2.1.1.5.0'

'''
>>> output=snmp_extract(snmp_data)
>>> snmp_data=snmp_get_oid(a_device, oid=OID)
>>> output=snmp_extract(snmp_data)
>>> print output
pynet-rtr1.twb-tech.com
>>> 
'''
