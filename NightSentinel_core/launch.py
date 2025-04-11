import os
import sys
import json
from datetime import datetime

# Ensure NightSentinel_core is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from NightSentinel_core.core.framework import EnhancedFramework
from NightSentinel_core.mixins.browser import BrowserAutomationMixin
from NightSentinel_core.utils.storage import SQLiteStorageSystem
from NightSentinel_core.utils.translator import translator_instance
from NightSentinel_core.utils.crawler import WebCrawler
from NightSentinel_core.utils.enrichment import perform_whois_lookup, perform_dns_lookup
from NightSentinel_core.utils.socmint import scrape_twitter_profile, scrape_linkedin_profile
from NightSentinel_core.utils.metadata import extract_file_metadata, extract_image_metadata
from NightSentinel_core.utils.darkweb import initialize_tor_session, renew_tor_ip, crawl_onion_site

class NightSentinelLauncher(BrowserAutomationMixin):
    def __init__(self):
        super().__init__()
        self.framework = EnhancedFramework(params={})  # Initialize EnhancedFramework

    def run(self):
        print("*****************************************")
        print("*                                       *")
        print("*       ")
        print("     _____                                     _____                                                               ")
        print(" ___|   _ |__  ____  ______  __   _    __   __|___  |__  ______  ____   _    __    ____  ____   _  ______  ____    ")
        print("|    \ | |   ||    ||   ___||  |_| | _|  |_|   ___|    ||   ___||    \ | | _|  |_ |    ||    \ | ||   ___||    |   ")
        print("|     \| |   ||    ||   |  ||   _  ||_    _|`-.`-.     ||   ___||     \| ||_    _||    ||     \| ||   ___||    |_  ")
        print("|__/\____| __||____||______||__| |_|  |__| |______|  __||______||__/\____|  |__|  |____||__/\____||______||______| ")
        print("    |_____|                                   |_____|                                                              ")
        print("                                                                                                                   ")
        print("     *")
        print("*                                       *")
        print("*****************************************")
        print("\nUnleashing the Power of NightSentinel:\n")
        print("- Comprehensive reconnaissance with cutting-edge browser automation.")
        print("- Advanced data extraction using intelligent CSS and XPath selectors.")
        print("- Streamlined investigations with minimal user input for maximum efficiency.")
        print("- Automated investigative report generation in sleek HTML format.")
        print("\n*****************************************")

        # Query the user for the URL
        url = input("Enter the URL to analyze: ").strip()
        if not url:
            print("No URL provided. Exiting.")
            return

        try:
            # Ensure the URL is properly formatted
            if not url.startswith("http://") and not url.startswith("https://"):
                if url.startswith("www."):
                    url = "https://" + url
                else:
                    url = "https://www." + url

            # Perform WHOIS lookup
            domain = url.split('//')[-1].split('/')[0]
            whois_data = perform_whois_lookup(domain)

            # Perform DNS lookup
            dns_data = perform_dns_lookup(domain)

            # Crawl the website
            crawler = WebCrawler(base_url=url, max_depth=3)
            crawler.crawl(url)
            crawled_urls = crawler.get_visited_urls()

            # Generate a report
            report_data = {
                "url": url,
                "whois_data": whois_data,
                "dns_data": dns_data,
                "crawled_urls": list(crawled_urls),
            }

            self.framework.generate_report(data=report_data, format="html")
            print("Investigative report generated successfully.")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close resources
            self.close_browser()

if __name__ == "__main__":
    launcher = NightSentinelLauncher()
    launcher.run()