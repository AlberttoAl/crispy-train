# Socket & Port Scanner — Midterm

**Description**  
This repository contains a simple threaded TCP server (`server.py`), a TCP client (`client.py`), and an educational TCP port scanner (`port_scanner.py`) created for a course midterm. The purpose of this project is to demonstrate socket programming, connection handling, input validation, and ethical port scanning practices.

---

## Files in this repository
- `server.py` — Threaded echo server (Python).  
- `client.py` — Simple TCP client for sending messages.  
- `port_scanner.py` — Educational TCP port scanner (whitelisted targets only).  
- `README.md` — This file.  
- `Socket_Port_Scanner_APA_Final.docx` — (optional) APA-formatted lab report.  
- `screenshots/` — (recommended) Folder containing terminal screenshots demonstrating tests.

---

## Requirements
- Python 3.9+ (3.11 recommended)
- Windows 10/11 (tested), PowerShell (or macOS/Linux Terminal)
- No external Python packages required

---

## Quick start / Usage examples

1. Run the server (Terminal A):
```powershell
cd C:\Users\<you>\OneDrive\Documents\Socket_Scanner
python server.py --host 127.0.0.1 --port 5000
```

2. Run the client (Terminal B):
```powershell
python client.py --host 127.0.0.1 --port 5000 --message "Hello from client"
```

3. Run the scanner (localhost common ports):
```powershell
python port_scanner.py --target 127.0.0.1 --ports 21,22,80,443
```

4. Run the scanner (port range):
```powershell
python port_scanner.py --target localhost --range 1-200
```

5. Authorized external scan (gentle; only for course testing):
```powershell
python port_scanner.py --target scanme.nmap.org --ports 22,80,443 --delay 0.1
```

---

## Important ethical & legal notice (READ THIS)
**Only** scan hosts you own or have explicit permission to scan. For this assignment, allowed targets are:
- `localhost` (127.0.0.1)
- `scanme.nmap.org` (authorized test host)

Do **not** run the scanner against any other IP/host. Aggressive scanning or scanning without permission may be illegal.

---

## Port scanner features & safeguards
- Accepts a comma-separated list of ports (`--ports 22,80`) or a range (`--range 1-1024`).
- Enforces a whitelist of allowed targets to prevent misuse.
- Validates inputs (port ranges and numbers) and shows helpful error messages.
- Configurable per-port timeout (`--timeout`) and delay between probes (`--delay`) to reduce load.

---

## Test checklist (include screenshots in `screenshots/` folder)
Capture and store the following images (with visible timestamps) and include them in your submission:

1. `01_server_listening.png` — server listening message.  
2. `02_client_success.png` — client connected & received response.  
3. `03_server_received.png` — server log showing received client message.  
4. `04_server_shutdown.png` — server graceful shutdown (Ctrl+C).  
5. `05_client_connection_refused.png` — client run when server is down (connection refused).  
6. `06_scanner_local_common.png` — scanner output for ports 21,22,80,443 on localhost.  
7. `07_scanner_local_range.png` — scanner output for range 1–200 (can be split).  
8. `08_scanner_scanme.png` — authorized scan of scanme.nmap.org.  
9. `09_scanner_invalid_ports.png` — invalid ports input error.  
10. `10_scanner_bad_range.png` — reversed/bad range input error.  
11. `11_scanner_unauthorized.png` — scanner refusing unauthorized target.

---

## Example git commands (one-time setup + push)
```powershell
cd C:\Users\<you>\OneDrive\Documents\Socket_Scanner

# initialize if needed
git init
git add .
git commit -m "Midterm: add server, client, port scanner, README, screenshots"
git branch -M main
git remote add origin https://github.com/YourUsername/socket-scanner-midterm.git
git push -u origin main
```
If prompted for credentials, use your GitHub username and a Personal Access Token (PAT) if required.

---

## Troubleshooting
- `python: command not found` — ensure Python is installed and added to PATH.
- `Connection refused` — confirm the server is running and firewall rules allow localhost connections.
- `scanme.nmap.org` resolution fails — check DNS/network connectivity; capture the error for documentation.

---

## Suggested submission text (copy to your assignment)
> Repository: `https://github.com/YourUsername/socket-scanner-midterm`  
> The repo contains `server.py`, `client.py`, `port_scanner.py`, an APA-format lab report, and screenshots demonstrating successful and unsuccessful connection tests and scanner output (timestamps included). All scans were limited to authorized targets.

---

## Citation (for reflection / references)
Lyon, G. F. (2009). *Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Security Scanning* (1st ed.). Insecure.Com LLC.

---

## Contact
If you have questions about the code or tests, email: your-email@example.com
