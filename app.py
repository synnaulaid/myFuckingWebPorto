import os, requests
from flask import Flask, render_template
from flask_caching import Cache
from dotenv import load_dotenv
from services import github_api as gh

load_dotenv()

app = Flask(__name__)
cache = Cache(app, config={"CACHE_TYPE": "SimpleCache"})
CACHE_TIMEOUT = int(os.getenv("CACHE_TIMEOUT", 600))

@cache.cached(timeout=CACHE_TIMEOUT, key_prefix="repos")
def cached_repos():
    return gh.get_repos()

@cache.cached(timeout=CACHE_TIMEOUT, key_prefix="events")
def cached_events():
    return gh.get_user_events(limit=40)
    


@app.route("/")
def index():
    repos = cached_repos()
    events = cached_events()
    repo = gh.get_repos()
    return render_template("index.html", repos=repos, events=events, url=repo)


@app.route("/repo/<name>")
def repo_detail(name):
    repo = gh.get_repo_detail(name)
    commits = gh.get_commits(name, limit=20)
    prs_open = gh.get_pull_requests(name, state="open", limit=10)
    prs_closed = gh.get_pull_requests(name, state="closed", limit=10)
    return render_template("repo.html",
                            repo=repo,
                            commits=commits,
                            prs_open=prs_open,
                            prs_closed=prs_closed)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
