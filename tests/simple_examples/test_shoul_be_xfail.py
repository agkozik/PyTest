from pytest import mark

@mark.door
def test_should_always_pass():
    assert True


@mark.skip(reason="Broken, fixing next sprint")
@mark.door
def test_this_needs_work():
    assert False


@mark.xfail(reason="This feature should have been deprecated")
@mark.door
def test_this_should_always_fail():
    assert False
