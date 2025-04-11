# NightSentinel

```
\033[1;34m_____                                     _____                                                               \033[0m
\033[1;36m ___|   _ |__  ____  ______  __   _    __   __|___  |__  ______  ____   _    __    ____  ____   _  ______  ____    \033[0m
\033[1;37m|    \ | |   ||    ||   ___||  |_| | _|  |_|   ___|    ||   ___||    \ | | _|  |_ |    ||    \ | ||   ___||    |   \033[0m
\033[1;36m|     \| |   ||    ||   |  ||   _  ||_    _|`-.`-.     ||   ___||     \| ||_    _||    ||     \| ||   ___||    |_  \033[0m
\033[1;34m|__/\____| __||____||______||__| |_|  |__| |______|  __||______||__/\____|  |__|  |____||__/\____||______||______| \033[0m
\033[1;37m    |_____|                                   |_____|\033[0m
```

## Overview
NightSentinel is a comprehensive reconnaissance and data collection framework designed for advanced web scraping, metadata extraction, social media intelligence, and dark web exploration. It integrates multiple submodules and utilities to provide a modular, extensible, and efficient solution for gathering and analyzing data.

## Features
- **Web Crawling and Scraping**: Deep crawling and scraping capabilities using CSS and XPath selectors.
- **Social Media Intelligence (SOCMINT)**: Extract data from platforms like Twitter and LinkedIn.
- **Metadata Extraction**: Extract metadata from files and images, including EXIF data.
- **Dark Web Exploration**: Crawl `.onion` sites using Tor integration.
- **WHOIS and DNS Lookups**: Perform domain lookups for additional context.
- **Browser Automation**: Automate browser actions for advanced data collection.
- **Modular Architecture**: Easily extend functionality with submodules like `Scrapling-main` and `camoufox-main`.
- **Flexible Reporting**: Generate reports in multiple formats, including HTML and JSON.

## Project Structure

### Root Directory
- **`dark_stalker.txt`**: ASCII art representing the NightSentinel logo.
- **`README-NightSentinel.md`**: This file, providing an overview of the project.
- **`NightSentinel_requirements.txt`**: Lists the dependencies required for the project.

### Subdirectories

#### `NightSentinel_core`
- **`launch.py`**: The main entry point for the program.
- **`core/`**: Core logic and framework components.
- **`mixins/`**: Reusable mixin classes for browser automation and other utilities.
- **`utils/`**: Utility functions for crawling, enrichment, metadata extraction, and more.

#### `Scrapling-main`
- **Purpose**: A submodule for advanced web scraping.
- **Key Features**:
  - Provides high-performance scraping capabilities.
  - Includes benchmarking tools to compare scraping performance.
  - Offers flexible and extensible scraping adaptors.
- **Key Files**:
  - `benchmarks.py`: Benchmarking tools for scraping performance.
  - `setup.py`: Defines dependencies and installation for the Scrapling module.
  - `tests/`: Contains test cases for Scrapling.

#### `camoufox-main`
- **Purpose**: A submodule for browser automation and obfuscation.
- **Key Features**:
  - Enables stealthy browser automation with advanced obfuscation techniques.
  - Provides tools for spoofing browser fingerprints and other identifiers.
  - Includes configurations for multiple platforms (Linux, macOS, Windows).
- **Key Files**:
  - `setup.py`: Defines dependencies and installation for the Camoufox module.
  - `additions/`: Contains browser configuration files and assets.
  - `scripts/`: Helper scripts for building and managing the module.
  - `tests/`: Contains test cases for Camoufox.

## Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)
- SQLite (for database storage)
- Tor (for dark web exploration)

### Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd NightSentinel
   ```
2. Install dependencies:
   ```bash
   pip install -r NightSentinel/NightSentinel_requirements.txt
   ```
3. Install submodules:
   ```bash
   pip install -e NightSentinel/Scrapling-main
   pip install -e NightSentinel/camoufox-main
   ```

## Usage

### Running the Program
1. Activate the Python environment:
   ```bash
   conda activate NightSentinel
   ```
2. Run the main script:
   ```bash
   python NightSentinel/NightSentinel_core/launch.py
   ```

### Features
- **Web Crawling**: Enter a URL to crawl and extract data.
- **Social Media Intelligence**: Provide Twitter or LinkedIn profiles for data extraction.
- **Metadata Extraction**: Input file paths to extract metadata.
- **Dark Web Exploration**: Enter `.onion` URLs for crawling.

## Database
- All data is stored in SQLite databases named `NightVault_<timestamp>.db`.
- Databases are created dynamically for each session and stored in the root directory.

## Contributing
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-branch
   ```
5. Open a pull request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- **Scrapling**: For advanced web scraping capabilities.
- **Camoufox**: For browser automation and obfuscation tools.
- **Tor Project**: For enabling dark web exploration.

---
For more information, refer to the documentation in the respective submodules or contact the project maintainers.
