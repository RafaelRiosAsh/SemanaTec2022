from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd

#load data
file = "Spotify/data.csv"
df = pd.read_csv(file)

#choose two variables (liked, instrumentalness)
cdf = df[["instrumentalness", "liked"]]
cdf = cdf.dropna(axis=0, how= 'any')

#determine a k value based on the existing data, and a question you want an answer to
kmeans = KMeans(n_clusters=4).fit(cdf)

#using scikitlearn calculate the centers of the k-means algorithm
centroids = kmeans.cluster_centers_
print(centroids)
cla = kmeans.predict(cdf)

#show the graph
plt.xlabel("instrumentalness")
plt.ylabel("liked")
plt.scatter(cdf["instrumentalness"], cdf["liked"], c=cla)
for i in range(len(centroids)):
    plt.scatter(centroids[i][0], centroids[i][1], marker="*", c="red")
plt.show()