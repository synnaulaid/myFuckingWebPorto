# services/github_api.py
import os
import requests
from datetime import datetime

GITHUB_API = "https://api.github.com"
USERNAME = os.getenv("GITHUB_USERNAME")
TOKEN = os.getenv("GITHUB_TOKEN")

def _headers():
    h = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        h["Authorization"] = f"Bearer {TOKEN}"
    return h

def _iso(dt: str) -> datetime:
    return datetime.fromisoformat(dt.replace('Z', '+00:00'))

# ---------------- Core fetchers ----------------
def get_repos(per_page=100):
    url = f"{GITHUB_API}/users/{USERNAME}/repos"
    params = {"sort": "updated", "direction": "desc", "per_page": per_page}
    r = requests.get(url, headers=_headers(), params=params, timeout=20)
    r.raise_for_status()
    return r.json()

def get_user_events(limit=30):
    url = f"{GITHUB_API}/users/{USERNAME}/events/public"
    r = requests.get(url, headers=_headers(), params={"per_page": limit}, timeout=20)
    r.raise_for_status()
    return r.json()

def get_org_events(org, limit=30):
    url = f"{GITHUB_API}/orgs/{org}/events"
    r = requests.get(url, headers=_headers(), params={"per_page": limit}, timeout=20)
    r.raise_for_status()
    return r.json()

def get_repo_detail(repo):
    if "/" in repo:
        owner, name = repo.split("/", 1)
    else:
        owner, name = USERNAME, repo
    url = f"{GITHUB_API}/repos/{owner}/{name}"
    r = requests.get(url, headers=_headers(), timeout=20)
    r.raise_for_status()
    return r.json()

def get_commits(repo, limit=20):
    if "/" in repo:
        owner, name = repo.split("/", 1)
    else:
        owner, name = USERNAME, repo
    url = f"{GITHUB_API}/repos/{owner}/{name}/commits"
    r = requests.get(url, headers=_headers(), params={"per_page": limit}, timeout=20)
    r.raise_for_status()
    return r.json()

def get_pull_requests(repo, state="open", limit=20):
    if "/" in repo:
        owner, name = repo.split("/", 1)
    else:
        owner, name = USERNAME, repo
    url = f"{GITHUB_API}/repos/{owner}/{name}/pulls"
    r = requests.get(url, headers=_headers(), params={"state": state, "per_page": limit}, timeout=20)
    r.raise_for_status()
    return r.json()

# ---------------- Merge & tree builder ----------------
def merge_user_and_org_events(orgs: list[str] | None = None, limit=40):
    events = get_user_events(limit=limit)
    if orgs:
        for org in orgs:
            try:
                events += get_org_events(org, limit=limit)
            except Exception:
                pass
    
    events.sort(key=lambda x: x.get("created_at",""), reverse=True)
    seen = set()
    uniq = []
    for e in events:
        eid = e.get("id")
        if eid and eid in seen:
            continue
        if eid: seen.add(eid)
        uniq.append(e)
    return uniq

def treeify_events(events, per_commit_fetch_limit=5):
    """
    Bentuk data siap render tree:
    [
      {
        "type": "...",
        "repo": "owner/name",
        "created_at": "...",
        "commits": [ { author, message, sha, url, date (pakai created_at event) }, ... ]
      }
    ]
    """
    out = []
    for e in events:
        etype = e.get("type")
        repo_name = (e.get("repo") or {}).get("name", "")
        created_at = e.get("created_at")
        actor = (e.get("actor") or {}).get("login", "")
        commits = []
        if etype == "PushEvent":
            payload_commits = (e.get("payload") or {}).get("commits") or []
            for c in payload_commits[:per_commit_fetch_limit]:
                commits.append({
                    "author": (c.get("author") or {}).get("name", actor),
                    "message": c.get("message", ""),
                    "sha": c.get("sha", ""),
                    "url": c.get("url", ""),
                    "date": created_at,   
                })
        out.append({
            "type": etype,
            "repo": repo_name,
            "created_at": created_at,
            "commits": commits
        })
    
    out.sort(key=lambda x: x["created_at"], reverse=True)
    return out
