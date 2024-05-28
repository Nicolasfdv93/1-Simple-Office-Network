Project 1 - Simple Office Networking project - Devs Conf

Router Configurations

en
conf t
hostname R0
int range g0/0-1
no shut
exit
int g0/0
ip address 192.168.40.1 255.255.255.128
int g0/1
ip address 192.168.40.129 255.255.255.128
