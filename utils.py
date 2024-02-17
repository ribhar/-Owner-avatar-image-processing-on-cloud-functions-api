# Function to print a list of blobs in a Google Cloud
# Storage bucket.

import sys
import google.cloud.storage as storage

def list_blobs(bucket_name='gcp_experiment_bucket'):
    """Lists all the blobs in the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    blobs = bucket.list_blobs()

    for blob in blobs:
        print(blob.name)

if __name__ == "__main__":
    list_blobs()

# [END storage_list_buckets]
