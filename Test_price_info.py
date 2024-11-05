import price_info as PRICE

print("Test Price Info")


def test_total_cost_shopping():
    expected = 46.75
    result = PRICE.total_cost_shopping()
    assert(result == expected)


def test_cost_of_fruit():
    expected = 49.5
    result = PRICE.cost_of_fruits('pomegranate', 10)
    assert(result == expected)