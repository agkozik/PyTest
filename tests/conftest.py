from pytest import fixture
from selenium import webdriver
from tests.config import Config
import json


data_path = 'tests/test_data.json'


def load_test_data_from_json(path):
    with open(path) as data_file:
        data = json.load(data_file)
        return data


@fixture(params=load_test_data_from_json(data_path))
def tv_brand(request):
    data = request.param
    return data


@fixture(params=[webdriver.Chrome, webdriver.Firefox, webdriver.Edge, webdriver.Opera])  # - один браузер на одину сессию (на все запущенные тесты) в 2 раза быстрее
def browser(request):
    driver = request.param
    drvr = driver()
    yield drvr
    drvr.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        help="Environment to run test against"
    )


@fixture(scope='session')
def env(request):
    return request.config.getoption("--env")


@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg


# @fixture(scope='function') #- один экземпляр браузера на один метод
@fixture(scope='session')  # - один браузер на одину сессию (на все запущенные тесты в 2 раза быстрее)
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser
    # Teardown
    print("\n-Teardown this browser-")
