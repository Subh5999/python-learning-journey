import matplotlib.pyplot as plt
import pandas as pd
import os

# Get dataset path
folder = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(folder, "netflix_titles.csv")

# Load dataset
data = pd.read_csv(csv_path)

# Display basic information
print("NETFLIX DATASET ANALYSIS")

print("\nFirst 5 Records:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nColumn Names:")
print(data.columns.tolist())

print("\nDataset Information:")
print(data.info())
# Check missing values
print("\nMISSING VALUES ANALYSIS")

missing_values = data.isnull().sum()

print(missing_values)

print("\nTotal Missing Values:")
print(missing_values.sum())
# Calculate missing value percentage

missing_percentage = (
    data.isnull().sum() / len(data)
) * 100

print("\nMISSING VALUE PERCENTAGE")

print(missing_percentage.sort_values(ascending=False))
# Handle missing values

data["country"] = data["country"].fillna("Unknown")
data["rating"] = data["rating"].fillna("Not Rated")
data["duration"] = data["duration"].fillna("Unknown")

print("\nMISSING VALUES AFTER CLEANING")
print(data.isnull().sum())

print("\nTotal Missing Values After Cleaning:")
print(data.isnull().sum().sum())
print("\nREMAINING MISSING VALUES")

remaining_missing = data.isnull().sum()

print(remaining_missing[remaining_missing > 0])
# Handle remaining missing values

data["director"] = data["director"].fillna("Unknown")

data["cast"] = data["cast"].fillna("Unknown")

data["date_added"] = data["date_added"].fillna("Not Available")

# Check missing values again

print("\nFINAL DATA CLEANING REPORT")

print(data.isnull().sum())

print("\nTotal Missing Values:")
print(data.isnull().sum().sum())
# Movies vs TV Shows Analysis

print("\nMOVIES VS TV SHOWS ANALYSIS")

content_count = data["type"].value_counts()

print(content_count)

print("\nPercentage Distribution:")

content_percentage = data["type"].value_counts(normalize=True) * 100

print(content_percentage.round(2))

# Movies vs TV Shows Bar Chart

plt.figure(figsize=(8, 5))

content_count.plot(kind="bar")

plt.title("Netflix Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Number of Titles")

plt.xticks(rotation=0)
plt.tight_layout()

# Save chart
chart_path = os.path.join(folder, "content_distribution.png")
plt.savefig(chart_path)

plt.show()

print("\nChart saved successfully!")
# Top 10 Countries Analysis

print("\nTOP 10 COUNTRIES ON NETFLIX")

country_count = (
    data["country"]
    .str.split(",")
    .explode()
    .str.strip()
)

top_countries = country_count.value_counts().head(10)

print(top_countries)
plt.figure(figsize=(10, 6))

top_countries.plot(kind="bar")

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Country")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    os.path.join(folder, "top_10_countries.png")
)

plt.show()
# Content Release Year Analysis

print("\nCONTENT RELEASE YEAR ANALYSIS")

year_count = data["release_year"].value_counts().sort_index()

print("\nLatest 10 Years:")
print(year_count.tail(10))
plt.figure(figsize=(12, 5))

year_count.plot(kind="line")

plt.title("Netflix Content Release by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(folder, "release_year_analysis.png")
)

plt.show()
# Movie Duration Analysis

print("\nMOVIE DURATION ANALYSIS")

movies = data[data["type"] == "Movie"].copy()

movies["duration_minutes"] = (
    movies["duration"]
    .str.extract(r"(\d+)")
    .astype(float)
)

print("\nAverage Movie Duration:")
print(movies["duration_minutes"].mean())

print("\nLongest Movie:")
print(movies["duration_minutes"].max())

print("\nShortest Movie:")
print(movies["duration_minutes"].min())
# Genre Analysis

print("\nTOP 10 NETFLIX GENRES")

genre_count = (
    data["listed_in"]
    .str.split(",")
    .explode()
    .str.strip()
)

top_genres = genre_count.value_counts().head(10)

print(top_genres)
plt.figure(figsize=(10, 6))

top_genres.plot(kind="bar")

plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    os.path.join(folder, "top_10_genres.png")
)

plt.show()
plt.figure(figsize=(10, 6))

top_genres.plot(kind="bar")

plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(folder, "top_10_genres.png"))
plt.show()
plt.figure(figsize=(10, 6))
top_genres.plot(kind="bar")

plt.title("Top 10 Netflix Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig(os.path.join(folder, "top_10_genres.png"))
plt.show()