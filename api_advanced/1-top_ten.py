#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    If the subreddit is invalid, prints None.
    """
    url = "https://old.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }
    params = {"limit": 10}

    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
    except requests.exceptions.RequestException:
        print(None)
        return

    if response.status_code != 200:
        print(None)
        return

    try:
        results = response.json().get("data").get("children")
    except (AttributeError, ValueError):
        print(None)
        return

    if not results:
        print(None)
        return

    for post in results[:10]:
        print(post.get("data").get("title"))

