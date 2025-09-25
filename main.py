from scanners.subdomain_enum import find_subdomains
from scanners.httpx_scan import check_alive
from scanners.katana_scan import run_katana

def main():
    domain = input("Enter domain: ").strip()

    # Step 1: Subdomain Enumeration
    subdomains = find_subdomains(domain)
    print(f"\n[+] Total subdomains found: {len(subdomains)}")

    # Step 2: Alive check with httpx
    alive_domains = check_alive(subdomains)
    print(f"[+] Alive subdomains found: {len(alive_domains)}")

    # Step 3: Crawl with katana
    run_katana()

if __name__ == "__main__":
    main()
