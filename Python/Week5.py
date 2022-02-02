#!/usr/bin/env python3
import pexpect

#Create user with my name
def create_user(address):
    child = pexpect.spawn("ssh justincase@" + address)
    child.expect(".*:")
    child.sendline("Password01")
    child.expect(".*\$")
    child.sendline("sudo adduser mat_neyers")
    child.expect(".*:")
    child.sendline("newPassword01")
    child.expect(".*:")
    child.sendline("newPassword01")
    child.expect(".*:")
    child.sendline("Mathew Neyers")
    child.expect(".*:")
    child.sendline("IT-385")
    child.expect(".*:")
    child.sendline("12345678910")
    child.expect(".*:")
    child.sendline("98765432101")
    child.expect(".*:")
    child.sendline("Week 5 Assignment")
    child.expect(".*\]")
    child.sendline("y")
    child.expect(".*\$")
    child.sendline("exit")

#Install Apache2 and auto-start
def install_apache2(address):
    child = pexpect.spawn("ssh justincase@" + address)
    child.expect(".*:")
    child.sendline("Password01")
    child.expect(".*\$")
    child.sendline("sudo apt install apache2")
    child.expect(".*\]")
    child.sendline("y")
    child.expect(".*:")
    child.sendline("Password01")
    child.expect(".*\$")
    child.sendline("sudo ufw app list")
    child.expect(".*\$")
    child.sendline("sudo ufw allow 'Apache'")
    child.expect(".*\$")
    child.sendline("sudo ufw start apache2")
    child.expect(".*\$")
    child.sendline("sudo ufw enable apache2")
    child.expect(".*\$")
    child.sendline("exit")

ip_addresses = [ "192.168.0.111", "192.168.0.112", "192.168.0.121", "192.168.0.122"]
for ip_address in ip_addresses:
    create_user(ip_address)
apache2Install = [ "192.168.0.111", "192.168.0.112" ]
for ip_addr in apache2Install:
    install_apache2(ip_addr)
