<div align="center">
  <h1>🦆 pyduckgo</h1>
  <h3>Simple async wrapper for DuckDuckGo</h3>
</div><br>

## 🛠 Usage
```python
from pyduckgo import Duck

duck = Duck()

results = await duck.search("test")

print(results[0].description)
print(results[0].link)
print(results[0].url)
```

## 🚀 Install
```bash
pip install pyduckgo
```
