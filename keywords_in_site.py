import requests
import nltk
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from collections import defaultdict

def word_frequency(text):
    # Load the English stopwords
    stop_words = set(stopwords.words('english'))

    # Tokenize the text into words
    words = nltk.word_tokenize(text.lower())

    # Create a defaultdict to store word frequencies
    word_freq = defaultdict(int)

    # Iterate through the words and count their frequencies
    for word in words:
        # Check if the word is not a stopword and is alphabetic
        if word not in stop_words and word.isalpha():
            word_freq[word] += 1

    return dict(word_freq)

# Set User-Agent header
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

def keywords_in_site(url,keywords):
    keyword_set = set([word.lower() for phrase in keywords for word in phrase.split()])
    # Create a session
    with requests.Session() as session:
        # Make the GET request
        response = session.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the HTML content
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract text content from the page
            page_text = soup.get_text()

            freq = word_frequency(page_text)
            print(freq)
            for word in keyword_set:
                if word.lower() in freq:
                    print(word)
        else:
            print("Failed to retrieve the webpage. -Status code:", response.status_code)

def main():
    keywords = ['Fruit And Vegetables', 'Fresh Fruit & Vegetables',
                'Food Processing Company', 'Farmers & Producers', 'Computer Software',
                'Incubators & Accelerators', 'Agriculture', 'Machine Learning', 'Machinery','Robotics'
                ]

    url = "https://www.agrograde.com/"
    keywords_in_site(url, keywords)


if __name__ == "__main__":
    main()