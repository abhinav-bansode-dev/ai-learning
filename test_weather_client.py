#Unit Testing
"""project/
├─ APIWeatherProject.py        # main script (imports fetch_weather)
├─ weather_client.py           # fetch_weather(city) -> dict
├─ persistence.py              # save_read(record)
└─ tests/
   └─ test_weather_client.py
"""

import pytest
import requests
from weather_client import fetch_weather

class DummyResp:
    def __init__(self, status_code=200, json_data=None, text=""):
        self.status_code = status_code
        self._json = json_data or {}
        self.text = text
    def raise_for_status(self):
        if 400 <= self.status_code < 600:
            raise requests.HTTPError(f"{self.status_code} Error", response=self)
    def json(self):
        return self._json

def test_fetch_success(monkeypatch):
    dummy = DummyResp(200, {"name":"TestCity","main":{"temp":20},"weather":[{"description":"sunny"}]})
    monkeypatch.setattr("requests.get", lambda *a, **k: dummy)
    res = fetch_weather("TestCity")
    assert res["city"] == "TestCity"
    assert res["temp"] == 20
    assert "sunny" in res["description"]

def test_fetch_404(monkeypatch):
    dummy = DummyResp(404, {}, "Not Found")
    monkeypatch.setattr("requests.get", lambda *a, **k: dummy)
    with pytest.raises(requests.HTTPError):
        fetch_weather("NoSuchCity")

def test_fetch_timeout(monkeypatch):
    def raise_timeout(*a, **k):
        raise requests.Timeout("timed out")
    monkeypatch.setattr("requests.get", raise_timeout)
    with pytest.raises(requests.Timeout):
        fetch_weather("AnyCity")
