"""Python client for the open Datacircle API: find the best GTM APIs. https://datacircle.dev"""
import json
import urllib.parse
import urllib.request

BASE_URL = "https://api.datacircle.dev/v1"
__version__ = "0.1.0"


def _get(path, **params):
    query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
    url = f"{BASE_URL}{path}" + (f"?{query}" if query else "")
    request = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": f"datacircle-python/{__version__}"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def apis():
    """Every API on the sheet."""
    return _get("/apis")


def best(slug, limit=None):
    """Who is best for one API."""
    return _get(f"/apis/{urllib.parse.quote(slug)}/best", limit=limit)


def plans(api=None, query=None, sort=None, limit=None, offset=None):
    """Search the plans, by API, text, sort order, limit and offset."""
    return _get("/plans", api=api, query=query, sort=sort, limit=limit, offset=offset)


def provider(slug):
    """One provider's ranks on every API."""
    return _get(f"/providers/{urllib.parse.quote(slug)}")
