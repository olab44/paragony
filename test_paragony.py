from paragony import split_price


def test_split_price():
    assert split_price(100) == (1, 00)


def test_fail():
    assert 2 + 2 * 2 == 8


