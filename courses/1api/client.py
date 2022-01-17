import requests

requests.get("http://localhost:7777")

requests.post("http://localhost:7777", json={"name": "vikings"})