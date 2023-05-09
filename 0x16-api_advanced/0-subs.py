#!/usr/bin/python3
""" retrieves number of subscribers from subreddit"""

import requests


def number_of_subscribers(subreddit):
    """returns number of subscribers"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "My Browser"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        subscribers = data.get("data").get("subscribers")
        return subscribers
    else:
        return 0
