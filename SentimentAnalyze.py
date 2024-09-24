import TextPreProcessing
from TextPreProcessing import df
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


print(df['Review'].head())
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
df['Review'][0:10].apply(lambda x: sia.polarity_scores(x))
df['Review'][0:10].apply(lambda x: sia.polarity_scores(x)["compound"])
df['polarity_score'] = df['Review'].apply(lambda x: sia.polarity_scores(x)["compound"])
print(df['polarity_score'])