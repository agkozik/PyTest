from pytest import mark


@mark.parametrize('tv_brand', [
    ('Samsung'),
    ('Sony'),
    ('LG')
]
                  )
def test_tv_turns_on(tv_brand):
    print(f'{tv_brand} turn on as expected')

