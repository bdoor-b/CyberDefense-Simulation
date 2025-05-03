**Defensive Strategy Proposal: Using Fail2Ban to Secure SSH**

 Objective

To secure the SSH service on the victim machine (Metasploitable3) by using Fail2Ban as a defensive mechanism to detect and block brute-force SSH attacks.

 Vulnerability Overview

Service Targeted: SSH (port 22)

Issue: SSH was accessible using password authentication, making it vulnerable to brute-force attacks.

Initial Security Posture: No controls in place to block repeated failed login attempts.
![1](https://github.com/user-attachments/assets/fec38019-9622-43ca-a7de-4fefcce2ff25)


Result: SSH allows publickey and password authentication.

🔧 Step-by-Step: Fail2Ban Defense Implementation

1️⃣ Install Fail2Ban

sudo apt install fail2ban -y
![2](https://github.com/user-attachments/assets/c40cda87-ad96-4d56-ba43-afd5c0a3d07b)


2️⃣ Copy Default Configuration

sudo cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local

![4](https://github.com/user-attachments/assets/5c5604fd-eb98-436a-b649-24e8dcd1efc7)


3️⃣ Configure SSH Jail Settings

File: /etc/fail2ban/jail.local

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 6
findtime = 600
bantime = 600
![5](https://github.com/user-attachments/assets/1ea95e03-2603-46a2-81de-123e378aed9c)


![6](https://github.com/user-attachments/assets/0c14c455-54f2-45b9-a018-7cdece586a1f)


4️⃣ Restart and Verify Fail2Ban

sudo service fail2ban restart
sudo fail2ban-client status
sudo fail2ban-client status sshd
![7](https://github.com/user-attachments/assets/98a128a1-2069-4a8e-8b7e-970ff1d4cd43)


🧪 Testing the Defense

🔁 Re-launch the Attack

The same brute-force script from Phase 1 was re-executed.

After several failed attempts, Fail2Ban detected and banned the attacker's IP.
![8](https://github.com/user-attachments/assets/010bb864-69a3-44c2-9875-a2986329a03b)


![9](https://github.com/user-attachments/assets/62b3ae53-6df2-4842-a9ca-05b508dc953c)


❌ SSH Access Denied After Ban

SSH port becomes inaccessible from the attacker’s IP.

Confirms that Fail2Ban actively blocked the brute-force attempt.

![10](https://github.com/user-attachments/assets/86263142-1850-4f14-8d5c-05d739f44e50)

✅ Results Summary

Phase

Description

Status

Vulnerability Identified

SSH with password login exposed

✅ Detected

Fail2Ban Installed

Deployed on Metasploitable3

✅ Done

Jail Configured & Active

Monitoring auth.log and banning on failures

✅ Done

Attack Simulated Again

IP exceeded retry threshold

✅ Done

IP Successfully Banned

SSH refused connection

✅ Verified

📌 Conclusion

By deploying Fail2Ban, we successfully protected the SSH service on Metasploitable3 from brute-force attacks. This reactive security control monitors login attempts and automatically bans malicious IPs, preventing further intrusion attempts.

The test results clearly show that after exceeding the allowed login failures, the attacker's IP was banned and SSH access was blocked — fully mitigating the threat.
