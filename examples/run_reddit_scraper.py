#!/usr/bin/env python3
"""
Reddit Media & API Scraper: Posts, Users & Comments — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/reddit-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/reddit-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/reddit-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_reddit_scraper.py
"""

import os
from apify_client import ApifyClient

client = ApifyClient(os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN"))

run_input = {
    "startUrls": [],
    "searchQuery": "artificial intelligence",
    "subreddit": ""
}

run = client.actor("unitbytes/reddit-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("title"), item.get("url"), item.get("itemType"))
