#!/usr/bin/env python

import paramiko
from getpass import getpass

ip ='184.105.247.70'
username='pyclass'
password=getpass()
port=22
remote_conn_pre=paramiko.SSHClient()

remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

# SSH connection should be established
# Now invoke shell:

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(5000)  # get 5k bytes from the output
print output

# remote_conn.send("show ip int brie \n") # For cisco
# remote_conn.send("show interfaces terse \n") # For SRX

remote_conn.send("show chassis hard \n") # For SRX
output = remote_conn.recv(10000)
print output

quit()

''' 
VIDEO 2

'''

ip ='184.105.247.76'
username='pyclass'
password=getpass()
port=22
remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
# Fails

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.load_system_host_keys("/home/jcerezo/.ssh/known_hosts") # or ()
remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)

stdin, stdout, stderr = remote_conn_pre.exec_command("show ip int brie \n")
print stdout.read()

'''
Paramiko and SSH only allows only 1 command per channel open. After executed, SSH channel is down

So we must use invoke.shell() to have the session open for multiple commands

'''

remote_conn_pre.connect(ip, username=username, password=password, look_for_keys=False, allow_agent=False, port=port)
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(5000)

print output

#

output = remote_conn.send("\n")
remote_conn.settimeout(6.0)
remote_conn.gettimeout()

# Wait for more than 6 seconds...

output = remote_conn.recv(5000)
print output

remote_conn.recv_ready()
# gets False

output = remote_conn.send("\n")
remote_conn.recv_ready()
# gets True
print output
'''
pynet-rtr1#

'''
remote_conn.recv_ready()
# False

output = remote_conn.send("show run")
output = remote_conn.recv(65535)
print output
# show run 
# he didn't send the newline ...

output = remote_conn.send("")
output = remote_conn.send("\n")
output = remote_conn.recv(65535)
print output
# Whole damn config...
# now don't page

output = remote_conn.send("term len 0 \n")
output = remote_conn.recv(65535)
print output

output = remote_conn.send("show run\n")
output = remote_conn.recv(65535)
print output
# The whole config

# How to handle larger than 65535 configs ??

####################### PEXPECT

import pexpect
import sys
from getpass import getpass

def main:
	ip_addr=''
	username='pyclass'
	poert=8022
	password=getpass()

	ssh_conn = pexpect.spawn('ssh -l {} {} -p {}'.format(username, ipaddr, port))
	#ssh_conn.log = sys.stdout  # puts everything on screen

	ssh_conn.timeout = 3
	ssh_conn.expect('ssword:')
	ssh_conn.sendline(password)

	ssh_conn.expect('#')
#	print ssh_conn.before   # select the ouput befor and/or after 
	
	ssh_conn.sendline('show ip int brie') 
	ssh_conn.expect('#')
	
	ssh_conn.sendline('term len 0') 
	ssh_conn.expect('#')

	ssh_conn.sendline('show version') 
	ssh_conn.expect('pynet-rtr[12]#') # this parses a regular expression...

	try:
		ssh_conn.sendline('show version')
		ssh_conn.expect('zzzz')
	except pexpect.TIMEOUT:
		print "Found timeout"

#Parsing output:

	pattern=re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
	ssh_conn.sendline('show version')
	ssh_conn.expect(pattern)

	print ssh_conn.before 
	print ssh_conn.after

################################## NETMIKO

from netmiko import ConnectHandler
from getpass import getpass
password=getpass()

#Dictionaries:

pynet1 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.70',
    'username': 'pyclass',
    'password': password,
}

pynet2 = {
    'device_type': 'cisco_ios',
    'ip': '184.105.247.71',
    'username': 'pyclass',
    'password': password,
    'secret': '',
    'port': 22,
}

juniper_srx = {
    'device_type': 'juniper',
    'ip': '184.105.247.76',
    'username': 'pyclass',
    'password': password,
    'port': 22,
}

pynet_rtr1=ConnectHandler(**pynet1)


pynet_rtr2=ConnectHandler(**pynet2)


pynet_srx=ConnectHandler(**juniper_srx)




config_commands=['loggin buffered 19000']
outp = net_connect.send_config_set(config_commands)

outp = srx.send_command('show arp')

pynet_srx.config_mode()
pynet_srx.check_config_mode()
# would be True...

config_commands=['set system host-name tes123']
outp=pynet_srx.send_config_set(config_commands)

# change is pending. we can commit or rollback, etc.

outp=pynet_srx.commit() 
# wait for some time...


if __name__ == "__main__":
	main()



