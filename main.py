import colorama
from colorama import Fore
import time
import webbrowser 
import os



def main():
    os.system('cls')
    colorama.init(autoreset=True)
    print(f"{Fore.RED}\n\n   ▄████████  ▄████████    ▄████████    ▄████████    ▄███████▄    ▄████████    ▄████████ ")
    print(f"{Fore.RED}  ███    ███ ███    ███   ███    ███   ███    ███   ███    ███   ███    ███   ███    ███ ")
    print(f"{Fore.RED}  ███    █▀  ███    █▀    ███    ███   ███    ███   ███    ███   ███    █▀    ███    ███ ")
    print(f"{Fore.RED}  ███        ███         ▄███▄▄▄▄██▀   ███    ███   ███    ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ ")
    print(f"{Fore.RED}▀███████████ ███        ▀▀███▀▀▀▀▀   ▀███████████ ▀█████████▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   ")
    print(f"{Fore.RED}         ███ ███    █▄  ▀███████████   ███    ███   ███          ███    █▄  ▀███████████ ")
    print(f"{Fore.RED}   ▄█    ███ ███    ███   ███    ███   ███    ███   ███          ███    ███   ███    ███ ")
    print(f"{Fore.RED} ▄████████▀  ████████▀    ███    ███   ███    █▀   ▄████▀        ██████████   ███    ███ ")
    print(f"{Fore.RED}                          ███    ███                                          ███    ███ ")

    
    
    maininput = input(f"{Fore.RED}\n\nEnter id server >> ")
    url = "https://servers-frontend.fivem.net/api/servers/single/" + maininput
    webbrowser.open_new(url)
    time.sleep(1)
    main()

main()