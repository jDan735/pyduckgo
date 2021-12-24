from bs4 import BeautifulSoup

from urllib.parse import unquote
from dataclasses import dataclass


@dataclass
class SearchResult:
    link: str
    description: str
    url: str

    def parse(soup: BeautifulSoup) -> "SearchResult":
        link = soup.findAll("a", {"class": "result__a"})[0]
        description = soup.findAll("a", {"class": "result__snippet"})
        url = unquote(link.get("href"))[25:].split("&rut=")[0]

        return SearchResult(
            link=link.text,
            description="" if len(description) == 0 else description[0].text,
            url=url
        )
