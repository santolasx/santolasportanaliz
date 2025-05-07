import socket
from concurrent.futures import ThreadPoolExecutor

# Kullanıcıdan IP adresi al
hedef_ip = input("Hangi IP adresinin portlarını taramak istersiniz? (Örn: 192.168.1.1): ")

# Mor renk kodu
mor_renk = "\033[1;35m"
reset_renk = "\033[0m"

# Mor renk ile "SANTOLAS EKİBİ" yazısını ekleyelim
print(f"{mor_renk}SANTOLAS EKİBİ{reset_renk}")

# Portları tarayan fonksiyon
def port_tara(port):
    try:
        soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soket.settimeout(0.5)  # zaman aşımı süresi
        sonuc = soket.connect_ex((hedef_ip, port))
        if sonuc == 0:
            print(f"[+] Açık Port: {port}")
        soket.close()
    except Exception:
        pass

# Tüm portları tara
print(f"{hedef_ip} adresi üzerindeki portlar taranıyor...\n")
with ThreadPoolExecutor(max_workers=1000) as executor:
    executor.map(port_tara, range(1, 65536))
