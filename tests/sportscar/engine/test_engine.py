from pytest import mark

@mark.ui
@mark.smoke
@mark.engine
def test_can_navigate_to_engine_page(chrome_browser):
    chrome_browser.get('http://artomanliness.com/articles/how-a-car-engine-works/')
    assert True
