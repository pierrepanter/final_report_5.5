import pandas as pd
from nltk.corpus import stopwords
from textblob import Word, TextBlob
from wordcloud import WordCloud
import nltk
import matplotlib.pyplot as plt
df = pd.read_csv('process.csv')
df["Content"] = df["Content"].apply(lambda x:" ".join(x.lower() for x in x.split()))#Convert to lowercase
df["Content"] = df["Content"].str.replace("\d","")#Removing numerical values
df["Content"] = df["Content"].str.replace("[^\w\s]","")#Removing punctations
sw = stopwords.words("english")
df["Content"] = df["Content"].apply(lambda x: " ".join(x for x in x.split() if x not in sw))
df["Content"] = df["Content"].apply(lambda x: " ".join([Word(x).lemmatize()]))
df["tokens"] = df["Content"].apply(lambda x: TextBlob(x).words)
text = " ".join(i for i in df.Content)
token = nltk.sent_tokenize(text, language="english")
token = "".join(i for i in token)
wordcloud = WordCloud(
    background_color="#6B5B95",
    colormap="Set2",
    collocations=False).generate(token)

plt.figure(figsize=[11,11])
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Visualization result")
plt.show()
"""
df.drop("Name", axis=1, inplace=True)
df.drop("User Name", axis=1, inplace=True)
df.drop("UTC", axis=1, inplace=True)
df.drop("Language", axis=1, inplace=True)
"""
"""data=[]
regex_str = [
        r'<[^>]+>',  # HTML tags
        r'(?:@[\w_]+)',  # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

        r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
        r'(?:[\w_]+)',  # other words
        r'(?:\S)'  # anything else
    ]
word_tokens = word_tokenize(text.strip())
clean_text = df["Content"].str.replace("regex_str","")
filter_text = [word for word in clean_text if word not in stopwords.words('english') ]"""

