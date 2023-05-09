#!/usr/bin/python3
"""
a recursive function that queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit.
If no results are found for the given subreddit,
the function should return None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API recursively"""

    url = "https://www.reddit.com/r/{}/hot.json?limit=50&after={}".format(subreddit, after)
    headers = {'User-Agent': 'My Browser'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        posts = response.json()
        after = posts['data']['after']

        for post in posts['data']['children']:
            hot_list.append(post['data']['title'])
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
