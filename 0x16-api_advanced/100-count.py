#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces.
Javascript should count as javascript, but java should not)
"""

import requests


def count_words(subreddit, word_list, after="", word_dic={}):
    """
    Returns a list containing the titles of all hot articles for a
    given subreddit. If no results are found for the given subreddit,
    the function should return None.
    """
    if not word_dic:
        for word in word_list:
            word_dic[word] = 0

    if after is None:
        word_list = [[key, value] for key, value in word_dic.items()]
        word_list = sorted(word_list, key=lambda x: (-x[1], x[0]))
        for wrd in word_list:
            if wrd[1]:
                print("{}: {}".format(wrd[0].lower(), wrd[1]))
        return None

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'user-agent': 'My Browser'}

    params = {
        'limit': 100,
        'after': after
    }

    res = requests.get(
        url, headers=headers, params=params, allow_redirects=False)

    if res.status_code != 200:
        return None

    try:
        js = res.json()

    except ValueError:
        return None

    try:

        data = js.get("data")
        after = data.get("after")
        children = data.get("children")
        for child in children:
            post = child.get("data")
            title = post.get("title")
            lower = [s.lower() for s in title.split(' ')]

            for wrd in word_list:
                word_dic[wrd] += lower.count(wrd.lower())

    except Exception:
        return None

    count_words(subreddit, word_list, after, word_dic)
