from moneymoney.presets import EUR, GBP, USD


def test_preset_eur(one_euro):
    assert one_euro == EUR(amount=1.0)


def test_preset_gbp(one_gbp):
    assert one_gbp == GBP(amount=1.0)


def test_preset_usd(one_usd):
    assert one_usd == USD(amount=1.0)
