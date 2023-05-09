#!/usr/bin/python3
"""
a function that queries the Reddit API
and prints the titles of the first 10 hot posts listed for a given subreddit.

Requirements:
    Prototype: def top_ten(subreddit)
    If not a valid subreddit, print None.
NOTE: Invalid subreddits may return a redirect to search results.
Ensure that you are not following redirects.
"""

import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {"User-Agent": "My Browser"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()

        for post in posts['data']['children']:
            print(post['data']['title'])
    else:
        print("None")
