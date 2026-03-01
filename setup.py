import os
import sys
import subprocess
import time

def clear():
    os.system('clear')

def setup():
    clear()
    print("\033[1;32m")
    print("      AKREP AİÇ - KURULUM SİHİRBAZI")
    print("      -----------------------------")
    print("\033[0m")
    
    # Kurulacak kütüphaneler
    libraries = [
        "requests",
        "beautifulsoup4",
        "phonenumbers",
        "googlesearch-python",
        "pillow"
    ]

    print(f"[*] Sistem güncellemeleri kontrol ediliyor...")
    # Termux için paket güncellemeleri (Opsiyonel ama önerilir)
    # subprocess.run(["pkg", "update", "-y"])

    print(f"[*] Python kütüphaneleri kuruluyor...")
    for lib in libraries:
        print(f"[+] {lib} yükleniyor...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print(f"    [OK] {lib} başarıyla kuruldu.")
        except:
            print(f"    [X] {lib} kurulumunda hata oluştu!")

    # Termux-API kontrolü (Link açmak için gerekli)
    print(f"[*] Sistem bileşenleri kontrol ediliyor...")
    os.system("pkg install termux-api -y")

    time.sleep(1)
    clear()
    print("\033[1;32m")
    print("      KURULUM TAMAMLANDI!")
    print("      -------------------")
    print("\033[1;37m")
    print("      Kullanım: python akrep.py")
    print("\033[0m")

if __name__ == "__main__":
    setup()
