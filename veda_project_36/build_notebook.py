import nbformat as nbf

nb = nbf.v4.new_notebook()

text_intro = """\
# Netflix Exploratory Data Analysis
This notebook explores the Netflix content catalog to identify trends in formats (Movies vs TV Shows), release years, top producing countries, and popular genres.
"""

code_setup = """\
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('netflix_titles.csv')
df.head()
"""

code_clean = """\
# Basic Cleaning
df['primary_country'] = df['country'].apply(lambda x: str(x).split(',')[0] if pd.notnull(x) else 'Unknown')
df_recent = df[df['release_year'] >= 2000]
"""

code_viz1 = """\
# 1. Movies vs TV Shows
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='type', palette='Set2')
plt.title('Distribution of Movies vs TV Shows')
plt.show()
"""

code_viz2 = """\
# 2. Content releases over the last 20 years
plt.figure(figsize=(12, 6))
sns.countplot(data=df_recent, x='release_year', hue='type', palette='Set1')
plt.title('Content Releases by Year (2000+)')
plt.xticks(rotation=45)
plt.show()
"""

code_viz3 = """\
# 3. Top 10 Producing Countries
top_countries = df[df['primary_country'] != 'Unknown']['primary_country'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(y=top_countries.index, x=top_countries.values, palette='viridis')
plt.title('Top 10 Content Producing Countries')
plt.show()
"""

code_viz4 = """\
# 4. Ratings Distribution
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='rating', order=df['rating'].value_counts().index, palette='magma')
plt.title('Distribution of Content Ratings')
plt.show()
"""

code_viz5 = """\
# 5. Top 15 Genres
df['genre'] = df['listed_in'].apply(lambda x: [g.strip() for g in str(x).split(',')])
df_exploded = df.explode('genre')
top_genres = df_exploded['genre'].value_counts().head(15)

plt.figure(figsize=(10, 6))
sns.barplot(y=top_genres.index, x=top_genres.values, palette='cubehelix')
plt.title('Top 15 Most Common Genres')
plt.show()
"""

code_viz6 = """\
# 6. Duration Analysis (Movies)
movies = df[df['type'] == 'Movie'].copy()
# Extract integer from duration e.g. "90 min"
movies['duration_min'] = movies['duration'].str.extract('(\\d+)').astype(float)

plt.figure(figsize=(10, 5))
sns.histplot(movies['duration_min'], bins=30, kde=True, color='teal')
plt.title('Distribution of Movie Durations (minutes)')
plt.show()
"""

nb['cells'] = [
    nbf.v4.new_markdown_cell(text_intro),
    nbf.v4.new_code_cell(code_setup),
    nbf.v4.new_code_cell(code_clean),
    nbf.v4.new_code_cell(code_viz1),
    nbf.v4.new_code_cell(code_viz2),
    nbf.v4.new_code_cell(code_viz3),
    nbf.v4.new_code_cell(code_viz4),
    nbf.v4.new_code_cell(code_viz5),
    nbf.v4.new_code_cell(code_viz6)
]

nbf.write(nb, 'eda_netflix.ipynb')
print("Notebook eda_netflix.ipynb created successfully.")
