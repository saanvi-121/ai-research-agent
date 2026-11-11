

import json

from ddgs import DDGS
from langchain_core.tools import tool


@tool
def web_search(query: str) -> str:
    """Search the web for a query and return titles, snippets, and source URLs."""
    try:
        search_results = DDGS().text(query, max_results=5) or []
    except Exception as exc:
        return json.dumps({"error": f"Web search failed: {exc}", "results": []})

    results = [
        {
            "title": item.get("title", ""),
            "url": item.get("href", ""),
            "snippet": item.get("body", ""),
        }
        for item in search_results
    ]
    return json.dumps({"results": results}, ensure_ascii=False)