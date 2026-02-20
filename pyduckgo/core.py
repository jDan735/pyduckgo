import aiohttp
from selectolax.lexbor import LexborHTMLParser
from dataclasses import dataclass, field

from yarl import URL
from .models import SearchResult
from msgspec import convert

from rich import print


@dataclass
class Duck:
    base_url: str = "https://lite.duckduckgo.com/lite/"
    user_agent: str = "abobka"

    async def _get(self, *args, **kwargs):
        async with aiohttp.ClientSession(
            headers={"USER-AGENT": self.user_agent}
        ) as session:
            return await session.get(*args, **kwargs)

    async def search(self, query: str, limit: int = -1) -> list[SearchResult]:
        """
        Returns search results

        Based on https://lite.duckduckgo.com/lite/
        """

        r = await self._get(self.base_url, params={"q": query})
        text = await r.text()

        lx = LexborHTMLParser(text)
        table = lx.css("table")[-1]

        snippets = table.css("td.result-snippet")
        links = table.css("a.result-link")

        raw_parsed = [f for i in table.text().split("\n") if (f := i.strip()) != ""]
        raw_results = []

        try:
            result_count = int(raw_parsed[-4][:-1])
        except TypeError:
            result_count = 10

        for i in range(0, result_count - 1):
            parsed = raw_parsed[4 * i : 4 * (i + 1)]

            snippet = snippets[i].inner_html
            link = links[i].attrs["href"]

            raw_results.append(
                {
                    "index": i + 1,
                    "snippet": snippet.strip(),
                    "title": parsed[1],
                    "link": URL(link).query["uddg"],
                }
            )

        return convert(raw_results[:limit], list[SearchResult])

    HTML_search = search
