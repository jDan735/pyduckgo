from msgspec import Struct


class SearchResult(Struct):
    index: int
    snippet: str
    title: str
    link: str
