# Method 1: Batch Analysis (Local)

This folder contains a memory-efficient batch processing workflow for analyzing ~8.3M rows of public crime data from the City of Chicago.

## 🔁 Approach

- Streams the dataset in 200,000-row batches using the Socrata OData API
- Aggregates crime statistics using `collections.Counter` without loading the full dataset into memory
- Preserves original outputs for reproducibility (API is now deprecated)

## 📊 Visuals

- Streamlit dashboard created using final aggregated `.pkl` file
- Dashboard includes:
  - Crime count by year
  - Top 10 crime types
  - Arrest distribution
  - Crimes by district
  - Crimes by hour of day
  - Monthly crime trends (optional)

## 📁 Structure

- `notebooks/`: Original batch notebook (preserved snapshot)
- `data/`: Aggregated outputs as `.pkl`
- `dashboard/`: Streamlit app displaying visual summaries
