# Configuration settings for the advanced cybersecurity tool

class Config:
    DEFAULT_SCAN_TIMEOUT = 30  # Default timeout for scans in seconds
    DEFAULT_RETRY_COUNT = 3     # Default number of retries for failed scans
    OUTPUT_DIRECTORY = "output"  # Directory to save scan results
    NMAP_PATH = "/usr/bin/nmap"  # Path to the Nmap executable
    SCAPY_LOG_LEVEL = "INFO"      # Log level for Scapy
    VULNERABILITY_DB_URL = "https://vulndb.com/api"  # URL for vulnerability database
    REPORT_FORMAT = "pdf"         # Default report format (pdf, html, etc.)
    ENABLE_VERBOSE_LOGGING = False # Flag to enable verbose logging

    @staticmethod
    def get_nmap_options():
        return "-sS -sV -O"  # Default Nmap options for scanning

    @staticmethod
    def get_scapy_options():
        return {"iface": "eth0", "filter": "ip"}  # Default Scapy options for sniffing