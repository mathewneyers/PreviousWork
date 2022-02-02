#!/usr/bin/env python3
#Emaple using pxssh
from pexpect import pxssh
def get_hostname(hostname):
    # Login to host
    s = pxssh.pxssh()
    #hostname = "192.168.0.111"
    username = "justincase"
    password = "Password01"
    s.login(hostname, username, password)
    # Get hostname
    s.sendline("hostname")
    s.prompt()
    print(s.before)
    # Logout
    s.logout()

ip_addresses = [ "192.168.0.111", "192.168.0.112", "192.168.0.121", "192.168.0.122"]
for ip_address in ip_addresses:
    get_hostname(ip_address)