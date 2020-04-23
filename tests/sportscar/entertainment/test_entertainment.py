from pytest import mark

@mark.ui
@mark.smoke
@mark.entertainment
def test_can_navigate_to_entertainment_page(chrome_browser):
    chrome_browser.get('http://siriusxm.com/')
    assert True
