import pytest

from moneymoney.money import Money


@pytest.fixture
def one_euro() -> Money:
    return Money(currency_code="EUR", amount=1.0)


@pytest.fixture
def one_gbp() -> Money:
    return Money(currency_code="GBP", amount=1.0)


@pytest.fixture
def one_usd() -> Money:
    return Money(currency_code="USD", amount=1.0)


@pytest.fixture
def three_gbp() -> Money:
    return Money(currency_code="gbp", amount=3.0)


@pytest.fixture
def three_usd() -> Money:
    return Money(currency_code="USD", amount=3.0)
