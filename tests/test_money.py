from _pytest.python_api import raises
from faker import Faker

from moneymoney.money import CurrencyCodeIsNoneException, CurrencyIsNotTheSameException, Money


def test_can_create_money():
    currency_code = Faker().currency_code()
    money = Money(currency_code=currency_code)
    assert money.amount == 0.0
    assert money.currency_code == currency_code


def test_can_create_money_with_str_as_currency_code():
    money = Money(currency_code="GBP")
    assert money.amount == 0.0
    assert money.currency_code == "GBP"


def test_can_print_money():
    currency_code = Faker().currency_code()
    money = Money(currency_code=currency_code)
    assert str(money) == f"0.0{currency_code}"


def test_can_print_money_amount_rounded():
    currency_code = Faker().currency_code()
    money = Money(currency_code=currency_code, amount=0.1111)
    assert str(money) == f"0.11{currency_code}"


def test_money_are_equal():
    currency_code = Faker().currency_code()
    money_one = Money(currency_code=currency_code, amount=1.0)
    money_two = Money(currency_code=currency_code, amount=1.0)
    assert money_one == money_two


def test_money_are_equal_for_same_currency_in_uppercase_and_lowercase():
    money_one = Money(currency_code="GBP", amount=1.0)
    money_two = Money(currency_code="gbp", amount=1.0)
    assert money_one == money_two


def test_money_are_not_equal():
    currency_code_one = Faker().currency_code()
    currency_code_two = Faker().currency_code()
    money_one = Money(currency_code=currency_code_one, amount=2.0)
    money_two = Money(currency_code=currency_code_two, amount=1.0)
    assert money_one != money_two


def test_raise_exception_if_no_currency_code():
    with raises(CurrencyCodeIsNoneException):
        _ = Money(currency_code=None)


def test_can_add_moneys_of_same_currency():
    currency_code = Faker().currency_code()
    money_one = Money(currency_code=currency_code, amount=1.0)
    money_two = Money(currency_code=currency_code, amount=3.0)
    money_three = money_one + money_two
    assert money_three.amount == 4.0
    assert money_three.currency_code == currency_code


def test_can_add_moneys_of_same_currency_different_case_currency_code():
    money_one = Money(currency_code="GBP", amount=1.0)
    money_two = Money(currency_code="gbp", amount=3.0)
    money_three = money_one + money_two
    assert money_three.amount == 4.0


def test_cannot_add_moneys_of_different_currency():
    currency_code_one = Faker().currency_code()
    currency_code_two = Faker().currency_code()
    money_one = Money(currency_code=currency_code_one, amount=1.0)
    money_two = Money(currency_code=currency_code_two, amount=3.0)
    with raises(CurrencyIsNotTheSameException):
        _ = money_one + money_two


def test_can_sub_moneys_of_same_currency():
    currency_code = Faker().currency_code()
    money_one = Money(currency_code=currency_code, amount=1.0)
    money_two = Money(currency_code=currency_code, amount=3.0)
    money_three = money_one - money_two
    assert money_three.amount == -2.0
    assert money_three.currency_code == currency_code


def test_can_sub_moneys_of_same_currency_different_case_currency_code():
    money_one = Money(currency_code="GBP", amount=1.0)
    money_two = Money(currency_code="gbp", amount=3.0)
    money_three = money_one - money_two
    assert money_three.amount == -2.0


def test_cannot_sub_moneys_of_different_currency():
    currency_code_one = Faker().currency_code()
    currency_code_two = Faker().currency_code()
    money_one = Money(currency_code=currency_code_one, amount=1.0)
    money_two = Money(currency_code=currency_code_two, amount=3.0)
    with raises(CurrencyIsNotTheSameException):
        _ = money_one - money_two
