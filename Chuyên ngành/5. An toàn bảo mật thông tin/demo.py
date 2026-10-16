from scapy.all import sniff, TCP, IP, ARP
from collections import defaultdict
import time

# -------------------------------
# Chống Nmap
def detect_nmap(pkt):
    if pkt.haslayer(TCP) and pkt[TCP].flags == 'S':
        src = pkt[IP].src
        print(f"Canh bao: {src} co dau hieu tan cong")

# -------------------------------
# Chống Masscan
count = 0
start = time.time()

def detect_masscan(pkt):
    global count, start
    if pkt.haslayer(IP):
        src = pkt[IP].src
        count += 1
        if time.time() - start >= 1:
            if count > 1000:  
                print(f"Canh bao: {src} co dau hieu tan cong")
            count = 0
            start = time.time()

# -------------------------------
# Chống Unicornscan
ports = {}

def detect_unicorn(pkt):
    if pkt.haslayer(TCP):
        src = pkt[IP].src
        dport = pkt[TCP].dport
        if src not in ports:
            ports[src] = set()
        ports[src].add(dport)
        if len(ports[src]) > 50:  
            print(f"Canh bao: {src} co dau hieu tan cong")

# -------------------------------
# Chống Netdiscover / arp-scan
def detect_arp(pkt):
    if pkt.haslayer(ARP) and pkt[ARP].op == 1: 
        src = pkt[ARP].psrc
        print(f"Canh bao: {src} co dau hieu tan cong")

# -------------------------------
# Chống Angry IP Scanner / SuperScan
connections = defaultdict(int)

def detect_simple_scan(pkt):
    if pkt.haslayer(TCP):
        src = pkt[IP].src
        connections[src] += 1
        if connections[src] > 100:  
            print(f"Canh bao: {src} co dau hieu tan cong")

# -------------------------------
# Hàm tổng hợp gọi tất cả detector
def detect_all(pkt):
    detect_nmap(pkt)
    detect_masscan(pkt)
    detect_unicorn(pkt)
    detect_arp(pkt)
    detect_simple_scan(pkt)

# -------------------------------
# Chạy sniff trên interface ens33
sniff(iface="ens33", prn=detect_all, store=False)
