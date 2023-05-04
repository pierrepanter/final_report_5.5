from textblob import TextBlob
from collections import Counter
import pandas as pd
df = pd.read_excel('crawled data.csv')
lis = []
neg = 0.0
n = 0.0
net = 0.0
pos = 0.0
p = 0.0
count_all = Counter()
cout = 0
for content in enumerate(df['Content']):

        # Create a list with all the terms
        blob = TextBlob(str(content[1::]))
        cout += 1
        lis.append(blob.sentiment.polarity)
        # print blob.sentiment.subjectivity
        # print (os.listdir(tweet["text"]))
        if blob.sentiment.polarity > 0:
            sentiment = "negative"
            neg += blob.sentiment.polarity
            n += 1
        elif blob.sentiment.polarity == 0:
            sentiment = "neutral"
            net += 1
        else:
            sentiment = "positive"
            pos += blob.sentiment.polarity
            p += 1

        # output sentiment

print("Total tweets", len(lis))
print("Positive ", float(p / cout) * 100, "%")
print("Negative ", float(n / cout) * 100, "%")
print("Neutral ", float(net / len(lis)) * 100, "%")