import requests


def test_twitter_is_avaliable():
    resp = requests.get("https://twitter.com")
    assert "twitter" in resp.text
