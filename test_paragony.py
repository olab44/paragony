import paragony
import pytest


def test_split_price_typical():
    price_zl, price_gr = paragony.split_price(123)
    assert price_zl == 1
    assert price_gr == 23


def test_split_price_zl_less_than_10():
    price_zl, price_gr = paragony.split_price(15)
    assert price_zl == 0
    assert price_gr == 15


def test_split_price_float():
    price_zl, price_gr = paragony.split_price(10.15)
    assert price_zl == 0
    assert price_gr == 10


def test_split_price_string():
    with pytest.raises(ValueError):
        paragony.split_price('101.5')
    price_zl, price_gr = paragony.split_price('10')
    assert price_zl == 0
    assert price_gr == 10


def test_split_price_zl_negative_price():
    price_zl, price_gr = paragony.split_price(-990)
    assert price_zl == -9
    assert price_gr == 90


def test_get_description_typical():
    description = paragony.get_description('Bananas', 499)
    assert description == 'price of Bananas is 4.99'


def test_get_description_empty_name():
    with pytest.raises(ValueError):
        paragony.get_description('', 499)


def test_get_description_zero_price():
    description = paragony.get_description('Apples', 0)
    assert description == "Price of Apples is 0.00"


def test_get_description_negative_price():
    description = paragony.get_description('Apples', -330)
    assert description == "Price of Apples is -3.30"


def test_format_price_typical():
    assert paragony.split_price(1332) == 13.32


def test_format_price_less_than_one():
    assert paragony.split_price(99) == 0.99


def test_format_price_negative():
    assert paragony.split_price(-9900) == -99.00
