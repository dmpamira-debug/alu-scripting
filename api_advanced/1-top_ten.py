#!/usr/bin/python3
"""Module that queries the Reddit API."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            print(None)
            return

        posts = response.json()["data"]["children"]

        for post in posts:
            print(post["data"]["title"])

    except Exception:
        print(None)
