from bs4 import BeautifulSoup
import httpx

from urllib.parse import unquote


class Duck:
    def __init__(self):
        self.url = "https://api.duckduckgo.com"
        self.params = {"format": "json"}

    async def _get(self, url, params={}, timeout=10):
        async with httpx.AsyncClient() as client:
            r = await client.get(url, params=params, timeout=timeout)
            return r.text

    """
    Went array

    [
        {
            "title": "ban",
            "url": "ban.ru",
            "description": "ban is cool"
        },
        ...
    ]
    """
    async def search(self, query, limit=-1):
        html_url = "https://html.duckduckgo.com/html/"

        page = await self._get(html_url, {"q": query})
        soup = (BeautifulSoup(page, "lxml")
                .find("div", id="links")
                .findAll("div", {"class": "result"}))

        links = []

        for _link in soup:
            link = _link.findAll("a", {"class": "result__a"})[0]
            description = _link.findAll("a", {"class": "result__snippet"})
            url = unquote(link.get("href"))[25:].split("&rut=")[0]

            if len(description) == 0:
                description = ""
            else:
                description = description[0].text

            links.append({
                "title": link.text,
                "url": url,
                "description": description
            })

        return links[:limit]

    HTML_search = search
