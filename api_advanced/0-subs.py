#!/usr/bin/python3
"""0-subs.py"""

import requests

def number_of_subscribers(subreddit):
    """Retrieve the number of subscribers for the given subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0

if __name__ == "__main__":
    # Test cases
    print(number_of_subscribers("existing_subreddit"))
    print(number_of_subscribers("nonexisting_subreddit"))
