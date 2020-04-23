# pytest -m json -v -s
from pytest import mark


@mark.json
def test_tv_turns_on(tv_brand):
    print(f'{tv_brand} turn on as expected')
