import paragony


def test_split_price_typical():
    price_zl, price_gr = paragony.split_price(123)
    assert price_zl == 1
    assert price_gr == 23


def test_split_price_gr_less_than_10():
    price_zl, price_gr = paragony.split_price(101)
    assert price_zl == 1
    assert price_gr == 1


def test_split_price_zl_less_than_10():
    price_zl, price_gr = paragony.split_price(15)
    assert price_zl == 0
    assert price_gr == 15
