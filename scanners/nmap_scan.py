import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

def run_nmap():
    alive_file = os.path.join(ROOT_DIR, "results", "alive.txt")
    output_file = os.path.join(ROOT_DIR, "results", "ports.txt")

    if not os.path.exists(alive_file):
        print("[-] alive.txt not found. Run httpx scan first.")
        return

    try:
        print("[+] Running Nmap on alive subdomains...")
        subprocess.run(
            ["nmap", "-iL", alive_file, "-p-", "--open", "-oN", output_file],
            check=True
        )
        print(f"[+] Nmap scan complete. Results saved to {output_file}")

    except Exception as e:
        print(f"[-] Nmap error: {str(e)}")
