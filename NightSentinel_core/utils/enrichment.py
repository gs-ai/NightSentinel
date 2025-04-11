import socket
import whois

def perform_whois_lookup(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        print(f"Error performing WHOIS lookup: {e}")
        return None

def perform_dns_lookup(domain):
    try:
        return socket.gethostbyname_ex(domain)
    except socket.gaierror as e:
        print(f"Error performing DNS lookup: {e}")
        return None