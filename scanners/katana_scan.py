import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

def run_katana():
    """Run katana on alive.txt and save results to endpoints.txt"""

    katana_path = os.path.join(ROOT_DIR, "katana.exe")
    input_file = os.path.join(ROOT_DIR, "alive.txt")
    output_file = os.path.join(ROOT_DIR, "endpoints.txt")

    if not os.path.exists(katana_path):
        print("[-] katana.exe not found in project root.")
        return []

    if not os.path.exists(input_file):
        print("[-] alive.txt not found. Run httpx scan first.")
        return []

    try:
        print(f"[+] Finding All Possible Endpoints Using Katana...")
        subprocess.run(
            [katana_path, "-silent", "-list", input_file, "-o", output_file],
            check=True
        )
        print(f"[+] Katana scan completed. Results saved in {output_file}")

        # ✅ Read endpoints from output file and return as list
        if os.path.exists(output_file):
            with open(output_file, "r") as f:
                endpoints = [line.strip() for line in f if line.strip()]
            return endpoints

        return []

    except Exception as e:
        print(f"[-] Katana error: {str(e)}")
        return []
