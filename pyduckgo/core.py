from bs4 import BeautifulSoup
import asyncio
import aiohttp
import json


class Duck:
    def __init__(self):
        self.url = "https://api.duckduckgo.com"
        self.params = {"format": "json"}

    async def _get(self, params, url=""):
        url = self.url if url == "" else url
        params = {**self.params, **params}

        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=params) as response:
                if not response.status == 200:
                    return 404

                return await response.text()

    async def search(self, query):
        response = await self._get({"q": query})
        return json.loads(response)

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
    async def HTML_search(self, query):
        html_url = "https://html.duckduckgo.com/html/"

        page = await self._get({"q": query}, url=html_url)
        soup = BeautifulSoup(page, "lxml").find("div", id="links") \
                                          .findAll("div", {"class": "result"})

        links = []

        for linkDiv in soup:
            link = linkDiv.findAll("a", {"class": "result__a"})[0]
            description = linkDiv.findAll("a", {"class": "result__snippet"})

            if len(description) != 0:
                description = "None"
            else:
                description = description[0]

            links.append({
                "title": link.text,
                "url": link.get("href"),
                "description": description.text
            })

        return links


async def test():
    ddg = Duck()
    print(await ddg.HTML_search("ban"))


if __name__ == "__main__":
    asyncio.run(test())
