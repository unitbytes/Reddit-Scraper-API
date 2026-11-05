#!/usr/bin/env python3
"""
Reddit Comments Scraper: Comment Trees, Replies & Sentiment — Official Python SDK Quickstart
Actor: https://apify.com/unitbytes/reddit-comments-scraper?fpr=939u3w&fp_sid=gh_py
Docs & Schema: https://unitbytes.com/actors/reddit-comments-scraper/
n8n Template: https://unitbytes.com/n8n/workflows/reddit-comments-scraper-n8n-workflow.json

Usage:
    pip install apify-client
    export APIFY_API_TOKEN="your_apify_api_token"
    python examples/run_reddit_comments_scraper.py
"""

import os
from apify_client import ApifyClient

APIFY_TOKEN = os.getenv("APIFY_API_TOKEN", "YOUR_APIFY_API_TOKEN")
if not APIFY_TOKEN or APIFY_TOKEN.startswith("YOUR_"):
    raise SystemExit("Please set your Apify API token: export APIFY_API_TOKEN='apify_api_...'")

client = ApifyClient(APIFY_TOKEN)

run_input = {
    "startUrls": [
        {
            "url": "https://www.reddit.com/r/technology/comments/1x0b0f5/fraudster_jailed_for_using_10k_bots_and_ai_songs/"
        }
    ],
    "maxCommentsPerPost": 100
}

run = client.actor("unitbytes/reddit-comments-scraper").call(run_input=run_input)

for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item.get("itemType"), item.get("postId"), item.get("author"))
