from pytest import mark


@mark.skip(reason="broken by deploy buildNumber")
@mark.entertainment
def test_environment_is_qa(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://qa.com"
    assert port == 80


@mark.entertainment
def test_environment_is_dev(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://dev.com"
    assert port == 8080


@mark.xfail(reason="Env was not qa")
@mark.entertainment
def test_environment_as_stage(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://stage.com"
    assert port == 8081
