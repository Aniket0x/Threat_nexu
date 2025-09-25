import subprocess
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # /scanners
ROOT_DIR = os.path.dirname(BASE_DIR)  # project root

def find_subdomains(domain: str):
    """Run Subfinder on a domain and return subdomains list."""
    subfinder_path = os.path.join(ROOT_DIR, "subfinder.exe")

    try:
        print(f"[+] Finding All Possible Subdomains on {domain}...")
        result = subprocess.run(
            [subfinder_path, "-d", domain, "-silent"],
            capture_output=True,
            text=True
        )

        if result.stderr:
            print(f"[-] Subfinder error: {result.stderr.strip()}")

        # Clean subdomains list
        subdomains = result.stdout.strip().split("\n")
        return [s for s in subdomains if s]

    except FileNotFoundError:
        print("[-] subfinder.exe not found in project root.")
        return []
