import aiohttp
import json


class Duck:
    def __init__(self):
        self.url = "https://api.duckduckgo.com"

    async def _get(self, params):
        self.params = {"format": "json"}
        self.params = {**self.params, **params}

        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, params=self.params) as response:
                if not response.status == 200:
                    return 404

                return json.loads(await response.text())

    async def search(self, query):
        return await self._get({"q": query})
