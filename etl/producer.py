import requests
import boto3
import time
import json
from datetime import datetime

# 🔷 CONFIGURATION
FIREHOSE_STREAM_NAME = 'chicago-crime-firehose'  #  Firehose stream name
SOCRATA_ENDPOINT = 'https://data.cityofchicago.org/resource/ijzp-q8t2.json'

MAX_ROWS = 10_000_000    # Stop after this many rows
MAX_BYTES = 10 * 1024 * 1024 * 1024  # Stop after ~10GB
POLL_INTERVAL = 0  # seconds between API calls
BATCH_SIZE = 200_000  # records per API call

# 🔷 STATE
rows_sent = 0
bytes_sent = 0
last_timestamp = None  # will hold the most recent datetime of ingested record

# 🔷 AWS CLIENT
firehose = boto3.client('firehose')

def fetch_new_records(last_ts, limit=BATCH_SIZE):
    """Fetch records newer than last_ts"""
    params = {
        '$order': 'date ASC',
        '$limit': limit
    }
    if last_ts:
        params['$where'] = f"date > '{last_ts}'"
    r = requests.get(SOCRATA_ENDPOINT, params=params)
    r.raise_for_status()
    data = r.json()
    return data

def estimate_size(records):
    """Estimate byte size of JSON records"""
    return sum(len(json.dumps(r).encode('utf-8')) for r in records)

def send_to_firehose(records):
    """Send records to Firehose in batches"""
    BATCH_MAX = 500  # Firehose max per batch API call
    for i in range(0, len(records), BATCH_MAX):
        batch = records[i:i+BATCH_MAX]
        response = firehose.put_record_batch(
            DeliveryStreamName=FIREHOSE_STREAM_NAME,
            Records=[
                {'Data': json.dumps(r) + '\n'} for r in batch
            ]
        )
        if response.get('FailedPutCount', 0) > 0:
            print(f"Warning: {response['FailedPutCount']} records failed to send.")


print("Starting producer...")

while rows_sent < MAX_ROWS and bytes_sent < MAX_BYTES:
    print(f"Polling API after timestamp: {last_timestamp}")
    batch = fetch_new_records(last_timestamp)

    if not batch:
        print("No new records yet. Waiting...")
        time.sleep(POLL_INTERVAL)
        continue

    # Send to Firehose
    send_to_firehose(batch)

    # Update counters
    batch_bytes = estimate_size(batch)
    rows_sent += len(batch)
    bytes_sent += batch_bytes

    print(f"Sent {len(batch)} records ({batch_bytes/1024:.2f} KB). "
          f"Total: {rows_sent} rows, {bytes_sent/1024/1024:.2f} MB")

    # Update last timestamp
    last_timestamp = batch[-1]['date']

    # Respect polling interval
    time.sleep(POLL_INTERVAL)

print("Threshold reached. Stopping ingestion.")
print(f"Final: {rows_sent} rows, {bytes_sent/1024/1024:.2f} MB")
