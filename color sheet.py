import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

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
