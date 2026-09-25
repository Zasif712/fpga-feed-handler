from scapy.all import Ether, IP, UDP, Raw, sendp, wrpcap
import time

from packet_gen import messages, build_payloads

IFACE = "Ethernet 6"            # USB Ethernet adapter name from show_interfaces()
DST_IP = "239.1.1.1"      # multicast group
DST_MAC = "01:00:5e:01:01:01"  # multicast MAC for 239.1.1.1
SRC_IP = "192.168.1.10"   # placeholder, FPGA doesn't check it
DST_PORT = 5000
SRC_PORT = 5000

SEND = True              # False = only save pcap, True = also send on IFACE

def build_packets(payloads):
    packets = []
    for payload in payloads:
        pkt = (Ether(dst=DST_MAC) /
               IP(src=SRC_IP, dst=DST_IP) / # packet's src ip and dest ip
               UDP(sport=SRC_PORT, dport=DST_PORT) /
               Raw(load=payload))
        packets.append(pkt)
    return packets

if __name__ == "__main__":
    packets = build_packets(build_payloads(messages))
    wrpcap("feed.pcap", packets)
    print(f"saved {len(packets)} packets to feed.pcap")

    if SEND:
        for pkt in packets:
            sendp(pkt, iface=IFACE, verbose=False)
            time.sleep(0.5)