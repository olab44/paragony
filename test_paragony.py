import paragony


def test_split_price():
    price_zl, price_gr = paragony.split_price(100)
    assert price_zl == 1
    assert price_gr == 0


def test_pass():
    assert 2 == 2
