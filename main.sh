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

if [[ "$(id -u)" -ne 0 ]]; then
  echo -e "${RED}Unable To Start Bl4nk, Are You Rooted? "
  exit 1
fi
function main() {
        echo "Complete!"
        exit 1
}


clear

echo -e "${ORANGE}"
echo ""
echo "
██████╗░██╗░░░░░░░██╗██╗███╗░░██╗██╗░░██╗
██╔══██╗██║░░░░░░██╔╝██║████╗░██║██║░██╔╝
██████╦╝██║░░░░░██╔╝░██║██╔██╗██║█████═╝░
██╔══██╗██║░░░░░███████║██║╚████║██╔═██╗░
██████╦╝███████╗╚════██║██║░╚███║██║░╚██╗
╚═════╝░╚══════╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝";

echo -e "${RED}[!] This Tool Must Run As ROOT [!]${NC}"

echo -e "
${CYAN}Discord Tools                            WiFi Tools                            Web Tools                      Other${GREEN}
|---------------------------------------------------------------------------------------------------------------------|      
| ${WHITE}[1]${GREEN} BruteCrack                      ${WHITE}[4]${GREEN} Network Scanner              ${WHITE}[7]${GREEN} Website Code copier         ${WHITE}[10]${GREEN} About Us  |
| ${WHITE}[2]${GREEN} Nitro Generator                 ${WHITE}[5]${GREEN} Fake AP                      ${WHITE}[8]${GREEN} Website Status Checker      ${WHITE}[11]${GREEN} EXIT      |
| ${WHITE}[3]${GREEN} Anti BruteCrack                 ${WHITE}[6]${GREEN} IfConfig                     ${WHITE}[9]${GREEN} Website Attack                             |
|                                                                                                                     |
                                                                                                                     
| --------------------------------------------------------------------------------------------------------------------|
${NC}";
echo -n -e "${BLUE}Bl4nk >>${NC} "
read choice

if [ $choice == 1 ]; then
cd modules
sudo python3 BruteCrack.py
sleep 2
sudo bash main.sh
fi
if [ $choice == 2 ]; then
cd modules
sudo python3 NitroGen.py
sleep 2
fi

if [ $choice == 3 ]; then
phases=( 
    'Checking For Token...'
    'Loading Assets...'
    'Checking For Weaknesses...'
    'Finishing...'
)   

for i in $(seq 1 100); do  
    sleep 0.1

    if [ $i -eq 100 ]; then
        echo -e "XXX\n100\nNo Weaknesses Found!\nXXX"
        sleep 3
    elif [ $(($i % 25)) -eq 0 ]; then
        let "phase = $i / 25"
        echo -e "XXX\n$i\n${phases[phase]}\nXXX"
    else
        echo $i
    fi 
done | whiptail --title 'AntiBruteCrack' --gauge "${phases[0]}" 6 60 0
sleep 2
sudo bash main.sh
fi

if [ $choice == 4 ]; then
echo -e "${RED}[!] This Tool Will Only Work On Operating Systems With Wlan0 (Kali Linux, Parrot Os etc.) Do You Want To Continue? (y/n)"
echo -n -e "${BLUE}Bl4nk >>${NC} "
read choice
if [ $choice == y ]; then
echo "Loading..."
echo -ne '#####                     (33%)\r'
sleep 1
echo -ne '#############             (66%)\r'
sleep 1
echo -ne '#######################   (100%)\r'
echo -ne '\n'
echo "Done!!!"
sleep 2
clear
cd modules
echo -e "${RED}[!] This Tool Needs Monitoring Mode Enabled To Work, Do You Want To Enable Monitoring Mode? (y/n)"
echo -n -e "${BLUE}Bl4nk >>${NC} "
read choice 
if [ $choice == y ]; then
sudo ifconfig wlan0 down
sudo iwconfig wlan0 mode monitor
sudo ifconfig wlan0 up
echo -e "${GREEN}[*] Monitoring Mode Enabled Successfully !!!"
sleep 2
python3 wifi-scanner.py
else
    echo -e "${RED}Exiting ..."
sleep 2
cd -
sudo bash main.sh
fi
fi
fi
if [ $choice == 5 ]; then
echo -e "${RED}[!] This Tool Will Only Work On Operating Systems With Wlan0 (Kali Linux, Parrot Os etc.) Do You Want To Continue? (y/n)"
echo -n -e "${BLUE}Bl4nk >>${NC} "
read choice
if [ $choice == y ]; then
echo "Loading..."
echo -ne '#####                     (33%)\r'
sleep 1
echo -ne '#############             (66%)\r'
sleep 1
echo -ne '#######################   (100%)\r'
echo -ne '\n'
echo "Done!!!"
sleep 2
clear
cd modules
clear
sudo python3 FakeAP.py
else
    cd -
    sudo bash main.sh
fi

if [ $choice == 6 ]; then
ifconfig
sleep 15
sudo bash main.sh
    fi

if [ $choice == 7 ]; then
echo -e "${RED}[!] This Tool Is Currently Under Development !!!"
sleep 2
sudo bash main.sh
    fi

if [ $choice == 8 ]; then
echo -e "${RED}[!] This Tool Is Currently Under Development !!!"
sleep 2
sudo bash main.sh
    fi

if [ $choice == 9 ]; then
echo -e "${RED}[!] This Tool Is Currently Under Development !!!"
sleep 2
sudo bash main.sh
fi
if [ $choice == 10 ]; then
echo -e "${GREEN}[*] This Tool Is Made For Education Purposes Only !!!
[*] This tool is actively being worked on !!!
[*] Developer: Mohi63
[*] GitHub: https://github.com/Mohi63 "
sleep 5
sudo bash main.sh
fi

if [ $choice == 11 ]; then
echo -e "${RED}Exiting..."
    exit
    clear
fi
fi
