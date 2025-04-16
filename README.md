# Python Bind Shell Listener

This repository contains a simple Python-based bind shell designed for **educational use only**. It listens on a specified TCP port and allows remote users to connect and obtain an interactive shell on the host system via a specified port. 

To run the script, execute the following command:

`python3 bind_shell.py`

Once the script is running, a remote user can connect using:

`nc <target_ip> 18252`

Ensure that port `18252` is open on the target system and that any firewalls are properly configured to allow incoming connections.

This script listens on TCP port `18252` and spawns a Bash shell for any client that connects, using a pseudo-terminal for full interactivity. It also disables bash history by setting `HISTFILE` to `/dev/null`, making it harder to detect in logs. 

Key Features:
- Binds to a local port and waits for incoming connections.
- Provides an interactive Bash shell using `pty.spawn()`.
- Disables bash history for stealth by setting `HISTFILE` to `/dev/null`.
- Forks child processes to handle multiple incoming connections.
- Written in Python 3.

## ⚠️ Custom Disclaimer

This repository is **for educational purposes only**. Use this code only in environments where you have explicit permission, such as for **penetration testing**, **capture the flag (CTF)** challenges, or **red teaming** exercises.

Unauthorized use of this code is illegal and unethical. The author is **not responsible** for any misuse of this code, and by using it, you agree to assume all risks associated with its use.

Do not deploy this code on systems or networks you do not own or have explicit authorization to test.

## 📄 License

This project is not licensed for general open-source use. By downloading or using this code, you agree to the terms of the **Custom Disclaimer** above.

## GitHub Repo Description

**Educational Python Bind Shell** — For use only in authorized, controlled environments (e.g., CTF, red team testing). Unauthorized use is illegal. Use at your own risk.
