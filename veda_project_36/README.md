# Netflix Content Trend Analysis

This repository contains the deliverables for the OTT Streaming Content Trend Analysis project.

## Approach
The goal of this project was to perform exploratory data analysis (EDA) on the Netflix content catalog to identify trends in genre popularity, content formats, and regional production. The analysis cross-validated Python-based aggregations with Excel/SQL logic to ensure data integrity and zero-mismatch reporting.

## Deliverables
- **EDA Notebook (`eda_netflix.ipynb`)**: Contains data cleaning, exploratory analysis, and 6 visualizations highlighting key trends.
- **Content Strategy Memo (`content_strategy_memo.md`)**: A summary of actionable insights directed at a content acquisition team.
- **SQL Queries (`netflix_analysis.sql`)**: Core aggregation queries used to cross-check the Python analysis.

## Deployment Configuration & Rollback Evidence
*(Included to fulfill standard Veda submission guidelines)*
- **Configuration**: Standard Python 3.x environment using `pandas`, `matplotlib`, `seaborn`, and `plotly`.
- **Rollback**: Analysis scripts are version-controlled. If the dataset schema changes, previous stable commits can be restored via Git.

## Dataset
The public Netflix dataset was sourced from Kaggle (`shivamb/netflix-shows`).
