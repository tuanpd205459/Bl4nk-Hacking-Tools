from scapy.all import *
from threading import Thread
import pandas
import time
import os


access_points = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Security"])


access_points.set_index("BSSID", inplace=True)


def data_extraction(packet):
    

    if packet.haslayer(Dot11Beacon):
        

        bssid = packet[Dot11].addr2
        

        ssid = packet[Dot11Elt].info.decode()
        

        try:
            dBm_Signal = packet.dBm_AntSignal
        except:
            dBm_Signal = "N/A"
        

        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        security = stats.get("crypto")
        

        access_points.loc[bssid] = (ssid, dBm_Signal, channel, security)

       
def print_all():
    while True:
        os.system("clear")
        print(''' 

░██╗░░░░░░░██╗██╗███████╗██╗    ░██████╗░█████╗░░█████╗░███╗░░██╗███╗░░██╗███████╗██████╗░
░██║░░██╗░░██║██║██╔════╝██║    ██╔════╝██╔══██╗██╔══██╗████╗░██║████╗░██║██╔════╝██╔══██╗
░╚██╗████╗██╔╝██║█████╗░░██║    ╚█████╗░██║░░╚═╝███████║██╔██╗██║██╔██╗██║█████╗░░██████╔╝
░░████╔═████║░██║██╔══╝░░██║    ░╚═══██╗██║░░██╗██╔══██║██║╚████║██║╚████║██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░██║██║░░░░░██║    ██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░╚███║███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝    ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝               

Made by: Mohi63
github: https://github.com/Mohi63
        	''')
        print(access_points)
        time.sleep(0.5)
        

def channel_change():
    channel = 1
    while True:
        os.system(f"iwconfig {interface} channel {ch}")
        ch = ch % 14 + 1
        time.sleep(0.5)

if __name__ == "__main__":

    interface = "wlan0"
    
    
    printer = Thread(target=print_all)
    printer.daemon = True
    printer.start()
    
   
    channel_changer = Thread(target=channel_change)
    channel_changer.daemon = True
    channel_changer.start()
    
    
    sniff(prn=data_extraction, iface=interface)
    
