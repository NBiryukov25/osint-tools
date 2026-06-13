# osint-tools
OSINT Dork Generator — Create categorized Google dorking queries for investigations. Input target details (name, username, email, phone, domain) and export 50+ search variations to CSV with clickable URLs. No dependencies. Python 3.6+.

OSINT Dork Generator

Generate Google dorking queries for open source intelligence (OSINT) investigations. Exports to CSV with clickable search URLs.

What it does

Takes target info (name, username, email, phone, domain, etc.) and generates categorized Google dorks (50+ variations). Exports to CSV with priority levels and clickable links. No dependencies — uses only Python standard library.

Categories

Identity — Names, usernames across platforms (GitHub, Twitter/X, Instagram, LinkedIn, Reddit, etc.)
Contact — Email and phone number searches including leak checks
Domain — Website-specific dorks and cached pages
Location — Geographic cross-references
Professional — Company and work associations
CrossRef — Combined field searches
DeepWeb — Pastebin, database mentions, leak references

Usage

Run the script:
python3 osint_dorks.py

Enter target info when prompted. Fields can be left blank. Output is a timestamped CSV file with sortable, clickable Google URLs.

Output Columns

Priority (High/Medium/Low)
Category and Subcategory
Query (the actual dork)
Google_URL (clickable link)

Requirements

Python 3.6 or higher

No pip install needed. Uses only standard library modules (csv, urllib.parse, datetime).
