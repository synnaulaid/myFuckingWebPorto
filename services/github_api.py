import os
import requests

GITHUB_API = "https://api.github.com"
USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")

def _headers():
    h = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h

def get_repos(per_page=100):
    url = f"{GITHUB_API}/users/{USERNAME}/repos"
    params = {
        "sort": "updated",
        "direction": "desc",
        "per_page": per_page,
        # "type": "owner"  # kalau mau hanya repo milik sendiri
    }
    r = requests.get(url, headers=_headers(), params=params, timeout=20)
    r.raise_for_status()
    return r.json()

def get_user_events(limit=30):
    url = f"{GITHUB_API}/users/{USERNAME}/events/public"
    r = requests.get(url, headers=_headers(), params={"per_page": limit}, timeout=20)
    r.raise_for_status()
    return r.json()

def get_repo_detail(repo):
    url = f"{GITHUB_API}/repos/{USERNAME}/{repo}"
    r = requests.get(url, headers=_headers(), timeout=20)
    r.raise_for_status()
    return r.json()

def get_commits(repo, limit=20):
    url = f"{GITHUB_API}/repos/{USERNAME}/{repo}/commits"
    r = requests.get(url, headers=_headers(), params={"per_page": limit}, timeout=20)
    r.raise_for_status()
    return r.json()

def get_pull_requests(repo, state="open", limit=20):
    url = f"{GITHUB_API}/repos/{USERNAME}/{repo}/pulls"
    r = requests.get(url, headers=_headers(), params={"state": state, "per_page": limit}, timeout=20)
    r.raise_for_status()
    return r.json()
