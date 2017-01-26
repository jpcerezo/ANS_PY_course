#!/usr/bin/env python

import telnetlib
import time
import socket
import sys 

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def send_cmd(remote_connection, cmd):
    cmd = cmd.rstrip()
    remote_connection.write(cmd + '\n')
    time.sleep(1)
    return remote_connection.read_very_eager()

def login(remote_connection, user, passw):
    output = remote_connection.read_until("sername:", TELNET_TIMEOUT)
    remote_connection.write(user + '\n')
    output += remote_connection.read_until("ssword:", TELNET_TIMEOUT)
    remote_connection.write(passw + '\n')
    return output

def telnet_connect(ipaddr):
    try:
        return telnetlib.Telnet(ipaddr, TELNET_PORT, TELNET_TIMEOUT)
    except socket.timeout:
        sys.exit("Connection timedouttt...")

def main():
#    ip_addr = "184.105.247.70"
#    username = 'pyclass'
#    password = '88newclass'

    ip_addr = "192.168.1.230"
    username = 'juampe'
    password = 'pimp01'

    remote_conn = telnet_connect(ip_addr)
    output = login(remote_conn, username, password)
#    print ('LOGIN results... ' + output + '\n')
#    time.sleep(1)
#    output = remote_conn.read_very_eager()

    output = send_cmd(remote_conn, 'term len 0')
    output = send_cmd(remote_conn, 'show version')
    print output
    output = send_cmd(remote_conn, 'who')
    print output

    remote_conn.close()


if __name__ == "__main__":
    main()


