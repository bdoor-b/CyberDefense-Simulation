##  Task 1: Integrate Logs from Victim Environment into SIEM (Splunk)

### Environment Setup

| Component        | Details                             |
| ---------------- | ----------------------------------- |
| SIEM Tool        | Splunk Enterprise                   |
| Victim Machine   | Metasploitable3 (`192.168.100.133`) |
| Attacker Machine | Kali Linux (hosting Splunk server)  |

---

###  Setup Steps

1. **Installed Splunk Enterprise** on the attacker machine.
2. **Installed Splunk Universal Forwarder** on the victim machine (Metasploitable3).
3. **Configured log forwarding** of `/var/log/auth.log` using:
Connect Forwarder to Splunk Server:
   ```
   sudo /opt/splunkforwarder/bin/splunk add forward-server 192.168.100.133:9997
   ```
   Add Data Inputs (Log Files):
   ```
   sudo /opt/splunkforwarder/bin/splunk add monitor /var/log/auth.log
   
   ```
4. **Verified forwarding is active:**

   ```
   sudo /opt/splunkforwarder/bin/splunk list forward-server
   ```

### Forwarder Integration Confirmation
This output confirms that logs from the victim are actively being forwarded to the Splunk SIEM on port `9997`
![لقطة شاشة 2025-05-02 175135](https://github.com/user-attachments/assets/953d7e91-b8bc-4435-838b-20316ae999cb)




---

### Screenshot 2 – Raw Log Events from /var/log/auth.log
Log data from the victim successfully appears in Splunk, including authentication attempts, confirming full log integration.

![لقطة شاشة 2025-05-02 173814](https://github.com/user-attachments/assets/c7ed600d-5ecf-4fdd-a69c-0f6a9b0642fc)



![لقطة شاشة 2025-05-02 173849](https://github.com/user-attachments/assets/6d68e6c5-78f9-4834-a68c-d8f63c91cce0)

---

## Task 2: Visualize Attacks and Analyze Behavior

### Attack Overview

The victim (Metasploitable3) was subjected to a brute-force SSH attack using a custom Python script. The attack attempted multiple username-password combinations until access was gained.

---

### Detection and Analysis

#### Splunk Search Query Used:

```spl
index=* source="/var/log/auth.log" ("Failed password" OR "Accepted password")
```
![لقطة شاشة 2025-05-02 183845](https://github.com/user-attachments/assets/7722c254-c7db-473a-ba27-98d94314fde5)

---

### Screenshot 3 – Brute-force Attempt Visualization
Shows multiple `Failed password` attempts and one successful `Accepted password` for user `vagrant`, confirming the brute-force succeeded.


![لقطة شاشة 2025-05-02 183908](https://github.com/user-attachments/assets/cb5f8abe-561a-40a4-af00-8e7fa2ad7a4d)


---

### 🔐 Post-Exploitation Behavior

After successful SSH access, the attacker escalated privileges using `sudo` to run administrative commands.

####  Screenshot 4 – `sudo` Log Entry (Privilege Escalation)

The attacker used `sudo` to execute a command with root access, indicating post-exploitation actions.

---

### 🕒 Session Analysis

Splunk also captured session opening and closing events, allowing timeline analysis of attacker behavior.

#### 📸 Screenshot 5 – Session Events

![Screenshot 5](./screenshots/session-logs.png)

> These entries show the timeline of the `vagrant` user session and actions performed as root.

---

### 🔄 Full Log Timeline from Victim

Additional queries helped track session transitions, `cron` jobs, and all relevant `auth.log` entries.

#### 📸 Screenshot 6 – Full Auth Log Timeline View

![Screenshot 6](./screenshots/full-auth-log.png)

> A broader view of system activity and authentication logs captured via `/var/log/auth.log`.

---

## 📈 Summary of Achievements

| Deliverable                              | Status      |
| ---------------------------------------- | ----------- |
| SIEM installed and configured            | ✅ Completed |
| Log forwarding from victim               | ✅ Completed |
| Brute-force attack executed and detected | ✅ Completed |
| Post-exploitation behavior visualized    | ✅ Completed |
| Splunk dashboard used for analysis       | ✅ Completed |

---

## 📌 Conclusion

Through this simulation, we successfully demonstrated the power of SIEM tools like Splunk in detecting and analyzing cyberattacks. The integration of system logs from Metasploitable3 enabled full visibility into brute-force login attempts and privilege escalation activity.

Splunk allowed us to track attacker behavior in real-time, from initial login attempts to successful compromise and root access. These insights are critical in real-world cybersecurity monitoring and response.

---

## 🧾 Appendix: Query Reference

```spl
index=* source="/var/log/auth.log" ("Failed password" OR "Accepted password")
index=* source="/var/log/auth.log" sudo
index=* source="/var/log/auth.log" session
```

---

Would you like this report exported as a **Word, PDF, or Markdown file** with all the screenshots embedded? I can generate and format it for you.
