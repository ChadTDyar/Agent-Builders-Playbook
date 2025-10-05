import requests
from bs4 import BeautifulSoup

def get_profile_info(url, cookie):
    headers = {"cookie": cookie, "User-Agent": "Mozilla/5.0"}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        return {"error": "Failed to fetch profile"}
    soup = BeautifulSoup(resp.text, "html.parser")
    # Dummy extraction for example
    name = soup.title.string if soup.title else "Unknown"
    return {"name": name, "url": url}
