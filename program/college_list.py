# This code create the college_list.csv file which contains all the school's name, state, and ID 

import csv
import requests
from bs4 import BeautifulSoup
import time
import re

# Output CSV file
output_file = "college_list.csv"
headers = ["IDs", "Names", "States"]

# Small subset of state codes for testing
state_codes = ["WY", "AS", "MP", "VI"]

'''
state_codes = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL",
    "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME",
    "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH",
    "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
    "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI",
    "WY", "AS", "GU", "MP", "PR", "VI"
]
'''

# Base listing URL
base_url = "https://nces.ed.gov/collegenavigator/?s={state_code}&pg={page_num}"

# School details URL pattern
school_url_template = "https://nces.ed.gov/collegenavigator/?s={state_code}&id={school_id}"

# Open CSV for writing
with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)

    for state_code in state_codes:
        page_num = 1

        while True:
            url = base_url.format(state_code=state_code, page_num=page_num)
            print(f"Scraping listing page: {url}")
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Failed to load listing page {url}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all links that contain "&id=" in the href
            links = soup.find_all("a", href=True)
            id_links = [link['href'] for link in links if "&id=" in link['href']]

            if not id_links:
                print("No more schools found on this page.")
                break

            # Use a set to avoid duplicate IDs
            seen_ids = set()

            for href in id_links:
                match = re.search(r"&id=(\d+)", href)
                if not match:
                    continue

                school_id = match.group(1)
                if school_id in seen_ids:
                    continue  # skip duplicates

                seen_ids.add(school_id)

                # Visit individual school page
                school_url = school_url_template.format(state_code=state_code, school_id=school_id)
                school_response = requests.get(school_url)
                if school_response.status_code != 200:
                    print(f"Failed to load school page {school_url}")
                    continue

                school_soup = BeautifulSoup(school_response.text, 'html.parser')
                title_tag = school_soup.find("title")
                if not title_tag:
                    continue

                school_name = title_tag.get_text(strip=True)

                # Clean title variations
                if "College Navigator - " in school_name:
                    school_name = school_name.replace("College Navigator - ", "")
                if " | College Navigator" in school_name:
                    school_name = school_name.replace(" | College Navigator", "")
                school_name = school_name.strip()


                writer.writerow([school_id, school_name, state_code])
                print(f"Added: {school_id}, {school_name}, {state_code}")

                time.sleep(0.1)  # Respectful delay for school pages

            page_num += 1
            time.sleep(0.2)  # Delay between listing pages
