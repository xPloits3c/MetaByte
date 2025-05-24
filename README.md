# MetaByte
Clean and Save Unique: URL’s-Email-Phone-IP’s.

 ![Repo View Counter](https://profile-counter.glitch.me/MetaByte/count.svg)
 
MetaByte is an advanced parsing script for extracting and removing duplicate.

Supports **emails**, **phone numbers**, **IPs**, and **URLs** detection, with automatic duplicate removal and saving to CSV files.

![image](https://github.com/user-attachments/assets/6ea17898-c5f0-44e4-9b8f-c34140ad4bbb)

---

## Features

> Automatic extraction of:
- Emails
- Phone numbers
- IP addresses (IPv4)
- Full URLs (HTTP/HTTPS)
- Duplicate removal for each data type
- Save results to separate CSVs
- Support for multiple modes (`email`, `phone`, `ip`, `url`, `all`)

---

![results_all](https://github.com/user-attachments/assets/7f1366bd-c5b5-4489-8149-b76c9a8bcaf2)

## Installation
   ```bash
   git clone https://github.com/xPloits3c/MetaByte.git
   cd MetaByte
   pip install -r requirements.txt
```

## Usage

python3 metabyte.py -f <file.txt> -m <mode>

Available modes:

+  email – Extracts email addresses only
+  phone – Extracts phone numbers only
+ ip – Extracts IP addresses only
+ url – Extracts URLs only
+ urlparams - With Params Only
+ all – Extracts everything

## Examples

+ python3 metabyte.py -f emails.txt -m email
+ python3 metabyte.py -f atomicurls.txt -m url
+ python3 metabyte.py -f mixdata.csv -m all
+ python3 metabyte.py -f urls.txt -m urlparams --filter id,token
- ES: `python3 metabyte.py -f urls.txt -m urlparams --filter .php?id`
  
![mb_h](https://github.com/user-attachments/assets/450329e5-9cf8-4844-9f27-992293dbe7b4)

## Output

Data automatically saved to CSV files:
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

