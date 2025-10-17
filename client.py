#!/usr/bin/env python3
"""
client.py — Simple client for midterm Part 1

Usage examples:
  python client.py --host 127.0.0.1 --port 5000 --message "Hello, server!"
  python client.py --host 127.0.0.1 --port 5000        # will prompt for message
"""
import argparse
import socket
import datetime

def ts() -> str:
    return datetime.datetime.now().isoformat(timespec="seconds")

def main():
    parser = argparse.ArgumentParser(description="Simple TCP client")
    parser.add_argument("--host", default="127.0.0.1", help="Server host/IP (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5000, help="Server port (default: 5000)")
    parser.add_argument("--message", help="Message to send (if omitted, you will be prompted)")
    parser.add_argument("--timeout", type=float, default=5.0, help="Connection timeout seconds (default: 5)")
    args = parser.parse_args()

    msg = args.message or input("Enter a message to send: ")

    try:
        with socket.create_connection((args.host, args.port), timeout=args.timeout) as sock:
            print(f"[{ts()}] Connected to {args.host}:{args.port}")
            sock.sendall(msg.encode())
            data = sock.recv(1024)
            print(f"[{ts()}] Received: {data.decode(errors='replace')}")
    except (ConnectionRefusedError, TimeoutError, socket.timeout) as e:
        print(f"[{ts()}] Could not connect to {args.host}:{args.port}: {e}")
    except Exception as e:
        print(f"[{ts()}] Unexpected error: {e}")
    finally:
        print(f"[{ts()}] Client exiting")

if __name__ == "__main__":
    main()
