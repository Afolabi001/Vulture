import requests
from colorama import Fore, Back, Style
import time
import sys
import os
import scanlib.js as js
import googlesearch
import threading
import urllib3
import logging
import urllib.parse
import random
import platform
from Modules import agents
import sys

sys.tracebacklimit = 0
try:
    raise Exception('This is an exception')
except Exception:
    pass

urllib3.disable_warnings()

user_agent_ = agents.get_useragent()
header = {"User-Agent": user_agent_}

#Banner
banner = print(f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣶⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⠋⠉⢻⣤⣀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣷⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠉⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀  {Fore.CYAN}• {Fore.WHITE}Platform Detection{Fore.YELLOW}:{Fore.RED}!{Fore.WHITE}⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠀⠀⠀{platform.system()} {platform.release()}⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠩⠽⢿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀Project{Fore.YELLOW}: {Fore.WHITE}Vulture⠀⠀⠀⠀⠀⠀
⠀⠀⣀⣴⣾⣿⣿⣿⣿⠟⠁⠙⢿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀Category{Fore.YELLOW}: {Fore.WHITE}Username Search⠀⠀⠀⠀⠀⠀
⠀⠈⣩⣿⣿⣿⡿⠋⠁⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀Developer{Fore.YELLOW}: {Fore.WHITE}AnonCatalyst
⠀⠈⠉⠈⠟⠉         ⣀⣽⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
               ⠉⠉⠉⠉⠉⠉⠁""")

#Platform Detection
def check_platform():
    if platform.system() == "Arch":
        return False
    elif platform.system() == "Debian" or platform.system() == "Windows":
        return True
def print_banner():
    print(banner)
    #print(f"You are running {platform.system()} {platform.release()}")
if check_platform():
    print_banner()




#Input
username = input(f"\nEnter a username{Fore.YELLOW}:{Fore.BLUE} ")


#Animation 
def load_animation():
    load_str = f"vulture is launching username search..."
    ls_len = len(load_str)
    animation = "|/-\\"
    anicount = 0
    counttime = 0        
    i = 0                     
  
    while (counttime != 100):
        time.sleep(0.075) 
        load_str_list = list(load_str) 
        x = ord(load_str_list[i])
        y = 0                             
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
        load_str = res

        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
        
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")
        
if __name__ == '__main__': 
    load_animation()


#Username Search
print(f" {Fore.RED}〘{Fore.WHITE} Username Search{Fore.YELLOW}: {Fore.CYAN}{username}{Fore.RED} 〙\n")


with open("urls.txt", "r") as f:
    url_list = (x.strip() for x in f.readlines())
def username_search(username: str, url: str):
    try:
        s = requests.Session()
        s.headers.update(header)
        response = s.get(urllib.parse.urljoin(url, username))
        status_code = response.status_code
        if status_code == 200:
            print(f"{Fore.CYAN}• {Fore.BLUE}{username} {Fore.RED}| {Fore.YELLOW}[{Fore.GREEN}✓{Fore.YELLOW}]{Fore.WHITE} URL{Fore.YELLOW}: {Fore.GREEN}{url}{Fore.WHITE} {status_code}")
        elif status_code == 404:
            print(f" {Fore.YELLOW}[{Fore.RED}×{Fore.YELLOW}] {Fore.WHITE}Profile page {Fore.RED}not found{Fore.YELLOW}:{Fore.RED} {status_code}{Fore.YELLOW}: {Fore.MAGENTA}{url}{Fore.WHITE}")
    except requests.exceptions.ConnectionError:
        print(f"{Fore.RED}╘{Fore.WHITE} Connection error{Fore.RED} !")
    except requests.exceptions.TooManyRedirects as err:
        print(f"\n{Fore.RED}╘{Fore.WHITE} Too many redirects{Fore.RED} !")

#threading
def main(username):
    threads = []
    for url in url_list:
        url = urllib.parse.urljoin(url, username)
        t = threading.Thread(target=username_search, args=(username, url))
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()
        time.sleep(0.3)

if __name__ == "__main__":
    try:
        main(username)
    except (urllib3.exceptions.MaxRetryError, requests.exceptions.RequestException):
        pass

    
print(f"\n {Fore.RED}〘 {Fore.WHITE}Domains Associated With{Fore.YELLOW}: {Fore.BLUE}{username} {Fore.RED}〙{Fore.WHITE}\n")
# Username association
try:
    for link in googlesearch.search(username):
        if username in link:
            print(f"{Fore.CYAN}⊶ {Fore.WHITE}", link)
except google.cloud.exceptions.TooManyRequests:
    print(f"{Fore.RED}[!] Too many requests, please try again later.{Fore.WHITE}")
else:
    print(f"No Other Domains Associated With: {username}")



#Google Search
#print(f"\n {Fore.RED}〘 {Fore.WHITE}Google Search For{Fore.YELLOW}: {Fore.BLUE}{username} {Fore.RED}〙{Fore.WHITE}\n")
#for urlx in googlesearch.search(username):
#    print(f"{Fore.CYAN}⊶ :{Fore.WHITE}",urlx)

import googlesearch
print(f"\n {Fore.RED}〘 {Fore.WHITE}Google Search For{Fore.YELLOW}: {Fore.BLUE}{username} {Fore.RED}〙{Fore.WHITE}\n")
choice = input(f"{Fore.YELLOW}[{Fore.CYAN}?{Fore.YELLOW}]{Fore.WHITE} Do you want to save the results? {Fore.CYAN}({Fore.WHITE}y{Fore.MAGENTA}/{Fore.WHITE}n{Fore.CYAN}){Fore.YELLOW}:{Fore.WHITE} ").lower()
if choice == "y":
    with open("usrassosiation.txt", "w") as f:
        for urlx in googlesearch.search(username):
            f.write(f"{urlx}\n")
    print("Results saved to usrassosiation.txt")
else:
    print(f"{Fore.CYAN}> {Fore.RED}Results not saved{Fore.YELLOW}...")
    for urlx in googlesearch.search(username):
        print(f"{Fore.CYAN}⊶ :{Fore.WHITE}",urlx)

