import requests
from bs4 import BeautifulSoup
import os
import time

# Create output folder
SAVE_DIR = "docs"
os.makedirs(SAVE_DIR, exist_ok=True)

# 100+ medical topics (you can extend this list)
topics = {
    "Asthma": "https://medlineplus.gov/ency/article/000141.htm",
    "Anemia": "https://medlineplus.gov/ency/article/000560.htm",
    "Fever": "https://medlineplus.gov/ency/article/003090.htm",
    "Headache": "https://medlineplus.gov/ency/article/003024.htm",
    "Diabetes": "https://medlineplus.gov/ency/article/001214.htm",
    "Heart_Attack": "https://medlineplus.gov/ency/article/000195.htm",
    "Cancer": "https://medlineplus.gov/ency/article/001289.htm",
    "Flu": "https://medlineplus.gov/ency/article/000080.htm",
    "Vomiting": "https://medlineplus.gov/ency/article/003117.htm",
    "Diarrhea": "https://medlineplus.gov/ency/article/003126.htm",
    # Add more if needed...
}

def clean_filename(name):
    return name.replace(" ", "_").replace("/", "_")

def scrape_medlineplus_article(name, url):
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")

        content_div = soup.find("div", {"class": "main"})
        content_text = content_div.get_text(separator="\n", strip=True) if content_div else soup.get_text()

        file_path = os.path.join(SAVE_DIR, f"{clean_filename(name)}.txt")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content_text)

        print(f"✅ Saved: {name}")
        time.sleep(1)  # Be nice to the server
    except Exception as e:
        print(f"❌ Error scraping {name}: {e}")

# Scrape all topics
for name, url in topics.items():
    scrape_medlineplus_article(name, url)
