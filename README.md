# Chicago Crime ETL Analysis

This project showcases two distinct methods for analyzing 8M+ rows of Chicago crime data from the City of Chicago public dataset.

---

## 📦 Method 1: Batch Analysis (Local Python)

Streams the dataset in 200K-row batches using the Socrata OData API, processes each batch locally, and aggregates key crime statistics using memory-efficient techniques.

- Implemented in Python with Pandas and Counter objects
- Notebook-based exploration
- Visualized using a local Streamlit dashboard

📁 Folder: `method_1_batching/`

---

## ☁️ Method 2: Streaming Analysis (Cloud)

A cloud-native pipeline using AWS tools to ingest, query, and visualize public crime data.

- Data streamed (or staged) into S3 using Firehose
- Athena queries run directly on raw JSON in S3
- Visualized using QuickSight to replicate the official City of Chicago dashboard
- Custom visual: bar chart of violent nighttime crime by district

📁 Folder: `method_2_streaming/`

---

## 🔧 Tools & Technologies
- Python, Pandas, Streamlit
- AWS S3, Athena, QuickSight, Kinesis Firehose
- SQL

---

## 🧑‍💻 Author
Mahmood Elkhatib
