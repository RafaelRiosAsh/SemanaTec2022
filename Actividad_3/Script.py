import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#load data
file = "Spotify/data.csv"

#select two columns that look interesting (danceabilty, acousticness)
df = pd.read_csv(file)

pd.set_option("display.max_rows", None, "display.max_columns", None)

print(df.columns)
    #show histogram
dance = df[df["danceability"]<=1]
acousticness = df[df["acousticness"] >= 0.0406]

dance.hist(column="danceability", grid=False, orientation="vertical", color = "coral")
plt.show()
acousticness.hist(column="acousticness", grid=True, orientation="vertical")
plt.show()

    #show box and whiskers diagrams
dance = df[df.danceability < 1]
acousticness = df[df.acousticness > 0.0406]
dance.boxplot(column=["danceability"], color = "green", showmeans=True )
plt.show()
acousticness.boxplot(column=["acousticness"], showmeans=True )
plt.show()

    #if there are outliers remove them and show the diagram again with the new data
    
#show the heat map of the correlations between all the numeric variables, choose the most appropiate visualization

sns.heatmap(df.corr(), annot=False, vmin=-1, vmax=1, cmap="cividis")
plt.show()
