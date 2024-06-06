#!/usr/bin/python

import socket
import os
import sys
from termcolor import colored

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner, filename):
	f = open(filename, "r")
	for line in f.readlines():
		byte_data = bytes(line, "utf-8")
		if byte_data in banner:
			print(colored("[+]Servere is vulnerable: "+ str(banner), "red"))




def main():
	if len(sys.argv) == 2:
		filename  = sys.argv[1]
		if not os.path.isfile(filename):
			print(colored("[-]file doesnot exit","red"))
			exit(0)
		if not os.access(filename, os.R_OK):
			print(colored("[-]access denied","red"))
			exit(0)

	else:
		print(colored("[-]Usage"+ str(sys.argv[0]) + "<vuln filename>", "green"))
		exit(0)

	portlist = [21,22,25,80,110,443,445]
	for x in range(4,8): #loop for scan all local machines in local network
		ip = "192.168.1."+str(x)
		for port in portlist:
			banner=retBanner(ip,port)
			if banner:
				print(colored("\n[+]"+ip+" /"+ str(port)+ ":" + str(banner), "green"))
				checkVulns(banner, filename)


main()

