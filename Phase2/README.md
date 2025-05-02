# ICS344 Project - Phase 2

## Phase 2: Visual Analysis with a SIEM Dashboard

---

## Task1: Integrate Logs from Victim Environment into SIEM (Splunk)

### 1. Environment Setup
- **SIEM Tool Used**: Splunk
- **Victim Machine**: Metasploitable3 (IP: `192.168.100.133`)

**Steps Taken:**
1. Installed and configured Splunk Enterprise on the attacker machine.
2. Set up log forwarding from Metasploitable3 using Splunk Universal Forwarder.
3. Verified log ingestion in Splunk.

**Screenshot: Splunk showing logs from victim machine (Metasploitable3)**  

---

## Task2: Visualize Attacks and Analyze Behavior

### 2. Attack Detection and Visualization


### Example Queries Used in Splunk:
```spl
index=* sourcetype="/var/log/auth.log"
