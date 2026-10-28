#!/usr/bin/env python3
"""
Reddit Community, Post, Comment & Search Data — Real-Time Synchronous REST API Quickstart (RapidAPI Hub & Zyla API Hub)
RapidAPI Hub: https://rapidapi.com/unitbytes/api/reddit-community-post-comment-search-data-api
Zyla API Hub: https://zylalabs.com/api-marketplace/social+media+%26+networking/reddit+community+post+comment+and+search+data+api/14529
Docs & Schema: https://unitbytes.com/actors/reddit-scraper/

Usage:
    pip install requests
    export RAPIDAPI_KEY="your_rapidapi_key"
    python examples/run_reddit_rapidapi.py
"""

import os
import requests

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY", "YOUR_RAPIDAPI_KEY")
if not RAPIDAPI_KEY or RAPIDAPI_KEY.startswith("YOUR_"):
    raise SystemExit("Please set your RapidAPI key: export RAPIDAPI_KEY='your_rapidapi_key'")

BASE_URL = "https://reddit-community-post-comment-search-data-api.p.rapidapi.com"
HEADERS = {
    "x-rapidapi-host": "reddit-community-post-comment-search-data-api.p.rapidapi.com",
    "x-rapidapi-key": RAPIDAPI_KEY,
}

# 1. Search Reddit across 5 tabs (posts, communities, people, media, comments)
resp = requests.get(
    f"{BASE_URL}/v1/reddit/search",
    headers=HEADERS,
    params={"query": "python", "tab": "posts", "sort": "relevance", "limit": 5},
    timeout=30,
)
resp.raise_for_status()
items = resp.json().get("data", {}).get("items", [])
print(f"Found {len(items)} Reddit posts:")
for post in items[:3]:
    print(f" - [{post.get('subreddit')}] {post.get('title')} (Score: {post.get('score')})")
