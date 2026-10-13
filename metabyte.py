# _xPloits3x
# MetaByte_v1.2
import re
import argparse
import os
import csv
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

def extract_email(content):
    email_raw = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', content)
    return sorted(set(email_raw))

def extract_phone(content):
    numbers = re.findall(r'\+?\d[\d\s\-]{6,}\d', content)
    cleaned_numbers = [re.sub(r'\s+|-', '', num) for num in numbers]
    return sorted(set(cleaned_numbers))

def extract_ip(content):
    ip_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
    raw_ips = re.findall(ip_pattern, content)
    valid_ips = [ip for ip in raw_ips if all(0 <= int(octet) <= 255 for octet in ip.split('.'))]
    return sorted(set(valid_ips))

def extract_url(content, remove_links=None):
    url_pattern = r'https?://[^\s\'",)]+'
    urls = re.findall(url_pattern, content)
    if remove_links:
        urls = [url for url in urls if not any(link in url for link in remove_links)]
    return sorted(set(urls))

def extract_url_with_params(content, filters=None):
    pattern = r'https?://[^\s\'",)]+\?[^\s\'",)]+=[^\s\'",)]+'
    url_param = re.findall(pattern, content)
    unique_urls = sorted(set(url_param))

    if filters:
        parameters = [f.strip().lower() for f in filters]
        filtered_urls = []
        for url in unique_urls:
            for p in parameters:
                if f"{p}=" in url.lower():
                    filtered_urls.append(url)
                    break
        return filtered_urls
    return unique_urls

def save_csv_separate(data, filename, header):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([header])
        for element in data:
            writer.writerow([element])

def load_links_to_remove(file_path):
    if not os.path.exists(file_path):
        print(Fore.RED + f"[!] The file '{file_path}' does not exist!")
        return []
    with open(file_path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file if line.strip()]

def execute_cleanup(file_path, mode, filters=None, links_to_remove=None):
    if not os.path.exists(file_path):
        print(Fore.RED + f"[!] The file '{file_path}' does not exist!")
        return

    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    email_list = []
    phone_list = []
    ip_list = []
    url_list = []
    url_params_list = []

    # Extract emails
    if mode in ['email', 'all']:
        email_list = extract_email(content)
        print(Fore.GREEN + f"[✓] {len(email_list)} Unique emails found.")
        if email_list:
            save_csv_separate(email_list, 'email.csv', 'Email')
            print(Fore.CYAN + "[✓] Emails saved in 'email.csv'.")

    # Extract phone numbers
    if mode in ['phone', 'all']:
        phone_list = extract_phone(content)
        print(Fore.GREEN + f"[✓] {len(phone_list)} Unique phone numbers found.")
        if phone_list:
            save_csv_separate(phone_list, 'phone.csv', 'PhoneNr')
            print(Fore.CYAN + "[✓] Phone numbers saved in 'phone.csv'.")

    # Extract IPs
    if mode in ['ip', 'all']:
        ip_list = extract_ip(content)
        print(Fore.GREEN + f"[✓] {len(ip_list)} Unique IP addresses found.")
        if ip_list:
            save_csv_separate(ip_list, 'ip.csv', 'IP')
            print(Fore.CYAN + "[✓] IPs saved in 'ip.csv'.")

    # Extract URLs
    if mode in ['url', 'all']:
        url_list = extract_url(content, links_to_remove)
        print(Fore.GREEN + f"[✓] {len(url_list)} Unique URLs found.")
        if url_list:
            save_csv_separate(url_list, 'urls.csv', 'URL')
            print(Fore.CYAN + "[✓] URLs saved in 'urls.csv'.")

    # Extract URLs with parameters
    if mode in ['urlparams', 'all']:
        url_params_list = extract_url_with_params(content, filters)
        print(Fore.GREEN + f"[✓] {len(url_params_list)} URLs with parameters found.")
        if url_params_list:
            save_csv_separate(url_params_list, 'urls_with_params.csv', 'URLs with Parameters')
            print(Fore.CYAN + "[✓] URLs with parameters saved in 'urls_with_params.csv'.")

    if not (email_list or phone_list or ip_list or url_list or url_params_list):
        print(Fore.YELLOW + "[!] No valid data found!")

def show_help():
    print(Fore.CYAN + """
Usage:
  python metabyte.py -f <file.txt> -m <email|phone|ip|url|urlparams|all> --remove <file_to_remove.txt> [--filter id,token]

Options:
  -f, --file                   Input file to analyze
  -m, --mode                   Mode: email, phone, ip, url, urlparams, all
  --remove                     File containing URLs or keywords to remove, one per line
  --filter                     Comma-separated parameter filters (only for urlparams mode)
  -h, --help                   Show this help message

Description:
  This script extracts emails, phone numbers, IPs and/or URLs from a .txt file,
  removes duplicates and saves each data type in a separate CSV file:
    - email.csv
    - phone.csv
    - ip.csv
    - urls.csv
    - urls_with_params.csv (filtered if --filter used)

Examples:
  - python3 metabyte.py -f emails.txt -m email
  - python3 metabyte.py -f urls.txt -m url --remove remove_links.txt
  - python3 metabyte.py -f urls.txt -m urlparams --filter id,token
  - python3 metabyte.py -f full_data.txt -m all
---------------------------------------------

        \033[91m   ᴹᵉᵗᵃᴮʸᵗᵉ_ⱽ¹ˑ²_ᵇʸ_ˣᴾˡᵒⁱᵗˢ³ᶜ \033[0m\n
\033[93m  [!]GitHub: https://github.com/xPloits3c/MetaByte \033[0m\n
""")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-f', '--file', required=True, help="Input file")
    parser.add_argument('-m', '--mode', required=True, help="Mode: email, phone, ip, url, urlparams, all")
    parser.add_argument('--remove', help="File containing URLs or keywords to remove, one per line")
    parser.add_argument('--filter', help="Filter URLs with specific parameters (e.g., id,token)")
    parser.add_argument('-h', '--help', action='store_true')

    args = parser.parse_args()

    if args.help or not args.file or not args.mode:
        show_help()
    else:
        links_to_remove = load_links_to_remove(args.remove) if args.remove else None
        filters = args.filter.split(",") if args.filter else None
        execute_cleanup(args.file, args.mode.lower(), filters, links_to_remove)
