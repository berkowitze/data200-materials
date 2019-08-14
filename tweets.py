import requests
import nltk
import re
from collections import defaultdict
nltk.download('stopwords')

from nltk.corpus import stopwords
stops = set(stopwords.words('english'))
tweets = []
for year in range(2009, 2020):
    resp = requests.get(f'http://www.trumptwitterarchive.com/data/realdonaldtrump/{year}.json')
    tweets.append((year, resp.json()))

tweet_data = defaultdict(lambda: defaultdict(int))
# map of year -> (word -> count)
def process(text):
    words = []
    for word in re.split(r'[^\w]', text):
        if not word or word in stops:
            continue

        words.append(word.lower())

    return words
    # return [word.lower() for word in re.split(r'[^\w]', text) if word and word not in stops]

for year, twts in tweets:
    for twt in twts:
        for word in process(twt['text']):
            tweet_data[year][word] += 1

for year in tweet_data:
    print(year)
    top = sorted(list(tweet_data[year].items()), key=lambda x: -x[1])[:10]
    for word, freq in top:
        print(f'\t{word}:\t{freq}')

    print()

