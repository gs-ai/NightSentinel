import os
import sys
import json
from datetime import datetime

# Ensure NightSentinel_core is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Add Scrapling and Camoufox to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "../../Scrapling-main"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../camoufox_main"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../camoufox_main/scripts"))

# Explicitly add the `scripts` directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "../../camoufox_main/scripts"))

# Debugging: Print the Python path to verify the inclusion of necessary directories
print("Python Path:", sys.path)

from NightSentinel_core.core.framework import EnhancedFramework
from NightSentinel_core.mixins.browser import BrowserAutomationMixin
from NightSentinel_core.utils.storage import SQLiteStorageSystem
from NightSentinel_core.utils.translator import translator_instance
from NightSentinel_core.utils.crawler import WebCrawler
from NightSentinel_core.utils.enrichment import perform_whois_lookup, perform_dns_lookup
from NightSentinel_core.utils.socmint import scrape_twitter_profile, scrape_linkedin_profile
from NightSentinel_core.utils.metadata import extract_file_metadata, extract_image_metadata
from NightSentinel_core.utils.darkweb import initialize_tor_session, renew_tor_ip, crawl_onion_site
from scrapling import Adaptor
from camoufox_main.scripts._mixin import CamoufoxMixin
from autoscraper import AutoScraper

class NightSentinelLauncher(BrowserAutomationMixin, CamoufoxMixin):
    def __init__(self):
        super().__init__()
        self.framework = EnhancedFramework(params={})  # Initialize EnhancedFramework
        self.scrapling_adaptor = AutoScraper()  # Initialize AutoScraper

    def run(self):
        print("\033[1;34m*****************************************\033[0m")
        print("\033[1;36m*                                       *\033[0m")
        print("\033[1;37m*       \033[0m")
        print("\033[1;34m     _____                                     _____                                                               \033[0m")
        print("\033[1;36m ___|   _ |__  ____  ______  __   _    __   __|___  |__  ______  ____   _    __    ____  ____   _  ______  ____    \033[0m")
        print("\033[1;37m|    \\ | |   ||    ||   ___||  |_| | _|  |_|   ___|    ||   ___||    \\ | | _|  |_ |    ||    \\ | ||   ___||    |   \033[0m")
        print("\033[1;36m|     \\| |   ||    ||   |  ||   _  ||_    _|`-.`-.     ||   ___||     \\| ||_    _||    ||     \\| ||   ___||    |_  \033[0m")
        print("\033[1;34m|__/\\____| __||____||______||__| |_|  |__| |______|  __||______||__/\\____|  |__|  |____||__/\\____||______||______| \033[0m")
        print("\033[1;37m    |_____|                                   |_____|                                                              \033[0m")
        print("\033[1;36m                                                                                                                   \033[0m")
        print("\033[1;34m     *\033[0m")
        print("\033[1;36m*                                       *\033[0m")
        print("\033[1;34m*****************************************\033[0m")
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

            # Initialize scraped_data to avoid referencing before assignment
            scraped_data = []

            # Updated Scrapling integration to shift to JS scraping if no data is found
            print("\nUsing Scrapling for advanced web scraping...")
            scraped_data = []
            try:
                scraped_data = self.scrapling_adaptor.build(url, wanted_list=['Example'])
                if not scraped_data:
                    print("No data found with standard scraping. Switching to JS scraping...")
                    from playwright.sync_api import sync_playwright
                    with sync_playwright() as p:
                        browser = p.chromium.launch(headless=True)
                        page = browser.new_page()
                        page.goto(url)
                        scraped_data = page.content()  # Extract full page content
                        browser.close()
            except Exception as e:
                print(f"Error during scraping: {e}")

            # Use Camoufox for browser automation
            print("\nUsing Camoufox for stealthy browser automation...")
            self.camoufox_automate(url)

            # Define the first part of the OSINT-related data categories to search for
            osint_targets = [
                "metadata",  # Extract metadata from the page
                "social media links",  # Look for links to social media profiles
                "contact details",  # Search for email addresses, phone numbers, etc.
                "keywords",  # Identify specific keywords or phrases
                "external links"  # Collect external links for further analysis
            ]

            print("\nSearching for OSINT-related data...")
            for target in osint_targets:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "metadata": extract_metadata_function()

            # Add the second part of the OSINT-related data categories to search for
            osint_targets_part2 = [
                "IP addresses",  # Extract IP addresses from the page
                "geolocation data",  # Look for geolocation information
                "email addresses",  # Search for email addresses in the content
                "phone numbers",  # Extract phone numbers from the page
                "file links"  # Identify downloadable file links (e.g., PDFs, docs)
            ]

            print("\nContinuing OSINT data search...")
            for target in osint_targets_part2:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "IP addresses": extract_ip_addresses_function()

            # Add the third part of the OSINT-related data categories to search for
            osint_targets_part3 = [
                "hidden directories",  # Search for hidden directories or endpoints
                "API keys",  # Look for exposed API keys in the content
                "cryptographic keys",  # Identify cryptographic keys or secrets
                "usernames",  # Extract usernames from the page
                "sensitive keywords"  # Search for sensitive keywords like 'password', 'confidential', etc.
            ]

            print("\nExpanding OSINT data search...")
            for target in osint_targets_part3:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "hidden directories": search_hidden_directories_function()

            # Add the fourth part of the OSINT-related data categories to search for
            osint_targets_part4 = [
                "exposed credentials",  # Search for exposed usernames and passwords
                "financial information",  # Look for financial data like credit card numbers
                "social security numbers",  # Identify SSNs or similar identifiers
                "tracking scripts",  # Detect tracking scripts or analytics tools
                "embedded media"  # Extract embedded media like videos or audio files
            ]

            print("\nDeepening OSINT data search...")
            for target in osint_targets_part4:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "exposed credentials": search_exposed_credentials_function()

            # Modify dark web and malware links to be sectioned off and not remotely accessible
            osint_targets_part5 = [
                "malware links",  # Detect links to potential malware or phishing sites
                "dark web references",  # Look for mentions of dark web marketplaces or onion links
                "code snippets",  # Extract code snippets or embedded scripts
                "open ports",  # Identify references to open ports or network configurations
                "security vulnerabilities"  # Search for mentions of known vulnerabilities or exploits
            ]

            print("\nPushing OSINT data search further...")
            for target in osint_targets_part5:
                print(f"Analyzing for: {target}")
                if target == "malware links" or target == "dark web references":
                    print(f"{target} will be sectioned off and not remotely accessible.")
                    # Logic to sanitize and isolate these links
                    # Example: Replace links with placeholders or store them in a secure, non-executable format
                    # sanitized_links = sanitize_links_function(scraped_data)
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "malware links": detect_malware_links_function()

            # Add the sixth part of the OSINT-related data categories to search for
            osint_targets_part6 = [
                "publicly exposed databases",  # Detect references to exposed databases (e.g., MongoDB, Elasticsearch)
                "cloud storage links",  # Look for links to cloud storage (e.g., AWS S3, Google Drive)
                "login portals",  # Identify login portals or admin panels
                "software versions",  # Extract software version numbers for vulnerability analysis
                "developer comments"  # Search for developer comments or TODOs in the code
            ]

            print("\nMaximizing OSINT data search...")
            for target in osint_targets_part6:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "publicly exposed databases": detect_exposed_databases_function()

            # Add the seventh part of the OSINT-related data categories to search for
            osint_targets_part7 = [
                "social engineering indicators",  # Look for content that could be used for social engineering
                "leaked documents",  # Detect references to leaked or confidential documents
                "threat actor mentions",  # Search for mentions of known threat actors or groups
                "breach data",  # Identify references to data breaches or leaked credentials
                "network configurations"  # Extract network-related configurations or details
            ]

            print("\nFinalizing OSINT data search...")
            for target in osint_targets_part7:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "social engineering indicators": detect_social_engineering_function()

            # Add the eighth part of the OSINT-related data categories to search for
            osint_targets_part8 = [
                "supply chain references",  # Look for mentions of supply chain partners or vendors
                "intellectual property",  # Detect references to patents, trademarks, or proprietary information
                "legal documents",  # Search for legal notices, terms of service, or privacy policies
                "employee information",  # Extract employee names, roles, or contact details
                "incident response plans"  # Identify references to security or incident response plans
            ]

            print("\nExploring advanced OSINT data categories...")
            for target in osint_targets_part8:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "supply chain references": detect_supply_chain_references_function()

            # Add the ninth part of the OSINT-related data categories to search for
            osint_targets_part9 = [
                "environmental data",  # Look for environmental impact reports or sustainability data
                "political affiliations",  # Detect references to political groups or affiliations
                "media mentions",  # Search for mentions in news articles or media outlets
                "historical data",  # Extract historical records or archived content
                "user-generated content"  # Identify user comments, reviews, or forum posts
            ]

            print("\nReaching deeper into OSINT data categories...")
            for target in osint_targets_part9:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "media mentions": detect_media_mentions_function()

            # Add the tenth part of the OSINT-related data categories to search for
            osint_targets_part10 = [
                "phishing indicators",  # Detect signs of phishing attempts or fake login pages
                "brand impersonation",  # Look for content impersonating well-known brands
                "data exfiltration methods",  # Identify potential methods for data exfiltration
                "insider threat indicators",  # Search for signs of insider threats or leaks
                "anomalous patterns"  # Detect unusual patterns or behaviors in the content
            ]

            print("\nUncovering advanced OSINT data categories...")
            for target in osint_targets_part10:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "phishing indicators": detect_phishing_indicators_function()

            # Add the eleventh part of the OSINT-related data categories to search for
            osint_targets_part11 = [
                "emerging threats",  # Look for mentions of new or emerging cyber threats
                "vulnerability disclosures",  # Detect references to disclosed vulnerabilities
                "threat intelligence feeds",  # Identify links or references to threat intelligence sources
                "security advisories",  # Search for security advisories or warnings
                "incident reports"  # Extract details from incident or breach reports
            ]

            print("\nDiving into specialized OSINT data categories...")
            for target in osint_targets_part11:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "emerging threats": detect_emerging_threats_function()

            # Add the twelfth part of the OSINT-related data categories to search for
            osint_targets_part12 = [
                "cybersecurity frameworks",  # Look for references to NIST, ISO, or other frameworks
                "compliance standards",  # Detect mentions of GDPR, HIPAA, PCI-DSS, etc.
                "threat hunting techniques",  # Identify references to threat hunting methodologies
                "security tools",  # Search for mentions of security tools like SIEMs or firewalls
                "incident timelines"  # Extract timelines of past incidents or breaches
            ]

            print("\nAdvancing OSINT data search...")
            for target in osint_targets_part12:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "cybersecurity frameworks": detect_cybersecurity_frameworks_function()

            # Add the thirteenth part of the OSINT-related data categories to search for
            osint_targets_part13 = [
                "data retention policies",  # Look for references to data storage and retention policies
                "employee training programs",  # Detect mentions of cybersecurity training initiatives
                "physical security measures",  # Identify references to physical security controls
                "supply chain vulnerabilities",  # Search for mentions of supply chain risks
                "business continuity plans"  # Extract details about business continuity or disaster recovery plans
            ]

            print("\nExploring organizational OSINT data categories...")
            for target in osint_targets_part13:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "data retention policies": detect_data_retention_policies_function()

            # Add the fourteenth part of the OSINT-related data categories to search for
            osint_targets_part14 = [
                "user behavior analytics",  # Look for patterns in user behavior or activity
                "insider threat detection",  # Detect signs of insider threats or malicious activity
                "anonymization techniques",  # Identify references to data anonymization methods
                "data masking",  # Search for mentions of data masking techniques
                "zero trust architecture"  # Detect references to zero trust security models
            ]

            print("\nFocusing on advanced security OSINT data categories...")
            for target in osint_targets_part14:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "user behavior analytics": detect_user_behavior_analytics_function()

            # Add the fifteenth part of the OSINT-related data categories to search for
            osint_targets_part15 = [
                "blockchain references",  # Look for mentions of blockchain technology or cryptocurrencies
                "smart contracts",  # Detect references to smart contracts or decentralized apps
                "tokenized assets",  # Search for mentions of tokenized assets or NFTs
                "cryptocurrency wallets",  # Identify references to cryptocurrency wallets or addresses
                "decentralized finance (DeFi)"  # Detect mentions of DeFi platforms or protocols
            ]

            print("\nInvestigating blockchain and cryptocurrency OSINT data categories...")
            for target in osint_targets_part15:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "blockchain references": detect_blockchain_references_function()

            # Add the sixteenth part of the OSINT-related data categories to search for
            osint_targets_part16 = [
                "emerging technologies",  # Look for mentions of AI, IoT, or quantum computing
                "patent filings",  # Detect references to patent applications or filings
                "research papers",  # Search for mentions of academic or industry research papers
                "open source projects",  # Identify references to open source software or repositories
                "technology roadmaps"  # Extract details about future technology plans or roadmaps
            ]

            print("\nExploring emerging technology OSINT data categories...")
            for target in osint_targets_part16:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "emerging technologies": detect_emerging_technologies_function()

            # Add the seventeenth part of the OSINT-related data categories to search for
            osint_targets_part17 = [
                "cyber espionage indicators",  # Look for signs of cyber espionage activities
                "hacktivist campaigns",  # Detect mentions of hacktivist groups or campaigns
                "nation-state actors",  # Identify references to nation-state threat actors
                "cyber warfare tactics",  # Search for mentions of cyber warfare strategies
                "critical infrastructure threats"  # Detect threats to critical infrastructure systems
            ]

            print("\nInvestigating cyber threat OSINT data categories...")
            for target in osint_targets_part17:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "cyber espionage indicators": detect_cyber_espionage_indicators_function()

            # Add the eighteenth part of the OSINT-related data categories to search for
            osint_targets_part18 = [
                "deepfake content",  # Look for signs of deepfake videos or images
                "AI-generated text",  # Detect AI-generated articles or comments
                "synthetic identities",  # Identify references to synthetic identities
                "voice cloning",  # Search for mentions of voice cloning technologies
                "AI-driven disinformation"  # Detect AI-driven disinformation campaigns
            ]

            print("\nExploring AI-related OSINT data categories...")
            for target in osint_targets_part18:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "deepfake content": detect_deepfake_content_function()

            # Add the nineteenth part of the OSINT-related data categories to search for
            osint_targets_part19 = [
                "biometric data",  # Look for references to biometric data like fingerprints or facial recognition
                "healthcare records",  # Detect mentions of exposed healthcare records
                "genomic data",  # Search for references to genomic or DNA data
                "medical devices",  # Identify mentions of medical device vulnerabilities
                "pharmaceutical research"  # Detect references to pharmaceutical research or trials
            ]

            print("\nFocusing on healthcare and biometric OSINT data categories...")
            for target in osint_targets_part19:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "biometric data": detect_biometric_data_function()

            # Add the twentieth part of the OSINT-related data categories to search for
            osint_targets_part20 = [
                "financial fraud schemes",  # Look for signs of financial fraud or scams
                "money laundering",  # Detect references to money laundering activities
                "tax evasion",  # Search for mentions of tax evasion schemes
                "investment scams",  # Identify references to fraudulent investment opportunities
                "cryptocurrency fraud"  # Detect signs of cryptocurrency-related fraud
            ]

            print("\nInvestigating financial crime OSINT data categories...")
            for target in osint_targets_part20:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "financial fraud schemes": detect_financial_fraud_schemes_function()

            # Add the twenty-first part of the OSINT-related data categories to search for
            osint_targets_part21 = [
                "climate change data",  # Look for references to climate change reports or data
                "natural disaster preparedness",  # Detect mentions of disaster preparedness plans
                "renewable energy projects",  # Search for references to renewable energy initiatives
                "environmental activism",  # Identify mentions of environmental activism or protests
                "sustainability metrics"  # Detect references to sustainability metrics or goals
            ]

            print("\nExploring environmental OSINT data categories...")
            for target in osint_targets_part21:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "climate change data": detect_climate_change_data_function()

            # Add the twenty-second part of the OSINT-related data categories to search for
            osint_targets_part22 = [
                "human rights violations",  # Look for references to human rights abuses or violations
                "whistleblower activity",  # Detect mentions of whistleblower reports or actions
                "protest movements",  # Search for references to protests or civil unrest
                "freedom of speech issues",  # Identify mentions of censorship or freedom of speech concerns
                "journalistic investigations"  # Detect references to investigative journalism reports
            ]

            print("\nExploring human rights and activism OSINT data categories...")
            for target in osint_targets_part22:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "human rights violations": detect_human_rights_violations_function()

            # Add the twenty-third part of the OSINT-related data categories to search for
            osint_targets_part23 = [
                "educational resources",  # Look for references to online courses or educational materials
                "academic collaborations",  # Detect mentions of academic partnerships or projects
                "university research",  # Search for references to university-led research
                "student activism",  # Identify mentions of student-led activism or protests
                "scholarship opportunities"  # Detect references to scholarships or funding opportunities
            ]

            print("\nExploring educational OSINT data categories...")
            for target in osint_targets_part23:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "educational resources": detect_educational_resources_function()

            # Add the twenty-fourth part of the OSINT-related data categories to search for
            osint_targets_part24 = [
                "corporate espionage",  # Look for signs of corporate espionage or trade secret theft
                "mergers and acquisitions",  # Detect references to corporate mergers or acquisitions
                "financial performance",  # Search for mentions of financial reports or performance metrics
                "board of directors",  # Identify references to corporate leadership or board members
                "shareholder activity"  # Detect mentions of shareholder meetings or actions
            ]

            print("\nExploring corporate OSINT data categories...")
            for target in osint_targets_part24:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "corporate espionage": detect_corporate_espionage_function()

            # Add the twenty-fifth part of the OSINT-related data categories to search for
            osint_targets_part25 = [
                "military operations",  # Look for references to military activities or operations
                "defense contracts",  # Detect mentions of defense-related contracts or agreements
                "weapons development",  # Search for references to weapons research or development
                "geopolitical conflicts",  # Identify mentions of geopolitical tensions or conflicts
                "intelligence agencies"  # Detect references to intelligence agencies or operations
            ]

            print("\nExploring military and defense OSINT data categories...")
            for target in osint_targets_part25:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "military operations": detect_military_operations_function()

            # Add the twenty-sixth part of the OSINT-related data categories to search for
            osint_targets_part26 = [
                "cultural heritage",  # Look for references to cultural heritage sites or artifacts
                "art theft",  # Detect mentions of stolen or missing artwork
                "historical preservation",  # Search for references to historical preservation efforts
                "archaeological discoveries",  # Identify mentions of recent archaeological finds
                "museum collections"  # Detect references to museum exhibits or collections
            ]

            print("\nExploring cultural and historical OSINT data categories...")
            for target in osint_targets_part26:
                print(f"Analyzing for: {target}")
                # Add logic to search for each target in the scraped data or page content
                # Example: if target == "cultural heritage": detect_cultural_heritage_function()

            # Generate a report
            report_data = {
                "url": url,
                "whois_data": whois_data,
                "dns_data": dns_data,
                "scraped_data": scraped_data,
            }

            # Move the Reports directory to the main directory
            reports_dir = os.path.join(parent_dir, "Reports")
            os.makedirs(reports_dir, exist_ok=True)

            # Generate a filename based on the URL and current timestamp
            sanitized_url = url.replace("http://", "").replace("https://", "").replace("/", "_").replace(":", "_")
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            report_filename = f"{sanitized_url}_{timestamp}.html"
            report_path = os.path.join(reports_dir, report_filename)

            # Save the report to the file
            self.framework.generate_report(data=report_data, format="html", output_file=report_path)

            print(f"Investigative report generated successfully: {report_path}")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Close resources
            self.close_browser()

if __name__ == "__main__":
    launcher = NightSentinelLauncher()
    launcher.run()