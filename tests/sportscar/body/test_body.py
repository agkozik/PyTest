from pytest import mark


@mark.ui
@mark.smoke
@mark.body
class BodyTests:
    def test_can_navigate_to_motor_page(self, chrome_browser):
        chrome_browser.get('http://motortrend.com/')
        assert True

    def test_bumper(self):
        assert True

    def test_windshief(self):
        assert True
# варианты запуска тестов:
# pytests -m smoke
# pytests -m body
# pytests -m "body and smoke"
# pytests -m "body or smoke"
# pytests -m "body not smoke"
# pytests -m "body or door
# маркеры описываются в pytest.ini
