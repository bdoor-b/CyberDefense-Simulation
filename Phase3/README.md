
# 🛡️ Phase 3: Defensive Strategy Proposal: Using Fail2Ban to Secure SSH

## 🎯 Objective

Secure the SSH service on the victim machine (**Metasploitable3**) by using **Fail2Ban** to detect and block brute-force SSH attacks.

---

## 🔍 Vulnerability Overview

- **Service Targeted**: SSH (Port 22)  
- **Issue**: SSH was accessible using **password authentication**, making it vulnerable to brute-force attacks.
- **Initial Security Posture**: No control in place to block repeated failed login attempts.

![SSH Settings](https://github.com/user-attachments/assets/fec38019-9622-43ca-a7de-4fefcce2ff25)

> Result: SSH allows both `publickey` and `password` authentication.

---

## 🔧 Step-by-Step: Fail2Ban Defense Implementation

### 1️⃣ Install Fail2Ban
```bash
sudo apt install fail2ban -y
```
![Install Fail2Ban](https://github.com/user-attachments/assets/c40cda87-ad96-4d56-ba43-afd5c0a3d07b)

---

### 2️⃣ Copy Default Configuration
```bash
sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local
```
![Copy Config](https://github.com/user-attachments/assets/5c5604fd-eb98-436a-b649-24e8dcd1efc7)

---

### 3️⃣ Configure SSH Jail Settings
```bash
sudo nano /etc/fail2ban/jail.local
```
Edit the `[sshd]` section to enable jail and define settings:

- `enabled = true`
- `port = ssh`
- `filter = sshd`
- `logpath = /var/log/auth.log`
- `maxretry = 6`
- `findtime = 600`
- `bantime = 600`



![Edit Jail](https://github.com/user-attachments/assets/1ea95e03-2603-46a2-81de-123e378aed9c)
![Jail Settings](https://github.com/user-attachments/assets/0c14c455-54f2-45b9-a018-7cdece586a1f)

---

### 4️⃣ Restart and Verify Fail2Ban
```bash
sudo service fail2ban restart
sudo fail2ban-client status
sudo fail2ban-client status sshd
```
![Fail2Ban Status](https://github.com/user-attachments/assets/98a128a1-2069-4a8e-8b7e-970ff1d4cd43)

---

## 🧪 Testing the Defense

### 🔁 Re-launch the Brute-Force Attack

Used the same brute-force script from Phase 1.  
After exceeding `maxretry`, **Fail2Ban** detected the attack and **banned the attacker's IP**.

![Banned IP](https://github.com/user-attachments/assets/010bb864-69a3-44c2-9875-a2986329a03b)

Check status again:


![Fail2Ban Updated Status](https://github.com/user-attachments/assets/62b3ae53-6df2-4842-a9ca-05b508dc953c)

---

### ❌ SSH Access Denied

SSH became inaccessible from the banned attacker's IP, confirming the defense worked as intended.

![SSH Blocked](https://github.com/user-attachments/assets/86263142-1850-4f14-8d5c-05d739f44e50)

---

## ✅ Results Summary

| Phase                  | Description                                | Status      |
|------------------------|--------------------------------------------|-------------|
| Vulnerability Identified | SSH with password login exposed          | ✅ Detected |
| Fail2Ban Installed     | Deployed on Metasploitable3                | ✅ Completed |
| Jail Configured & Active | Monitoring auth.log for failures        | ✅ Completed |
| Attack Simulated Again | IP exceeded retry threshold                | ✅ Triggered |
| IP Successfully Banned | SSH access refused from attacker's IP     | ✅ Verified  |

---

## 📌 Conclusion

By deploying **Fail2Ban**, we successfully protected the SSH service on **Metasploitable3** from brute-force attacks.  
This **reactive control** monitored login attempts and automatically banned malicious IPs, blocking further intrusion attempts.

> ✅ After exceeding the allowed login failures, the attacker’s IP was blocked, fully mitigating the threat.

---
