# Kinesis Firehose Setup

This outlines how the streaming ingestion was set up.

## 🧩 Goal

Stream incoming JSON crime data into an S3 bucket:
s3://chicago-crime-stream-data/2025/



## 🔧 Steps

1. Open AWS Console → **Kinesis Firehose**
2. Create new Delivery Stream
   - Source: Direct PUT or other source
   - Destination: Amazon S3
   - Bucket: `chicago-crime-stream-data`
3. Enable compression (optional)
4. Buffer size: 5MB or every 60 seconds
5. (Optional) Add data transformation using Lambda
6. Start streaming data manually or from an external script

> For this demo, historical data was staged into the bucket as if it had arrived via Firehose.


