#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of subscribers for a given subreddit.
If the subreddit is invalid, it returns 0.
"""

import requests

def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for the given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers of the subreddit, or 0 if the subreddit is invalid.
    """
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
