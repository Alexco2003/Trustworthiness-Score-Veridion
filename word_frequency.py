import nltk
from nltk.corpus import stopwords
from collections import defaultdict

# nltk.download('punkt')


# Load the English stopwords
stop_words = set(stopwords.words('english'))


def word_frequency(text):
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


# Example text
text = "This is a sample text with some sample words. We want to count the frequency of each word in this text."

# Get word frequency dictionary
frequency_dict = word_frequency(text)

# Print the word frequency dictionary
print(frequency_dict)
