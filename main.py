def main():

"""
Main entry point for the Advanced Cybersecurity Tool.
Provides command-line interface for port scanning and file encryption/decryption.
"""

import argparse
from port_scanner import scan_ports
from file_encryptor import encrypt_file, decrypt_file

def main():
    """Parse command-line arguments and execute the selected command."""
    parser = argparse.ArgumentParser(description="Advanced Cybersecurity Tool")
    subparsers = parser.add_subparsers(dest="command")

    # Port scanner command
    scan_parser = subparsers.add_parser("scan", help="Scan ports on a host")
    scan_parser.add_argument("host", help="Target host to scan")
    scan_parser.add_argument("--start", type=int, default=1, help="Start port")
    scan_parser.add_argument("--end", type=int, default=1024, help="End port")

    # File encryption command
    enc_parser = subparsers.add_parser("encrypt", help="Encrypt a file")
    enc_parser.add_argument("file", help="File to encrypt")
    enc_parser.add_argument("key", help="Encryption key (32 bytes or Fernet key)")

    # File decryption command
    dec_parser = subparsers.add_parser("decrypt", help="Decrypt a file")
    dec_parser.add_argument("file", help="File to decrypt")
    dec_parser.add_argument("key", help="Decryption key (32 bytes or Fernet key)")

    args = parser.parse_args()

    if args.command == "scan":
        scan_ports(args.host, args.start, args.end)
    elif args.command == "encrypt":
        encrypt_file(args.file, args.key)
    elif args.command == "decrypt":
        decrypt_file(args.file, args.key)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
