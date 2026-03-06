from tavily import TavilyClient
from config import TAVILY_API_KEY

client = TavilyClient(api_key=TAVILY_API_KEY)

def search_web(query):

    response = client.search(
        query=query,
        search_depth="advanced",
        max_results=5
    )

    context = "\n".join([r["content"] for r in response["results"]])

    return context