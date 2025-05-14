# MetaByte
Clean and Save Unique: URL’s-Email-Phone-IP’s.

 ![Repo View Counter](https://profile-counter.glitch.me/MetaByte/count.svg)
 
[+] MetaByte is an advanced parsing script for extracting, cleaning and saving sensitive information from `.txt` files.

[+] Supports **emails**, **phone numbers**, **IPs**, and **URLs** detection, with automatic duplicate removal and saving to CSV files.

![image](https://github.com/user-attachments/assets/6ea17898-c5f0-44e4-9b8f-c34140ad4bbb)

---

## Features

- Automatic extraction of:
- Emails
- Phone numbers
- IP addresses (IPv4)
- Full URLs (HTTP/HTTPS)
- Duplicate removal for each data type
- Save results to separate CSVs
- Support for multiple modes (`email`, `phone`, `ip`, `url`, `all`)

---

## Installation
   ```bash
   git clone https://github.com/xPloits3c/MetaByte.git
   pip install -r requirements.txt
   cd MetaByte
```

## Usage

python3 metabyte.py -f <file.txt> -m <mode>

Available modes:

+  email – Extracts email addresses only
+  phone – Extracts phone numbers only
+ ip – Extracts IP addresses only
+ url – Extracts URLs only
+ all – Extracts everything

## Examples

+ python metabyte.py -f emails.txt -m email
+ python metabyte.py -f atomicurls.txt -m url
+ python metabyte.py -f mixeddata.txt -m all
  
![image](https://github.com/user-attachments/assets/7b7fba9e-cf5c-4450-aa97-13ee98916139)

## Output

Data automatically saved to CSV files:s
+ email.csv
+ phone.csv
+ ip.csv
+ urls.csv

## Credits
+ Developed by: xPloits3c
+ GitHub: https://github.com/xPloits3c/MetaByte
+ Version: 1.0
+ License: MIT

## TODO (future ideas)
+ IPv6 support
+ JSON export
+ Graphical user interface (GUI)
+ Automatic scanning from folders

