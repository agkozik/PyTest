from pytest import mark


@mark.browsers
def test_browser_can_navigate_to_training(browser):
    browser.get('https://techstepacademy.com/training-ground')