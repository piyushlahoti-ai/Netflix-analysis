import pandas as pd
#Load dataset
df = pd.read_csv(r"C:\Users\Piyush\OneDrive\Desktop\Netflix analysis\NetFlix.csv")

#printing first 5 rows
print(df.head())

#show data information
print(df.info())

#checking for missing values 
print(df.isnull().sum())


print(df["type"].value_counts())

#cheking top 10 ratings
print(df["rating"].value_counts().head(10))

#cheking top 10 countries
print(df["country"].value_counts().head(10))

#filtering movies released after 2020
recent_movies = df[df["release_year"] > 2020]
print(recent_movies[["title", "release_year"]])

#finding longest movie
movies = df[df["type"] == "Movie"]
print(movies["duration"].head(1))

import matplotlib.pyplot as plt

df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.show()





























