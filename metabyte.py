#_xPloits3x_

import re
import argparse
import os
import csv
from colorama import init, Fore, Style

# Inizializza Colorama
init(autoreset=True)

def estrai_email(contenuto):
    email_grezze = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', contenuto)
    return sorted(set(email_grezze))

def estrai_telefono(contenuto):
    numeri = re.findall(r'\+?\d[\d\s\-]{6,}\d', contenuto)
    numeri_puliti = [re.sub(r'\s+|-', '', num) for num in numeri]
    return sorted(set(numeri_puliti))

def estrai_ip(contenuto):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    ip_grezzi = re.findall(ip_pattern, contenuto)
    ip_validi = [ip for ip in ip_grezzi if all(0 <= int(octet) <= 255 for octet in ip.split('.'))]
    return sorted(set(ip_validi))

def estrai_url(contenuto):
    url_pattern = r'https?://[^\s\'",)]+'
    urls = re.findall(url_pattern, contenuto)
    return sorted(set(urls))

def salva_csv_separato(dati, filename, intestazione):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([intestazione])
        for elemento in dati:
            writer.writerow([elemento])

def esegui_pulizia(file_path, mode):
    if not os.path.exists(file_path):
        print(Fore.RED + f"[!] The file '{file_path}' does not exist!")
        return

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        contenuto = file.read()

    email_list, phone_list, ip_list, url_list = [], [], [], []

    if mode in ['email', 'all']:
        email_list = estrai_email(contenuto)
        print(Fore.GREEN + f"[✓] {len(email_list)} Unique emails found.")
        if email_list:
            salva_csv_separato(email_list, 'email.csv', 'Email')
            print(Fore.CYAN + "[✓] Emails saved in 'email.csv'.")

    if mode in ['phone', 'all']:
        phone_list = estrai_telefono(contenuto)
        print(Fore.GREEN + f"[✓] {len(phone_list)} Unique phone numbers found.")
        if phone_list:
            salva_csv_separato(phone_list, 'phone.csv', 'Telefono')
            print(Fore.CYAN + "[✓] Phone nr. saved in 'phone.csv'.")

    if mode in ['ip', 'all']:
        ip_list = estrai_ip(contenuto)
        print(Fore.GREEN + f"[✓] {len(ip_list)} Unique IP addresses found.")
        if ip_list:
            salva_csv_separato(ip_list, 'ip.csv', 'IP')
            print(Fore.CYAN + "[✓] IPs saved in 'ip.csv'.")

    if mode in ['url', 'all']:
        url_list = estrai_url(contenuto)
        print(Fore.GREEN + f"[✓] {len(url_list)} Unique URLs found.")
        if url_list:
            salva_csv_separato(url_list, 'urls.csv', 'URL')
            print(Fore.CYAN + "[✓] URLs saved in 'urls.csv'.")

    if not (email_list or phone_list or ip_list or url_list):
        print(Fore.YELLOW + "[!] No valid data found!")

def mostra_help():
    print(Fore.CYAN + """
Usage:
  python metabyte.py -f <file.txt> -m <email|phone|ip|url|all>

Options:
  -f, --file       Input files to analyze
  -m, --mode       Mode: email, phone, ip, url, all
  -h, --help       Show this help message

Description:
  This script extracts emails, phone numbers, IPs and/or URLs from a file .txt,
  removes duplicates and saves each data type in a separate CSV file:
    - email.csv
    - phone.csv
    - ip.csv
    - urls.csv

ES:
  - python3 metabyte.py -f emails.txt -m email
  - python3 metabyte.py -f atomicurls.txt -m url
  - python3 metabyte.py -f data.txt -m all
---------------------------------------------

[+] _xPloits3c_
[+] GitHub: https://github.com/xPloits3c/MetaByte
[+] Version 1.0
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-f', '--file', help="File di input")
    parser.add_argument('-m', '--mode', help="Modalità: email, phone, ip, url, all")
    parser.add_argument('-h', '--help', action='store_true')

    args = parser.parse_args()

    if args.help or not args.file or not args.mode:
        mostra_help()
    else:
        esegui_pulizia(args.file, args.mode.lower())
