## ☁️ Method 2: Streaming Analysis (Cloud)

This method showcases a cloud-native pipeline for analyzing 8M+ Chicago crime records.

**Pipeline:**
- Ingested data into S3 using Amazon Kinesis Firehose
- Queried raw JSON data directly from S3 using AWS Athena
- Built an interactive dashboard in AWS QuickSight replicating the official City of Chicago visuals
- Added a custom bar chart showing **districts with the most violent crimes between 8PM and 4AM**

📂 Folder: `method_2_streaming/`
