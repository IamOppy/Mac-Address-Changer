import subprocess
import optparse
import re

def get_arguments():
	parser = optparse.OptionParser()
	parser.add_option("-i", "--interface", dest="interface", help="interface to change current MAC address")
	parser.add_option("-m", "--mac" , dest="new_mac", help="New MAC address")
	(options, arguments) = parser.parse_args()
	if not options.interface and not arguments:
		parser.error("Please Specify Interface. Use --help for info ")
	elif not options.new_mac and not arguments:
		parser.error("Please Specify MAC Address. Use --help for info")
	return options
		
	


def change_mac(interface, new_mac):
	print("Selected: %s to new MAC ADDRESS: %s" %(interface, new_mac))
	subprocess.call(["sudo", "-s", "ifconfig", interface, "down"])
	subprocess.call(["sudo", "-s", "ifconfig", interface, "hw", "ether", new_mac]) 
	subprocess.call(["sudo" , "-s", "ifconfig", interface, "up"]) 
	print('finished Update')


def get_current_mac(interface):
	ifconfig_bytes_result = subprocess.check_output(["ifconfig", interface])
	ifconfig_str_result  = str(ifconfig_bytes_result)

	MAC_address_search_result = re.search(r"\d\d:\d\d:\d\d:\d\d:\d\d:\d\d", ifconfig_str_result)
	if not MAC_address_search_result:
		print("Could not retrieve MAC address")
	else:
		return MAC_address_search_result.group(0)
	

options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current Mac = %s" %current_mac)
#change_mac(options.interface, options.new_mac)


