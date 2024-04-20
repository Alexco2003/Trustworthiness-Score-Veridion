import requests
import re
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from instascrape import Profile, scrape_posts

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

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        # print(soup.get_text().lower())
        #print(rem(soup.get_text()))

        text = soup.get_text()
        last_post_date = extract_time_from_last_post(rem(text))
        follower_count = extract_followers(text)

        return (follower_count, last_post_date)

    return None
def rem(text):
    text =text.strip()
    text = re.sub(r'\s+', ' ',text)
    return text


def main():
    #print(scrap_linkedin_followers("https://www.linkedin.com/company/ubisoft/"))
    #print(scrap_linkedin_followers("https://www.linkedin.com/company/xarvio"))
    #print(scrap_linkedin_followers("https://www.linkedin.com/company/ubisoft"))
    print(scrap_linkedin("https://www.linkedin.com/company/knoweaformation"))
    #scrap_instagra_followers("https://www.instagram.com/skpha_/")


if __name__ == "__main__":
    main()