import requests
import pandas as pd
from urllib.parse import urlparse
from time import sleep

# Load your CSV file
df = pd.read_csv('input/url_list.csv')  # Update with the path to your downloaded CSV file

# Define a function to resolve a URL to its final destination
def resolve_url(url):
    try:
        response = requests.get(url, timeout=10)  # GET request to follow redirects
        return response.url
    except requests.RequestException as e:
        return str(e)

# Resolve URLs with a delay between requests to avoid overwhelming servers
resolved_urls = []
for url in df['List A']:
    resolved_url = resolve_url(url)
    resolved_urls.append(resolved_url)
    print('working...')
    sleep(1)  # Sleep for 1 second between requests

# Add the resolved URLs to your DataFrame
df['List B'] = resolved_urls

# Save the updated DataFrame to a new CSV file
df.to_csv('output/resolved_url_list.csv', index=False)
