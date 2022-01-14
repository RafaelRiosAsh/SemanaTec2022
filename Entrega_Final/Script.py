import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.cluster import KMeans

#load data
file = "DATA/data.csv"
df = pd.read_csv(file)

'''
Primer apartado de Actividad - familiarización con el dataset elegido
'''

#show number of variables and amount of data
print(f"number of columns: {len(df.columns)}")
print(f"number of rows: {len(df)}")

#show column name
print(f"column names: ")
for var in df.columns:
    print(var, end= ", ")

#show data types
print(f"\ntypes of data:\n{df.dtypes}")
#choose two columns (energy, duration_ms)
print("chosen columns: energy and duration")
    #show unique values
print(f"unique values in energy:")
energy_values = df.energy.unique()
energy_values.sort()
for value in energy_values:
    print(value)

print(f"unique values in duration:")
duration_values = df.duration_ms.unique()
duration_values.sort()
for value in duration_values:
    print(value)

    #show maximum and minimum values
print(f"maximum value in price {energy_values.max()}, minimum value in price {energy_values.min()}")
print(f"maximum value in year {duration_values.max()}, minimum value in year {duration_values.min()}")

    #show media, mediana and standard deviation
print("energy:")
print(f"    media: {df.energy.mean()}")
print(f"    mediana: {df.energy.median()}")
print(f"    deviacion estandar: {df.energy.std()}")

print("duration:")
print(f"    media: {df.duration_ms.mean()}")
print(f"    mediana: {df.duration_ms.median()}")
print(f"    deviacion estandar: {df.duration_ms.std()}")

'''
Segundo apartado de Actividad - Análisis de datos inicial e identificación de variables relevantes
'''

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

'''
Tercer apartado de Actividad - Análisis de datos avanzado y derivación de conclusiones en base a resultados
'''

#choose two variables (loudness, energy)
cdf = df[["energy", "loudness"]]
cdf = cdf.dropna(axis=0, how= 'any')

#determine a k value based on the existing data, and a question you want an answer to
kmeans = KMeans(n_clusters=4).fit(cdf)

#using scikitlearn calculate the centers of the k-means algorithm
centroids = kmeans.cluster_centers_
print(centroids)
cla = kmeans.predict(cdf)

#show the graph
plt.xlabel("energy")
plt.ylabel("loudness")
plt.scatter(cdf["energy"], cdf["loudness"], c=cla)
for i in range(len(centroids)):
    plt.scatter(centroids[i][0], centroids[i][1], marker="*", c="red")
plt.show()