import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

END = '\033[0m'
#text colors
print(f"{Fore.RED}Red Text")
print(f"{Fore.GREEN}Green Text")
print(f"{Fore.YELLOW}Yellow Text")
print(f"{Fore.BLUE}Blue Text")
print(f"{Fore.MAGENTA}Magenta Text")
print(f"{Fore.CYAN}Cyan Text")
print(f"{Fore.WHITE}White Text")

# background color
print(f"{Back.RED}B{Back.GREEN}A{Back.YELLOW}C{Back.BLUE}K{Back.MAGENTA}G{Back.CYAN}R{Back.WHITE}O{Back.RED}U{Back.GREEN}N{Back.YELLOW}D{Back.BLUE}!")
print(f"{Back.RED}Red Background")
print(f"{Back.GREEN}Green Background")
print(f"{Back.YELLOW}Yellow Background")
print(f"{Back.BLUE}Blue Background")
print(f"{Back.MAGENTA}Magenta Background")
print(f"{Back.CYAN}Cyan Background")
print(f"{Back.WHITE}White Background")

#bright, normal or dim text
print(f"{Style.DIM}S{Style.NORMAL}T{Style.BRIGHT}Y{Style.DIM}L{Style.NORMAL}E{Style.BRIGHT}!")
print(f"{Style.DIM}Dim Text")
print(f"{Style.NORMAL}Normal Text")
print(f"{Style.BRIGHT}Bright Text")

print(f"{Fore.YELLOW}{Back.RED}C{Back.GREEN}{Fore.RED}O{Back.YELLOW}{Fore.BLUE}M{Back.BLUE}{Fore.BLACK}B{Back.MAGENTA}{Fore.CYAN}I{Back.CYAN}{Fore.GREEN}N{Back.WHITE}A{Back.RED}T{Back.GREEN}I{Back.YELLOW}O{Back.BLUE}N")
print(f"{Fore.GREEN}{Back.YELLOW}{Style.BRIGHT}Green Text - Yellow Background - Bright")
print(f"{Fore.CYAN}{Back.WHITE}{Style.DIM}Cyan Text - White Background - Dim")
##################################################
END = '\033[0m'

# Regular Colors
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White

# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White

# Underline
UBlack="\033[4;30m"       # Black
URed="\033[4;31m"         # Red
UGreen="\033[4;32m"       # Green
UYellow="\033[4;33m"      # Yellow
UBlue="\033[4;34m"        # Blue
UPurple="\033[4;35m"      # Purple
UCyan="\033[4;36m"        # Cyan
UWhite="\033[4;37m"       # White

# Background
On_Black="\033[40m"       # Black
On_Red="\033[41m"         # Red
On_Green="\033[42m"       # Green
On_Yellow="\033[43m"      # Yellow
On_Blue="\033[44m"        # Blue
On_Purple="\033[45m"      # Purple
On_Cyan="\033[46m"        # Cyan
On_White="\033[47m"       # White