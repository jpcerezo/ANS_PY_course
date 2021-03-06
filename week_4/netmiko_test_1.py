
#!/usr/bin/env python
'''
Using Netmiko enter into configuration mode on a network device.
Verify that you are currently in configuration mode.
'''

from getpass import getpass
from netmiko import ConnectHandler
from test_devices import cisco1, cisco2, vsrx1

def main():
    '''
    Using Netmiko enter into configuration mode on a network device.
    Verify that you are currently in configuration mode.
    Juampe
    '''
    password = getpass()
    for a_dict in (cisco1, cisco2, vsrx1):
        a_dict['password'] = password
    net_connect2 = ConnectHandler(**cisco2)
    net_connect2.config_mode()
    print "\n>>>>"
    print "Checking cisco2 is in configuration mode."
    print "Config mode check: {}".format(net_connect2.check_config_mode())
    print "Current prompt: {}".format(net_connect2.find_prompt())
    print ">>>>\n"

if __name__ == "__main__":
    main()
