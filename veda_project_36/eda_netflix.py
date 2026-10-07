import pandas as pd
import os

# Load dataset
df = pd.read_csv('netflix_titles.csv')

# 1. Distribution of Movies vs TV Shows
type_counts = df['type'].value_counts().reset_index()
type_counts.columns = ['Type', 'Count']
type_counts.to_csv('agg_type_counts.csv', index=False)

# 2. Content releases over the years (last 20 years)
recent_years = df[df['release_year'] >= 2000]
yearly_trend = recent_years.groupby(['release_year', 'type']).size().unstack(fill_value=0).reset_index()
yearly_trend.to_csv('agg_yearly_trend.csv', index=False)

# 3. Top 10 Countries by content production
# Some rows have multiple countries separated by commas, let's just take the first one (primary country)
df['primary_country'] = df['country'].apply(lambda x: str(x).split(',')[0] if pd.notnull(x) else 'Unknown')
top_countries = df[df['primary_country'] != 'Unknown']['primary_country'].value_counts().head(10).reset_index()
top_countries.columns = ['Country', 'Count']
top_countries.to_csv('agg_top_countries.csv', index=False)

# 4. Top Genres (listed_in)
# Explode the genres since they are comma-separated
df['genre'] = df['listed_in'].apply(lambda x: [g.strip() for g in str(x).split(',')])
df_exploded = df.explode('genre')
top_genres = df_exploded['genre'].value_counts().head(15).reset_index()
top_genres.columns = ['Genre', 'Count']
top_genres.to_csv('agg_top_genres.csv', index=False)

print("Aggregations completed and saved to CSV files.")
