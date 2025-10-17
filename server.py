#!/usr/bin/env python3
"""
server.py — Simple threaded echo server for midterm Part 1

Usage:
  python server.py --host 127.0.0.1 --port 5000

What it does:
- Listens for TCP connections
- Prints connection events with timestamps
- Echoes back whatever the client sends
- Shuts down cleanly with Ctrl+C
"""
import argparse
import socket
import threading
import datetime
from typing import Tuple

def ts() -> str:
    """ISO 8601 timestamp helper."""
    return datetime.datetime.now().isoformat(timespec="seconds")

def handle_client(conn: socket.socket, addr: Tuple[str, int]) -> None:
    print(f"[{ts()}] Connected by {addr}")
    try:
        with conn:
            # Receive up to 1024 bytes at a time
            while True:
                data = conn.recv(1024)
                if not data:
                    print(f"[{ts()}] Client {addr} disconnected")
                    break
                message = data.decode(errors="replace")
                print(f"[{ts()}] Received from {addr}: {message!r}")
                response = f"Server received: {message}"
                conn.sendall(response.encode())
    except ConnectionResetError:
        print(f"[{ts()}] Connection reset by {addr}")
    except Exception as e:
        print(f"[{ts()}] Error with {addr}: {e}")

def main():
    parser = argparse.ArgumentParser(description="Simple threaded echo server")
    parser.add_argument("--host", default="127.0.0.1", help="Host/IP to bind (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=5000, help="Port to listen on (default: 5000)")
    args = parser.parse_args()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # Allow rapid restart during testing
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            s.bind((args.host, args.port))
            s.listen()
            print(f"[{ts()}] Server listening on {args.host}:{args.port}")
            while True:
                conn, addr = s.accept()
                t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
                t.start()
        except KeyboardInterrupt:
            print(f"\n[{ts()}] Shutting down server (KeyboardInterrupt) ...")
        except OSError as e:
            print(f"[{ts()}] Socket error: {e}")
        finally:
            print(f"[{ts()}] Server stopped")

if __name__ == "__main__":
    main()
