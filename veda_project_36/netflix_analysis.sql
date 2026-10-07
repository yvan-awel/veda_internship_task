-- Core aggregations used in the Netflix Trend Analysis

-- 1. Distribution of Movies vs TV Shows
SELECT 
    type, 
    COUNT(*) as count
FROM netflix_titles
GROUP BY type
ORDER BY count DESC;

-- 2. Content releases over the years (last 20 years)
SELECT 
    release_year, 
    type, 
    COUNT(*) as count
FROM netflix_titles
WHERE release_year >= 2000
GROUP BY release_year, type
ORDER BY release_year DESC;

-- 3. Top 10 Countries by content production
SELECT 
    TRIM(SUBSTRING_INDEX(country, ',', 1)) as primary_country, 
    COUNT(*) as count
FROM netflix_titles
WHERE country IS NOT NULL 
  AND country != ''
GROUP BY primary_country
ORDER BY count DESC
LIMIT 10;

-- 4. Top Genres
SELECT 
    TRIM(SUBSTRING_INDEX(listed_in, ',', 1)) as primary_genre, 
    COUNT(*) as count
FROM netflix_titles
GROUP BY primary_genre
ORDER BY count DESC
LIMIT 15;
