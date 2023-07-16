from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    # Create an ARP request packet to get information about connected devices
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    # Send the packet and capture the response
    result = srp(packet, timeout=3, verbose=0)[0]

    # Parse the response to extract the IP and MAC addresses
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    return devices

# Specify the IP range of your network to scan, such as '192.168.0.0/24'
ip_range = '192.168.0.0/24'

# Scan the network and print the connected devices
devices = scan_network(ip_range)
print(len(devices))
print("Connected devices:")
for device in devices:
    print(f"IP: {device['ip']}, MAC: {device['mac']}")
