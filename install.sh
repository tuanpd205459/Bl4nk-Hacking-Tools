#!/bin/bashd


BLACK='\e[30m'
RED='\e[31m'
GREEN='\e[92m'
YELLOW='\e[33m'
ORANGE='\e[93m'
BLUE='\e[34m'
PURPLE='\e[35m'
CYAN='\e[36m'
WHITE='\e[37m'
NC='\e[0m'
purpal='\033[35m'


clear

echo -e "${ORANGE}"
echo ""
echo "
██╗███╗░░██╗░██████╗████████╗░█████╗░██╗░░░░░██╗░░░░░    ██████╗░██╗░░░░░░░██╗██╗███╗░░██╗██╗░░██╗
██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██║░░░░░██║░░░░░    ██╔══██╗██║░░░░░░██╔╝██║████╗░██║██║░██╔╝
██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░░░░██║░░░░░    ██████╦╝██║░░░░░██╔╝░██║██╔██╗██║█████═╝░
██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░░░░██║░░░░░    ██╔══██╗██║░░░░░███████║██║╚████║██╔═██╗░
██║██║░╚███║██████╔╝░░░██║░░░██║░░██║███████╗███████╗    ██████╦╝███████╗╚════██║██║░╚███║██║░╚██╗
╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚══════╝    ╚═════╝░╚══════╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝";

echo -e "${RED}                              [!] This Tool Must Run As ROOT [!]${NC}"

echo -e "${GREEN}"
echo "Do you want to install the Bl4nk hacking tool? (y/n)"
echo -n -e "${BLUE}Bl4nk >>${NC} "
read choice

if [ $choice == y ]; then
        echo "[*] Checking Internet Connection ..."
	wget -q --tries=10 --timeout=20 --spider https://google.com
	if [[ $? -eq 0 ]]; then
	    echo -e ${WHITE}"[✔] Loading ... "
	    sudo apt-get update && apt-get upgrade 
	    sudo apt-get install python-pip
            sudo apt install python3-pip
	    clear
            echo "[✔] Trying to installing Requirements ..."
            sudo apt install net-tools
		sudo pip3 install lolcat
		sudo apt-get install -y figlet
		sudo pip3 install boxes
		sudo apt-get install boxes
		sudo pip3 install flask
		sudo pip3 install requests
                sudo pip install discord_webhook 
                sudo pip install requests
                sudo pip install colorama
                sudo pip install plyer
                sudo pip install discord.py
                sudo pip install discord
                sudo pip install selenium
                sudo pip install beautifulsoup4
                sudo pip install Pillow
                sudo pip install PyAutoGUI
                sudo pip install pyperclip
                sudo pip install aiohttp
                sudo pip install pypresence
                sudo pip install pyinstaller
                sudo pip install dhooks
                sudo pip3 install discord_webhook 
                sudo pip3 install requests
                sudo pip3 install colorama
                sudo pip3 install plyer
                sudo pip3 install discord.py
                sudo pip3 install discord
                sudo pip3 install selenium
                sudo pip3 install beautifulsoup4
                sudo pip3 install Pillow
                sudo pip3 install PyAutoGUI
                sudo pip3 install pyperclip
                sudo pip3 install aiohttp
                sudo pip3 install pypresence
                sudo pip3 install pyinstaller
                sudo pip3 install dhooks
		clear
echo -e "${GREEN}[✔] Installation Successful !!!"
echo "[*] To Start The Tool Run The Main.sh With Root"
sleep 3
sudo bash main.sh
                else 
                echo -e $RED "Please Check Your Internet Connection ..!!"
        fi
if [ $choice == n ]; then
             echo "Exiting..."
             exit
    fi
        fi
