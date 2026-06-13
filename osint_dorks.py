#!/usr/bin/env python3
import csv
import urllib.parse
from datetime import datetime


class OSINTDorksGenerator:
    def __init__(self):
        self.dorks = []
        
    def get_inputs(self):
        print("\n" + "="*60)
        print("🔍 OSINT DORKS GENERATOR - CSV EXPORT")
        print("="*60 + "\n")
        
        inputs = {}
        print("Enter target information (press Enter to skip):")
        print("-" * 50)
        
        inputs['primary_name'] = input("Primary Full Name: ").strip()
        inputs['alt_name'] = input("Alternate Name (nickname/alias/maiden): ").strip()
        inputs['primary_username'] = input("Primary Username: ").strip()
        inputs['alt_username'] = input("Alternate Username: ").strip()
        inputs['email'] = input("Email Address: ").strip()
        inputs['phone'] = input("Phone Number: ").strip()
        inputs['domain'] = input("Domain/Website: ").strip()
        inputs['location'] = input("Location/City: ").strip()
        inputs['company'] = input("Company/Organization: ").strip()
        
        return inputs
    
    def make_url(self, query):
        """Create clickable Google search URL"""
        return f"https://www.google.com/search?q={urllib.parse.quote(query)}"
    
    def generate_dorks(self, inputs):
        """Generate comprehensive dorks with full categorization"""
        
        primary_name = inputs.get('primary_name', '')
        alt_name = inputs.get('alt_name', '')
        primary_username = inputs.get('primary_username', '')
        alt_username = inputs.get('alt_username', '')
        email = inputs.get('email', '')
        phone = inputs.get('phone', '')
        domain = inputs.get('domain', '')
        location = inputs.get('location', '')
        company = inputs.get('company', '')
        
        all_names = [n for n in [primary_name, alt_name] if n]
        all_usernames = [u for u in [primary_username, alt_username] if u]
        
        # === IDENTITY - NAMES ===
        for n in all_names:
            self.dorks.extend([
                (f'"{n}"', "Identity", "Name - Exact", "High"),
                (f'"{n}" filetype:pdf', "Identity", "Name - PDFs", "Medium"),
                (f'"{n}" filetype:doc OR filetype:docx', "Identity", "Name - Documents", "Medium"),
                (f'"{n}" filetype:xls OR filetype:xlsx', "Identity", "Name - Spreadsheets", "Medium"),
                (f'"{n}" "resume" OR "CV"', "Identity", "Name - Resumes", "Medium"),
                (f'"{n}" "contact" OR "email"', "Identity", "Name - Contact Info", "Medium"),
                (f'"{n}" intitle:"profile"', "Identity", "Name - Profile Pages", "Medium"),
                (f'"{n}" inurl:profile', "Identity", "Name - URL Profiles", "Medium"),
            ])
        
        # === IDENTITY - USERNAME ===
        for u in all_usernames:
            self.dorks.extend([
                (f'"{u}"', "Identity", "Username - Exact", "High"),
                (f'"{u}" site:github.com', "Identity", "Username - GitHub", "High"),
                (f'"{u}" site:gitlab.com', "Identity", "Username - GitLab", "Medium"),
                (f'"{u}" site:twitter.com OR site:x.com', "Identity", "Username - Twitter/X", "High"),
                (f'"{u}" site:instagram.com', "Identity", "Username - Instagram", "High"),
                (f'"{u}" site:reddit.com', "Identity", "Username - Reddit", "Medium"),
                (f'"{u}" site:linkedin.com', "Identity", "Username - LinkedIn", "Medium"),
                (f'"{u}" site:tiktok.com', "Identity", "Username - TikTok", "Medium"),
                (f'"{u}" site:youtube.com', "Identity", "Username - YouTube", "Medium"),
                (f'"{u}" site:twitch.tv', "Identity", "Username - Twitch", "Low"),
                (f'"{u}" site:steamcommunity.com', "Identity", "Username - Steam", "Low"),
                (f'"{u}" "forum"', "Identity", "Username - Forums", "Low"),
            ])
        
        # === CONTACT - EMAIL ===
        if email:
            local_part = email.split('@')[0] if '@' in email else email
            domain_part = email.split('@')[1] if '@' in email else ''
            
            self.dorks.extend([
                (f'"{email}"', "Contact", "Email - Exact", "High"),
                (f'"{email}" "leaked" OR "breach" OR "dump"', "Contact", "Email - Leaks", "High"),
                (f'"{email}" site:haveibeenpwned.com', "Contact", "Email - HIBP", "High"),
                (f'"{email}" site:pastebin.com', "Contact", "Email - Pastebin", "Medium"),
                (f'"{local_part}"', "Contact", "Email - Local Part Only", "Medium"),
                (f'"{email}" filetype:txt', "Contact", "Email - Text Files", "Medium"),
            ])
        
        # === CONTACT - PHONE ===
        if phone:
            clean_phone = phone.replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
            self.dorks.extend([
                (f'"{phone}"', "Contact", "Phone - Exact", "High"),
                (f'"{clean_phone}"', "Contact", "Phone - Clean Format", "High"),
                (f'"{phone}" "reverse lookup"', "Contact", "Phone - Reverse Lookup", "Medium"),
                (f'"{phone}" site:facebook.com', "Contact", "Phone - Facebook", "Medium"),
                (f'"{phone}" "whatsapp"', "Contact", "Phone - WhatsApp", "Low"),
            ])
        
        # === DOMAIN / WEBSITE ===
        if domain:
            clean_domain = domain.replace('https://', '').replace('http://', '').replace('www.', '').strip('/')
            self.dorks.extend([
                (f'site:{clean_domain}', "Domain", "Domain - Site Search", "High"),
                (f'site:{clean_domain} filetype:pdf', "Domain", "Domain - PDFs", "Medium"),
                (f'site:{clean_domain} "admin" OR "login"', "Domain", "Domain - Admin/Login", "Medium"),
                (f'"@{clean_domain}"', "Domain", "Domain - Email Domain", "Medium"),
                (f'"{clean_domain}" "whois"', "Domain", "Domain - WHOIS", "Low"),
                (f'cache:{clean_domain}', "Domain", "Domain - Cached", "Low"),
            ])
        
        # === LOCATION ===
        if location:
            for n in all_names:
                self.dorks.extend([
                    (f'"{n}" "{location}"', "Location", "Name + Location", "Medium"),
                    (f'"{n}" "{location}" site:facebook.com', "Location", "Name + Location - Facebook", "Medium"),
                ])
        
        # === COMPANY / WORK ===
        if company:
            for n in all_names:
                self.dorks.extend([
                    (f'"{n}" "{company}"', "Professional", "Name + Company", "Medium"),
                    (f'"{n}" "{company}" site:linkedin.com', "Professional", "Name + Company - LinkedIn", "High"),
                ])
        
        # === COMBINED / CROSS-REFERENCE ===
        if primary_name and primary_username:
            self.dorks.append((f'"{primary_name}" "{primary_username}"', "CrossRef", "Name + Username", "High"))
        if email and primary_username:
            self.dorks.append((f'"{email}" "{primary_username}"', "CrossRef", "Email + Username", "High"))
        if alt_name and primary_username:
            self.dorks.append((f'"{alt_name}" "{primary_username}"', "CrossRef", "Alt Name + Username", "Medium"))
        
        # === ADVANCED / DEEP WEB ===
        for n in all_names:
            self.dorks.extend([
                (f'"{n}" site:pastebin.com', "DeepWeb", "Name - Pastebin", "Medium"),
                (f'"{n}" inurl:paste', "DeepWeb", "Name - Paste URLs", "Medium"),
                (f'"{n}" "database" OR "dump"', "DeepWeb", "Name - Database Mentions", "Low"),
            ])
        
        for u in all_usernames:
            self.dorks.extend([
                (f'"{u}" "password" OR "pass"', "DeepWeb", "Username - Password Mentions", "Low"),
                (f'"{u}" "leaked" OR "exposed"', "DeepWeb", "Username - Leak Mentions", "Low"),
            ])
        
        return self.dorks
    
    def export_to_csv(self, filename=None):
        if not filename:
            filename = f"osint_dorks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        # Sort by priority then category
        sorted_dorks = sorted(self.dorks, key=lambda x: ({"High": 0, "Medium": 1, "Low": 2}.get(x[3], 3), x[0]))
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Priority', 'Category', 'Subcategory', 'Query', 'Google_URL'])
            
            for query, category, subcategory, priority in sorted_dorks:
                url = self.make_url(query)
                writer.writerow([priority, category, subcategory, query, url])
        
        print(f"\n💾 Saved: {filename}")
        print(f"📊 Total dorks: {len(sorted_dorks)}")
        
        # Print summary
        categories = {}
        for _, cat, _, pri in sorted_dorks:
            key = f"{cat} ({pri})"
            categories[key] = categories.get(key, 0) + 1
        
        print(f"\n📋 Breakdown:")
        for cat, count in sorted(categories.items()):
            print(f"   {cat}: {count}")
        
        return filename
    
    def run(self):
        inputs = self.get_inputs()
        
        print("\n🔄 Generating dorks...")
        self.generate_dorks(inputs)
        print(f"✅ Generated {len(self.dorks)} dorks")
        
        self.export_to_csv()


if __name__ == "__main__":
    generator = OSINTDorksGenerator()
    generator.run()