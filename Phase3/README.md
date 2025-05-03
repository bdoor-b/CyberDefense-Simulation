Step 1: Change SSH Configuration

1️⃣ Using Nmap to Verify Security Status (Before)

Nmap scan confirms that both password and publickey authentication methods were supported.
![1](https://github.com/user-attachments/assets/31e32c09-a641-4bf1-b742-6dad7ff8210f)

2️⃣ SSH Connection Works (Before Defense)

Successful SSH login using valid credentials (vagrant:vagrant)

![2](https://github.com/user-attachments/assets/a75b5e34-fda2-4a7a-8ddf-0604d3a3752d)

3️⃣ Open SSH Configuration File

Edited using sudo nano /etc/ssh/sshd_config

![3](https://github.com/user-attachments/assets/9e2b070b-3fa2-49dc-b1ca-2a73d0e7c68d)

4️⃣ Check for PasswordAuthentication Line

Located the line PasswordAuthentication yes

![4](https://github.com/user-attachments/assets/788078d5-a8cb-4acf-9064-756a6b6c854a)
![5](https://github.com/user-attachments/assets/4c3c046d-b5ff-4647-bc71-82d61214a07b)


5️⃣ Disable PasswordAuthentication

Changed setting to no

![6](https://github.com/user-attachments/assets/115c9cc0-e22b-429b-9306-b5f5cccc0222)


6️⃣ Restart SSH Service

Applied changes by restarting SSH

 ![7](https://github.com/user-attachments/assets/985473c7-8af1-4888-b2b4-95be7a6c25b7)

7️⃣ Confirm PublicKeyAuthentication is Enabled

![8](https://github.com/user-attachments/assets/b98d056d-47b0-4227-9191-acd784cba849)

8️⃣ Validate Changes with Nmap

Nmap confirms only publickey is supported now
![9-2](https://github.com/user-attachments/assets/13cd12b9-29a8-4d9f-a834-4bbcbcbe660c)


9️⃣ Confirmed SSH Rejects Password Logins

Even correct credentials are rejected after password login is disabled

📸 8 we got failed even though it used the correct username and password (vagrant).png
📸 10 we can see clearly that PasswordAuthentication no.png
📸 8 confirms that password authentication is disabled, and only key-based logins are allowed.png

✅ Result: Password-based brute force attacks are no longer effective.

🛡️ Step 2: Fail2Ban Deployment

1️⃣ Scan Before Fail2Ban

Nmap reveals open services including SSH

📸 1 using nmap to verify security status BEFORE.png

2️⃣ Install Fail2Ban

Installed via sudo apt install fail2ban -y

📸 2 installing fail2ban.png

3️⃣ Copy Default Config & Edit jail.local

Used nano to configure jail settings

📸 3 Copy Default Configuration.png
📸 4 after running nano.png

4️⃣ Apply Filter and Ban Settings

[sshd]
enabled = true
port = ssh
filter = sshd
logpath = /var/log/auth.log
maxretry = 6
findtime = 600
bantime = 600

📸 5 ensure that it is enabled and added findtime and bantime=10 min.png

5️⃣ Restart and Verify Functionality

📸 6 restarting and checking everything works.png

6️⃣ Simulate Attack

Re-executed brute-force attack from Phase 1

📸 7 attacking using the attack from phase 1.png

7️⃣ Attacker Banned

Fail2Ban detected the failed logins and banned the attacker's IP

📸 8 it banned kali ip address.png

8️⃣ SSH No Longer Accessible from Banned Host

📸 9 ssh port is no longer accessable.png

✅ Result: Brute-force attempts are blocked after exceeding max retries.

✅ Results Summary

Phase

Objective

Status

SSH Configuration Hardening

Disabled password-based logins

✅ Success

Fail2Ban Setup

Block repeated brute-force attempts

✅ Success

After Attack Retest

Attacker blocked or denied

✅ Success

📌 Conclusion

This phase demonstrated two layered defenses:

Hardening SSH Configuration to eliminate password-based authentication.

Deploying Fail2Ban to dynamically block attackers based on failed login attempts.

Together, these defenses achieved complete mitigation of the brute-force vulnerability, satisfying all project deliverables with clear before-and-after evidence.
