import requests
import re
import numpy as np
from bs4 import BeautifulSoup

# HELPER, DONT TOUCH
def extract_followers(html):
    # Define a regular expression pattern to match the followers count
    pattern = r'(\d{1,3}(,\d{3})*|\d+)\s*followers'

    # Search for the pattern in the HTML content
    match = re.search(pattern, html)

    if match:
        # Extract the matched followers count
        followers_count = match.group(1)
        # Remove any commas from the count
        followers_count = followers_count.replace(',', '')
        # Convert the count to an integer
        followers_count = int(followers_count)
        return followers_count
    else:
        return None

def extract_time_from_last_post(html):
    pattern = r'followers (\d+[hdwm])\b'

    # Search for the pattern in the HTML content
    match = re.search(pattern, html)

    if match:
        # Extract the matched followers count
        followers_count = match.group(1)
        # Remove any commas from the count
        followers_count = followers_count.replace(',', '')
        return followers_count
    else:
        return None


# Takes the URL to a linkedin profile
# Returns (No. followers, time from last post)
def scrap_linkedin(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
    }

    if url is None:
        return 0
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        text = soup.get_text()
        last_post_date = extract_time_from_last_post(removeWhitespace(text))
        follower_count = extract_followers(text)

        latestPostScore = 0
        if last_post_date is not None:
            if 'h' in last_post_date:
                latestPostScore = 100
            elif 'd' in last_post_date:
                latestPostScore = 80
            elif 'w' in last_post_date:
                latestPostScore = 50
            elif 'm' in last_post_date:
                latestPostScore = 20
            elif 'y' in last_post_date:
                latestPostScore = 10

        if follower_count is None:
            return 0

        if follower_count > 100_000:
            return 0.5 + latestPostScore / 200

        if follower_count > 10_000:
            return 0.25 + latestPostScore / 200

        if follower_count > 1_000:
            return 0.1 + latestPostScore / 200

        return  latestPostScore / 200

    return 0
def removeWhitespace(text):
    text =text.strip()
    text = re.sub(r'\s+', ' ',text)
    return text

