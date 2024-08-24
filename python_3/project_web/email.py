import subprocess
from scapy.all import ARP, Ether, srp

def scan_devices(ip_range):
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=3, verbose=False)[0]
    
    devices = []
    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})
    
    return devices

def block_device(mac_address):
    subprocess.run(["sudo", "pfctl", "-t", "blocklist", "-T", "add", mac_address])
    print(f"Device dengan MAC address {mac_address} telah diblokir.")

def unblock_device(mac_address):
    subprocess.run(["sudo", "pfctl", "-t", "blocklist", "-T", "delete", mac_address])
    print(f"Device dengan MAC address {mac_address} telah dibuka kembali.")

def main():
    ip_range = "192.168.1.1/24"  # Ganti dengan subnet jaringanmu
    devices = scan_devices(ip_range)
    
    print("Perangkat yang terhubung:")
    print("------------------------")
    for device in devices:
        print(f"IP: {device['ip']}, MAC: {device['mac']}")
    
    mac_to_block = input("Masukkan MAC address perangkat untuk diblokir (atau biarkan kosong): ").strip()
    if mac_to_block:
        block_device(mac_to_block)
    
    mac_to_unblock = input("Masukkan MAC address perangkat untuk dibuka kembali (atau biarkan kosong): ").strip()
    if mac_to_unblock:
        unblock_device(mac_to_unblock)

if __name__ == "__main__":
    main()

