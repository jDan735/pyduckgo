import pytest
from pyduckgo import Duck


@pytest.mark.asyncio
async def test_search():
    duck = Duck()
    results = await duck.search("test", limit=3)

    assert len(results) <= 3
    assert results[0].url == "https://wwww.speedtest.net/"
