#!/usr/bin/env python3
#Example pexpect on SSH
import pexpect

def get_uptime(address):
    child = pexpect.spawn("ssh justincase@" + address)
    child.expect(".*password:")
    child.sendline("Password01")
    child.expect(".*\$")
    child.sendline("uptime")
    child.expect(".*\$")
    print(child.after)
    child.sendline("exit")

ip_addresses = [ "192.168.0.111", "192.168.0.112", "192.168.0.121", "192.168.0.122"]
for ip_address in ip_addresses:
    get_uptime(ip_address)