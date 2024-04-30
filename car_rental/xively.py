import time
from xively import XivelyAPIClient, Datapoint

# Xively API key and feed ID
API_KEY = 'YOUR_API_KEY'
FEED_ID = 'YOUR_FEED_ID'

# Create Xively client
client = XivelyAPIClient(API_KEY)

# Get feed
feed = client.feeds.get(FEED_ID)

# Create a new datapoint
datapoint = Datapoint(value=42)  # Change the value to the data you want to send


feed.datapoints.create(datapoint)

print("Data sent to Xively cloud.")
