import requests
from bs4 import BeautifulSoup
url = "https://www.bbc.com/news"
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    headlines = soup.find_all("h2")
    print("\n===== BBC NEWS HEADLINES =====\n")
    for index, item in enumerate(headlines, start=1):
        title = item.get_text(strip=True)
        if title:
            print(index, title)
except requests.exceptions.RequestException as e:
    print("Error:", e)
    