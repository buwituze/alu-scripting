#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """Reddit subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "My-User-Agent"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raises exception for HTTP errors
        data = response.json()
        return data['data']['subscribers']
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return 0  # Subreddit not found
        else:
            print(f"Error: {e}")
            return 0
    except Exception as e:
        print(f"Error: {e}")
        return 0
