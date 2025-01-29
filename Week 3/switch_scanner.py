import scapy.all as scapy

def scan_network(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    brodcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_brodcast = brodcast / arp_request
    answered_list = scapy.srp(arp_request_brodcast, timeout=1, verbose=False)[0]

    devices_list = []
    for element in answered_list:
        device_dict = {'ip': element[1].psrc, 'mac': element[1].hwsrc}
        devices_list.append(device_dict)
    return devices_list


def identify_switches(scan_result):
    switch_list = []
    switch_prefixes = ['00:01:02', '00:04:9f', '00:0e:08']

    for device in scan_result:
        if any(device['mac'].startswith(prefix) for prefix in switch_prefixes):
            switch_list.append(device)
    return switch_list


scan_result = scan_network("192.168.1.0/24")
switches = identify_switches(scan_result)

if switches:
    print('Detected Switches:')
    for switch in switches:
        print(f'IP: {switch['ip']}, MAC: {switch['mac']}')
else:
    print('No switches detected in the network.')
