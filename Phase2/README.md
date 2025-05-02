# ICS344 Project - Phase 2

## Phase 2: Visual Analysis with a SIEM Dashboard

---

## Task: Integrate Logs from Victim Environment into SIEM (Splunk)

### 1. Environment Setup
- **SIEM Tool Used**: Splunk
- **Victim Machine**: Metasploitable3 (IP: `192.168.XX.XX`)
- Logs forwarded via syslog or file monitoring to the Splunk instance.
- Log collection focused on SSH authentication events (e.g., `/var/log/auth.log` or equivalent on Windows if applicable).

**Steps Taken:**
1. Installed and configured Splunk Enterprise on the attacker machine.
2. Set up log forwarding from Metasploitable3 using either:
   - Splunk Universal Forwarder
   - Syslog agent (e.g., rsyslog or nxlog)
3. Verified log ingestion in Splunk.

**Screenshot: Splunk showing logs from victim machine (Metasploitable3)**  

---

## ✅ Task: Visualize Attacks and Analyze Behavior

### 2. Attack Detection and Visualization

**Goal**: Visualize the SSH brute-force login attempts carried out in Phase 1.

### Example Queries Used in Splunk:
```spl
index=* host=metasploitable3 sourcetype=auth
