#!/usr/bin/python3
"""
Queries the Reddit API and prints the titles of the first
10 hot posts for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "python:reddit.api:v1.0 (by /u/reddit_api)"
    }
    params = {
        "limit": 10
    }

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )

        if response.status_code != 200:
            print("None")
            return

        results = response.json().get("data", {}).get("children", [])

        if not results:
            print("None")
            return

        for post in results:
            print(post.get("data").get("title"))

    except requests.RequestException:
        print("None")
