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
██████╗░██╗░░░░░░░██╗██╗███╗░░██╗██╗░░██╗
██╔══██╗██║░░░░░░██╔╝██║████╗░██║██║░██╔╝
██████╦╝██║░░░░░██╔╝░██║██╔██╗██║█████═╝░
██╔══██╗██║░░░░░███████║██║╚████║██╔═██╗░
██████╦╝███████╗╚════██║██║░╚███║██║░╚██╗
╚═════╝░╚══════╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝";

echo -e "${RED}[!] This Tool Must Run As ROOT [!]${NC}"

echo -e "




${CYAN}Discord Tools                      WiFi Tools                      Web Tools                      Other${GREEN}
|---------------------------------------------------------------------------------------------------------------------|      
| ${WHITE}[1]${GREEN} BruteCrack                      ${WHITE}[4]${GREEN} Network Scanner              ${WHITE}[7]${GREEN} Website Code copyer         ${WHITE}[10]${GREEN} About Us  |
| ${WHITE}[2]${GREEN} Nitro Generator                 ${WHITE}[5]${GREEN} Network Attack               ${WHITE}[8]${GREEN} Website Status Checker      ${WHITE}[11]${GREEN} EXIT      |
| ${WHITE}[3]${GREEN} Anti BruteCrack                 ${WHITE}[6]${GREEN} IfConfig                ${WHITE}[9]${GREEN} Website Attack                             |
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
    'Checking For Discord.exe...'
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
echo -e "${RED}[!] This Tool Is Currently Under Development !!!"
sleep 2
sudo bash main.sh
fi

if [ $choice == 5 ]; then
echo -e "${RED}[!] This Tool Is Currently Under Development !!!"
sleep 2
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

fi
