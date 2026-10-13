# MetaByte

**Clean and save unique URLs, emails, phone numbers and IPs.**

MetaByte is a fast parsing script that extracts **emails**, **phone numbers**, **IPv4 addresses** and **URLs** from any text file, removes duplicates automatically and saves each data type in its own CSV file.

![image](https://github.com/user-attachments/assets/6ea17898-c5f0-44e4-9b8f-c34140ad4bbb)

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modes](#modes)
- [Options](#options)
- [Examples](#examples)
- [Output](#output)
- [Credits](#credits)
- [Roadmap](#roadmap)

---

## Features

- Automatic extraction of:
  - Emails
  - Phone numbers
  - IP addresses (IPv4, octets validated 0-255)
  - Full URLs (HTTP/HTTPS)
  - Full URLs with parameters, e.g. `id=1`, `.php?catid=`
- Duplicate removal for every data type
- **Link removal**: exclude unwanted sites or keywords (e.g. `google.com`, `bing.com`) using a blacklist file
- Parameter filter for URLs (`--filter id,token`)
- Results saved to separate CSV files
- Multiple modes: `email`, `phone`, `ip`, `url`, `urlparams`, `all`

![results_all](https://github.com/user-attachments/assets/7f1366bd-c5b5-4489-8149-b76c9a8bcaf2)

---

## Installation

```bash
git clone https://github.com/xPloits3c/MetaByte.git
cd MetaByte
pip install -r requirements.txt
```

Requires Python 3 and `colorama`.

---

## Usage

```bash
python3 metabyte.py -f <file.txt> -m <mode> [--remove <blacklist.txt>] [--filter <params>]
```

### Modes

| Mode        | Description                                |
|-------------|--------------------------------------------|
| `email`     | Extracts email addresses only              |
| `phone`     | Extracts phone numbers only                |
| `ip`        | Extracts IP addresses only                 |
| `url`       | Extracts URLs only                         |
| `urlparams` | Extracts URLs with parameters only         |
| `all`       | Extracts everything                        |

### Options

| Option             | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| `-f`, `--file`     | Input file to analyze                                                       |
| `-m`, `--mode`     | Extraction mode (see table above)                                           |
| `--remove`         | Text file with URLs or keywords to remove, **one per line** (`url` mode)    |
| `--filter`         | Comma-separated parameter filters (`urlparams` mode), e.g. `id,token`       |
| `-h`, `--help`     | Show the help message                                                       |

### Removing unwanted links

Create a text file with one URL or keyword per line:

```text
google.com
bing.com
youtube.com
```

Any extracted URL containing one of these entries is discarded:

```bash
python3 metabyte.py -f urls.txt -m url --remove remove_links.txt
```

---

## Examples

```bash
# Emails only
python3 metabyte.py -f emails.txt -m email

# URLs only
python3 metabyte.py -f atomicurls.txt -m url

# URLs, excluding the sites listed in remove_links.txt
python3 metabyte.py -f urls.txt -m url --remove remove_links.txt

# URLs with parameters, filtered by parameter name
python3 metabyte.py -f urls.txt -m urlparams --filter id,token

# Example with a PHP pattern
python3 metabyte.py -f urls.txt -m urlparams --filter .php?id

# Everything
python3 metabyte.py -f mixdata.csv -m all
```

![mb_h](https://github.com/user-attachments/assets/450329e5-9cf8-4844-9f27-992293dbe7b4)

---

## Output

Data is automatically saved to CSV files in the current directory:

| File                   | Content                          |
|------------------------|----------------------------------|
| `email.csv`            | Unique emails                    |
| `phone.csv`            | Unique phone numbers             |
| `ip.csv`               | Unique IPv4 addresses            |
| `urls.csv`             | Unique URLs                      |
| `urls_with_params.csv` | Unique URLs with parameters      |

---

## Credits

- **Developed by:** xPloits3c
- **GitHub:** https://github.com/xPloits3c/MetaByte
- **Contact:** whitehat.report@onionmail.org
- **Version:** 1.2
- **License:** MIT

---

## Roadmap

- [ ] IPv6 support
- [ ] JSON export
- [ ] Graphical user interface (GUI)
- [ ] Automatic scanning from folders
