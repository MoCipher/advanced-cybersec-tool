def send_packet(packet):
    from scapy.all import send
    send(packet)

def sniff_packets(interface, count=10):
    from scapy.all import sniff
    packets = sniff(iface=interface, count=count)
    return packets

def create_packet(protocol, src, dst, payload):
    from scapy.all import IP, TCP, UDP, Raw
    if protocol.lower() == 'tcp':
        return IP(src=src, dst=dst) / TCP() / Raw(load=payload)
    elif protocol.lower() == 'udp':
        return IP(src=src, dst=dst) / UDP() / Raw(load=payload)
    else:
        raise ValueError("Unsupported protocol: {}".format(protocol))