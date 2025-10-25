# Socket & Port Scanner

**Description**  
This repository contains a simple threaded TCP server (`server.py`), a TCP client (`client.py`), and an educational TCP port scanner (`port_scanner.py`) created for my course midterm. The purpose of this project is to demonstrate socket programming, connection handling, input validation, and ethical port scanning practices.

---

## Files in this repository
- `server.py` — Threaded echo server (Python).  
- `client.py` — Simple TCP client for sending messages.  
- `port_scanner.py` — Educational TCP port scanner (whitelisted targets only).  
- `README.md` — This file.  
- `screenshots/` — Folder containing terminal screenshots demonstrating tests.

---

## Requirements
- Python 3.11.4+ (recommended)
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

## Screenshots 

1. `1_Terminals.png` 
2. `2_Error_Correction.png`
3. `3_Error_Mgmt.png`  
4. `4_Ports_Closed.png`  
5. `5_Open_Port_135.png`  
6. `6_Approved_Nmap_Scan.png` 
7. `7_Nmap_1-200_Scan.png`  
8. `8_Nmap_1-200_Scan_Part2.png`  
9. `9_Invalid_Ports.png`  
10. `10_Bad_Range.png`  
11. `11_Unauthorized_Target.png`

---

## Example git commands (one-time setup + push)
```powershell
cd C:\Users\<you>\OneDrive\Desktop\crispy-train

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

## Citation (for reflection / references)
Lyon, G. F. (2009). *Nmap Network Scanning: The Official Nmap Project Guide to Network Discovery and Security Scanning* (1st ed.). Insecure.Com LLC.

---

## Contact
If you have questions about the code or tests, message me.
