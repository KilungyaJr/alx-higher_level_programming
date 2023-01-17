#!/usr/bin/python3
"""
This module is used to get the last 10 commits of a repository
using the package requests and sys
"""
import requests
import sys

if __name__ == "__main__":
    repoName = sys.argv[1]
    owner = sys.argv[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repoName)
    response = requests.get(url)
    commits = response.json()[:10]
    for commit in commits:
        sha = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
