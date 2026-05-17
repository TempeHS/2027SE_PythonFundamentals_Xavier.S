from fuel import convert, tank


# tests that convert returns the correct percentage for valid fractions
def test_convert():
    assert convert("1/2") == 50
    assert convert("1/4") == 25


# test that convert raises the correct errors for inve alid inputs
def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("3/2")
