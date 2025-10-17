#!/usr/bin/env python3
"""
port_scanner.py — Midterm Part 2 port scanner (safe & respectful)

Authorized targets for this assignment:
  - localhost / 127.0.0.1
  - scanme.nmap.org

Features:
- Scan specific ports (--ports "22,80,443") OR a range (--range "1-1024")
- Timeout and optional delay between connection attempts
- Input validation and useful error messages
- Clear, timestamped output
- Refuses to scan unauthorized targets to help you comply with course rules

Usage examples:
  # Common ports on localhost
  python port_scanner.py --target 127.0.0.1 --ports 21,22,80,443

  # Range on localhost
  python port_scanner.py --target localhost --range 1-200

  # Limited demo on scanme.nmap.org with gentle pacing:
  python port_scanner.py --target scanme.nmap.org --ports 22,80,443 --delay 0.1
"""
import argparse
import socket
import time
import datetime
from typing import List

AUTHORIZED_HOSTS = {"127.0.0.1", "localhost", "scanme.nmap.org"}

def ts() -> str:
    return datetime.datetime.now().isoformat(timespec="seconds")

def parse_ports_list(text: str) -> List[int]:
    ports = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if not part.isdigit():
            raise ValueError(f"Invalid port '{part}'. Use commas, e.g., 22,80,443")
        p = int(part)
        if not (1 <= p <= 65535):
            raise ValueError(f"Port out of range: {p} (valid 1-65535)")
        ports.append(p)
    if not ports:
        raise ValueError("No valid ports provided")
    return ports

def parse_range(text: str) -> List[int]:
    try:
        start_s, end_s = [t.strip() for t in text.split("-", 1)]
        start, end = int(start_s), int(end_s)
    except Exception:
        raise ValueError("Range must look like '1-1024'")
    if start > end:
        raise ValueError("Range start must be <= end")
    if not (1 <= start <= 65535 and 1 <= end <= 65535):
        raise ValueError("Ports must be between 1 and 65535")
    # Bound size to something reasonable for class demo
    if end - start + 1 > 5000:
        raise ValueError("Range too large for demo (max 5000 ports at once)")
    return list(range(start, end + 1))

def resolve_host(target: str) -> str:
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror as e:
        raise ValueError(f"Cannot resolve host '{target}': {e}")

def scan_port(ip: str, port: int, timeout: float) -> bool:
    """Return True if port is open, False otherwise."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            result = s.connect_ex((ip, port))
            return result == 0
        except Exception:
            return False

def main():
    parser = argparse.ArgumentParser(description="Educational TCP port scanner")
    parser.add_argument("--target", required=True, help="Target hostname or IP (localhost, 127.0.0.1, scanme.nmap.org)")
    parser.add_argument("--ports", help="Comma-separated ports, e.g., 22,80,443")
    parser.add_argument("--range", help="Port range, e.g., 1-1024")
    parser.add_argument("--timeout", type=float, default=0.5, help="Per-port timeout seconds (default: 0.5)")
    parser.add_argument("--delay", type=float, default=0.0, help="Delay between ports in seconds (default: 0.0)")
    args = parser.parse_args()

    # Enforce authorized targets
    if args.target not in AUTHORIZED_HOSTS:
        print(f"[{ts()}] Refusing to scan unauthorized target '{args.target}'.")
        print(f"[{ts()}] Allowed: localhost, 127.0.0.1, scanme.nmap.org")
        return

    # Build port list
    try:
        if args.ports and args.range:
            raise ValueError("Specify either --ports or --range, not both")
        if args.ports:
            port_list = parse_ports_list(args.ports)
        elif args.range:
            port_list = parse_range(args.range)
        else:
            # Default to a few common ports
            port_list = [21, 22, 80, 443]
    except ValueError as e:
        print(f"[{ts()}] Input error: {e}")
        return

    try:
        ip = resolve_host(args.target)
    except ValueError as e:
        print(f"[{ts()}] Host error: {e}")
        return

    print(f"[{ts()}] Starting scan of {args.target} ({ip})")
    print(f"[{ts()}] Ports: {port_list}  | timeout={args.timeout}s | delay={args.delay}s")
    open_ports: List[int] = []
    for p in port_list:
        is_open = scan_port(ip, p, timeout=args.timeout)
        status = "OPEN" if is_open else "closed"
        print(f"[{ts()}] Port {p:>5}: {status}")
        if is_open:
            open_ports.append(p)
        if args.delay > 0:
            time.sleep(args.delay)
    print(f"[{ts()}] Scan complete. Open ports: {open_ports if open_ports else 'None detected'}")

if __name__ == "__main__":
    main()
