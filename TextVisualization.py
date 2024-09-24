import TextPreProcessing
from TextPreProcessing import df
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

#Calculate Frequence of "Review"
tf=df["Review"].apply(lambda x: pd.Series(x.split(" ")).value_counts()).sum(axis=0).reset_index()
#print(tf)
tf.columns = ["words","tf"]
#print(tf)

#barplot visualization
print(df['Review'])
tf[tf["tf"]>500].plot.bar(x="words", y="tf")
plt.show()

#####
text=" ".join(i for i in df.Review)
wordcloud=WordCloud().generate(text)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
wordcloud.to_file("wordcloud.png")
