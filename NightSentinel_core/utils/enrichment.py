import socket
import whois

def perform_whois_lookup(domain):
    try:
        w = whois.query(domain)
        if w:
            return {
                "name": w.name,
                "registrar": w.registrar,
                "creation_date": w.creation_date,
                "expiration_date": w.expiration_date
            }
        else:
            print("WHOIS query returned no data. Please verify the domain.")
            return None
    except Exception as e:
        print(f"Error performing WHOIS lookup: {e}")
        return None

def perform_dns_lookup(domain):
    try:
        return socket.gethostbyname_ex(domain)
    except socket.gaierror as e:
        print(f"Error performing DNS lookup: {e}")
        return None