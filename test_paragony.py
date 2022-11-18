import paragony


def test_split_price():
    assert paragony.split_price(100) == (1, 00)


