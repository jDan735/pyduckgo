import httpx
from bs4 import BeautifulSoup

from dataclasses import dataclass, field

from .models import SearchResult


@dataclass
class Duck:
    api_url: str = "https://api.duckduckgo.com"
    base_url: str = "https://html.duckduckgo.com/html/"
    params: dict = field(default_factory=lambda: {"format": "json"})

    async def _get(self, *args, **kwargs):
        async with httpx.AsyncClient() as client:
            return await client.get(*args, **kwargs)

    async def search(self, query: str, limit: int = -1) -> list[SearchResult]:
        """
        Went search results

        Based on https://html.duckduckgo.com/html/
        """

        page = await self._get(self.base_url, params={"q": query})
        soup = (BeautifulSoup(page.text, "lxml")
                .find("div", id="links")
                .findAll("div", {"class": "result"}))

        links = [SearchResult.parse(link) for link in soup]
        return links[:limit]

    HTML_search = search
