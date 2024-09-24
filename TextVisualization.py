import TextPreProcessing
from TextPreProcessing import df
import pandas as pd
import matplotlib.pyplot as plt

#Calculate Frequence of "Review"
tf=df["Review"].apply(lambda x: pd.Series(x.split(" ")).value_counts()).sum(axis=0).reset_index()
#print(tf)
tf.columns = ["words","tf"]
#print(tf)



