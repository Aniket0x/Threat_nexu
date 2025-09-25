import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(BASE_DIR)

def check_alive(subdomains):
    """Check which subdomains are alive using httpx.exe"""
    httpx_path = os.path.join(ROOT_DIR, "httpx.exe")

    if not os.path.exists(httpx_path):
        print("[-] httpx.exe not found in project root.")
        return []

    # Save subdomains into a temp file
    input_file = os.path.join(ROOT_DIR, "subdomains.txt")
    with open(input_file, "w") as f:
        f.write("\n".join(subdomains))

    try:
        # Step 1: Run httpx to find alive subdomains
        result = subprocess.run(
            [httpx_path, "-silent", "-l", input_file],
            capture_output=True,
            text=True
        )

        alive = result.stdout.strip().split("\n")
        alive = [a for a in alive if a]

        # Save alive subdomains into alive.txt
        alive_file = os.path.join(ROOT_DIR, "alive.txt")
        with open(alive_file, "w") as f:
            f.write("\n".join(alive))

        # Step 2: Detailed scan (status code + title), save only in file
        detailed_file = os.path.join(ROOT_DIR, "httpx_detailed.txt")
        subprocess.run(
            [httpx_path,"-silent", "-l", alive_file, "-sc", "-title", "-o", detailed_file],
            text=True
        )

        # No output to console, just returning alive list in case needed
        return alive

    except Exception as e:
        print(f"[-] httpx error: {str(e)}")
        return []
