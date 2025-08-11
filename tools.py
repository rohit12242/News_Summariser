# tools.py
import os
import requests
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()
NEWS_API_KEY = os.getenv("NEWSAPI_KEY")

@tool
def search_news(topic: str) -> str:
    """Search the latest news for a given topic."""
    url = f"https://newsapi.org/v2/everything?q={topic}&pageSize=5&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = [
        f"{a['title']}: {a['description'] or ''}" 
        for a in data.get("articles", [])
    ]
    return "\n".join(articles)
