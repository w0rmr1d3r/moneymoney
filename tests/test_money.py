from _pytest.python_api import raises

from moneymoney.money import (
    CurrencyCodeIsNoneException,
    CurrencyIsNotTheSameException,
    Money,
    OtherIsMoneyInstanceException,
    OtherIsNotMoneyInstanceException,
)


def test_can_create_money():
    currency_code = "EUR"
    money = Money(currency_code=currency_code)
    assert money.amount == 0.0
    assert money.currency_code == currency_code


def test_can_create_money_with_str_as_currency_code():
    money = Money(currency_code="GBP")
    assert money.amount == 0.0
    assert money.currency_code == "GBP"


def test_can_print_money():
    currency_code = "EUR"
    money = Money(currency_code=currency_code)
    assert str(money) == f"0.0{currency_code}"


def test_can_print_money_amount_rounded():
    currency_code = "EUR"
    money = Money(currency_code=currency_code, amount=0.1111)
    assert str(money) == f"0.11{currency_code}"


def test_money_are_equal():
    currency_code = "EUR"
    money_one = Money(currency_code=currency_code, amount=1.0)
    money_two = Money(currency_code=currency_code, amount=1.0)
    assert money_one == money_two


def test_money_are_equal_for_same_currency_in_uppercase_and_lowercase(one_gbp):
    money_two = Money(currency_code="gbp", amount=1.0)
    assert one_gbp == money_two


def test_money_are_not_equal(one_euro, three_usd):
    assert one_euro != three_usd


def test_raise_exception_if_no_currency_code():
    with raises(CurrencyCodeIsNoneException):
        _ = Money(currency_code=None)


def test_can_add_moneys_of_same_currency(one_euro):
    currency_code = "EUR"
    money_two = Money(currency_code=currency_code, amount=3.0)
    money_three = one_euro + money_two
    assert money_three.amount == 4.0
    assert money_three.currency_code == currency_code


def test_can_add_moneys_of_same_currency_different_case_currency_code(one_gbp):
    money_two = Money(currency_code="gbp", amount=3.0)
    money_three = one_gbp + money_two
    assert money_three.amount == 4.0


def test_cannot_add_moneys_of_different_currency(one_euro, three_usd):
    with raises(CurrencyIsNotTheSameException):
        _ = one_euro + three_usd


def test_cannot_add_money_with_other_type(one_euro):
    with raises(OtherIsNotMoneyInstanceException):
        _ = one_euro + 2


def test_can_sub_moneys_of_same_currency(one_euro):
    currency_code = "EUR"
    money_two = Money(currency_code=currency_code, amount=3.0)
    money_three = one_euro - money_two
    assert money_three.amount == -2.0
    assert money_three.currency_code == currency_code


def test_can_sub_moneys_of_same_currency_different_case_currency_code(one_gbp, three_gbp):
    money_three = one_gbp - three_gbp
    assert money_three.amount == -2.0


def test_cannot_sub_moneys_of_different_currency(one_euro, three_usd):
    with raises(CurrencyIsNotTheSameException):
        _ = one_euro - three_usd


def test_cannot_sub_money_with_other_type(one_euro):
    with raises(OtherIsNotMoneyInstanceException):
        _ = one_euro - 2


def test_can_compare_less_than_moneys(one_gbp, three_gbp):
    assert one_gbp < three_gbp


def test_can_compare_less_equals_moneys(one_gbp, three_gbp):
    assert one_gbp <= three_gbp


def test_can_compare_greater_than_moneys(one_gbp, three_gbp):
    assert three_gbp > one_gbp


def test_can_compare_greater_equals_moneys(one_gbp, three_gbp):
    assert three_gbp >= one_gbp


def test_cannot_mul_money_with_other_money(one_euro):
    currency_code_one = "EUR"
    money_two = Money(currency_code=currency_code_one, amount=1.0)
    with raises(OtherIsMoneyInstanceException):
        _ = one_euro * money_two


def test_can_right_multiply_money(one_gbp):
    result = 3 * one_gbp
    assert result.amount == 3.0


def test_can_left_multiply_money(one_gbp):
    result = one_gbp * 3.5
    assert result.amount == 3.5


def test_can_neg_money(one_gbp):
    result = -one_gbp
    assert result.amount == -1


def test_can_neg_of_neg_money():
    money_one = Money(currency_code="GBP", amount=-1.0)
    result = -money_one
    assert result.amount == 1


def test_can_abs_money():
    money_one = Money(currency_code="GBP", amount=-1.0)
    result = abs(money_one)
    assert result.amount == 1
