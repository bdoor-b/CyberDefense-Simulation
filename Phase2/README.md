# Phase 2: Visual Analysis with a SIEM Dashboard

##  Task 1: Integrate Logs from Victim Environment into SIEM (Splunk)

### Environment Setup

| Component        | Details                             |
| ---------------- | ----------------------------------- |
| SIEM Tool        | Splunk Enterprise                   |
| Victim Machine   | Metasploitable3 (`192.168.100.138`) |
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

###  Raw Log Events from /var/log/auth.log
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

```
index=* source="/var/log/auth.log" ("Failed password" OR "Accepted password")
```
![لقطة شاشة 2025-05-02 183845](https://github.com/user-attachments/assets/7722c254-c7db-473a-ba27-98d94314fde5)

---

### Brute-force Attempt Visualization
Here we can notice multiple `Failed password` attempts and one successful `Accepted password` for user `vagrant`, confirming the brute-force succeeded.


![لقطة شاشة 2025-05-02 183908](https://github.com/user-attachments/assets/cb5f8abe-561a-40a4-af00-8e7fa2ad7a4d)


---
### Additional Visual Analysis
To gain deeper insights, we broke down the SSH authentication events into separate visualizations:



**Accepted SSH Logins Over Time**
As shown in the picture, we use the query: 
```
index=* source="/var/log/auth.log" ("Accepted password") | timechart count

```

![PHOTO-2025-05-03-20-37-17 2](https://github.com/user-attachments/assets/ec9238b9-5f53-4edc-950b-116e13b74be1)
 >This visualization shows 4 successful login events, all occurring on May 2, 2025. 

**Failed SSH Logins Over Time**
As shown in the picture, we use the query: 
```
index=* source="/var/log/auth.log" ("Failed password") | timechart count
```
![PHOTO-2025-05-03-20-37-17 3](https://github.com/user-attachments/assets/29f140f0-73a7-46f3-b558-78fc892c4280)
 >The chart reveals a noticeable increase in failed login attempts on May 2, 2025.


**Failed Login Attempts by Host**
As shown in the picture, we use the query: 
```
index=* source="/var/log/auth.log" ("Failed password") | stats count by host
```
![PHOTO-2025-05-03-20-37-17](https://github.com/user-attachments/assets/18b88520-bef4-4cd2-b7e2-d8a7bb82d7e8)
 >A total of 31 failed login attempts were recorded on the host metasploitable3, confirming it was the primary target of the brute-force attack.



## Conclusion

Through this simulation, we successfully demonstrated the power of SIEM tools like Splunk in detecting and analyzing cyberattacks. The integration of system logs from Metasploitable3 enabled full visibility into brute-force login attempts and privilege escalation activity.

Splunk allowed us to track attacker behavior in real-time, from initial login attempts to successful compromise and root access. These insights are critical in real-world cybersecurity monitoring and response.

---
