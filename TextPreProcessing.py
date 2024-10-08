import matplotlib.pyplot as plt
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import Word, TextBlob

df = pd.read_excel('amazon.xlsx')
df["Review"] = (df['Review'].str.lower())

# clearing text from punctuation
df["Review"] = df["Review"].str.replace('[^\w\s]', '', regex=True)
#print(df["Review"])

# clearing text from numbers
df["Review"] = df["Review"].str.replace('/d', '', regex=True)
#print(df["Review"].head(15))

# clearing text from stopwords
import nltk

nltk.download("stopwords")
swords = stopwords.words('english')
df["Review"]=df["Review"].apply(lambda x: " ".join(x for x in str(x).split() if x not in swords))
#print(df["Review"])



#clearing text from rarewords

temp_df =pd.Series(" ".join(df["Review"]).split()).value_counts()[-1000:]
#print(temp_df)
df["Review"]=df["Review"].apply(lambda x: " ".join(x for x in str(x).split() if x not in temp_df))
#print(df["Review"])


#lemmatization
nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()
df["Review"] = df["Review"].apply(lambda x: " ".join([lemmatizer.lemmatize(word) for word in x.split()]))
#print(df["Review"])














