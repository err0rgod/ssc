# 🔓 SSH-Crack – Multi-Mode SSH Brute Force Tool

> **"Crack SSH credentials with speed, stealth, and smart mutation."**

SSH-Crack is a Python-based SSH credential brute-forcing toolkit featuring **Basic** and **Advanced** modes.  
It is designed for **authorized penetration testing and security auditing** only.

---

## ⚠️ Disclaimer
This tool must only be used on systems you own or have explicit permission to test.  
The author is **not responsible** for any misuse.

---

## ✨ Features

### **Basic Mode (`basic.py`)**
- Targets a **single username** with a password list
- Multi-threaded for faster attacks
- Minimal setup, quick execution

### **Advanced Mode (`adv.py`)**
- Supports **multiple usernames**
- Includes **Smart Mutate** option *(originally developed by err0rgod)*:
  - Applies leetspeak substitutions (`a`→`@`, `i`→`1`, `e`→`3`, etc.)
  - Appends common suffixes (`123`, `!`, `2024`, `@`)
  - Capitalization variations
- Multi-threaded job queue for efficient cracking
- Detects open SSH ports before attempting attacks

---

## 📂 Project Structure

```
ssh-cracker/
├── basic.py       # Basic SSH brute force script
├── adv.py         # Advanced SSH brute force with Smart Mutate
├── user.txt       # Example list of usernames (for testing)
├── pass.txt       # Example list of passwords (for testing)
└── README.md      # You're reading it!
```

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/err0rgod/ssh-cracker.git
   cd ssh-cracker
   ```

2. **Install dependencies**
   ```bash
   pip install paramiko
   ```

3. **Ensure Python 3 is installed**
   ```bash
   python3 --version
   ```

---

## 🚀 Usage

### **Basic Mode**
Brute-force a single SSH username with a password list:
```bash
python3 basic.py -t <target_ip> -u <username> -w pass.txt -c 30
```
**Arguments:**
- `-t` / `--target` → Target hostname/IP
- `-u` / `--user` → Username
- `-w` / `--wordlist` → Path to password list
- `-c` / `--threads` → (Optional) Number of threads (default: 20)

---

### **Advanced Mode**
Brute-force multiple usernames with **Smart Mutate** enabled:
```bash
python3 adv.py -t <target_ip> -u user.txt -p pass.txt --mutate
```
**Arguments:**
- `-t` / `--target` → Target hostname/IP
- `-u` / `--user` → File containing usernames (one per line)
- `-p` / `--passwd` → Path to password list
- `-m` / `--mutate` → Enable Smart Mutate mode

---

## 🔍 Example

```bash
# Basic mode
python3 basic.py -t 192.168.1.10 -u admin -w pass.txt

# Advanced mode with Smart Mutate
python3 adv.py -t 192.168.1.10 -u user.txt -p pass.txt --mutate
```

**Sample Output:**
```
✅ SUCCESS 🎉 admin : P@ssw0rd123
```

---

## 🧠 Smart Mutate Feature
The Smart Mutate feature, **originally developed by err0rgod**, automatically expands the password list by:
- Applying **leet substitutions** (`a`→`@`, `o`→`0`, `s`→`$`, etc.)
- Adding **common suffixes** (`123`, `2024`, `!`, `@`)
- Generating capitalization variations

This increases the probability of cracking weakly modified passwords without requiring an enormous wordlist.

---

## 📜 License
Released under the **MIT License**.

---

## 👤 Author
**err0rgod** – [GitHub Profile](https://github.com/err0rgod)  
10x Dev | IoT Hacker | Malware Dev | Red Teamer | Python/C/C++ | AI/ML | IoT | Robotics
