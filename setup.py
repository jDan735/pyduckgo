from setuptools import setup
from pyduckgo import __version__

with open("README.md", encoding="utf-8") as readme:
    long_description = readme.read()

setup(
    name="pyduckgo",
    version=__version__,
    author="Daniel Zakharov",
    author_email="daniel734@bk.ru",
    description="Simple async wrapper for DuckDuckGo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="api duckduckgo python",
    url="https://github.com/jDan735/pyduckgo",
    license="MIT",
    packages=["pyduckgo"],
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3",
    install_requires=[
        "beautifulsoup4",
        "httpx"
    ]
)
