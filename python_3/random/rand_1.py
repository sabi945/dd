from scapy.all import *
from scapy.layers.inet import IP  # Mengimpor hanya kelas IP
from scapy.layers.inet import ICMP  # Mengimpor hanya kelas IP
import time

import socket

def packet_callback(pkt):
    if IP in pkt:
        try:
            src_domain = socket.gethostbyaddr(pkt[IP].src)[0]
            dst_domain = socket.gethostbyaddr(pkt[IP].dst)[0]
            print(f"Sumber: {src_domain}, Tujuan: {dst_domain}, Protokol: {pkt[IP].proto}")
        except socket.herror:
            print(f"Sumber: {pkt[IP].src}, Tujuan: {pkt[IP].dst}, Protokol: {pkt[IP].proto}")
        time.sleep(1)

sniff(prn=packet_callback, filter="ip", store=0)