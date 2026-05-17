from plates import is_valid


# test
def test_valid_plate():
    assert is_valid("CS50") == True
    assert is_valid("AA") == True
    assert is_valid("AAA123") == True


def test_too_short():
    assert is_valid("A") == False


def test_too_long():
    assert is_valid("AAAAAAA") == False


def test_must_start_with_two_letters():
    assert is_valid("1A") == False
    assert is_valid("A1") == False


def test_no_letters_after_numbers():
    assert is_valid("AA1B") == False
    assert is_valid("CS50X") == False


def test_first_number_not_zero():
    assert is_valid("AA01") == False


def test_no_punctuation():
    assert is_valid("AA!") == False
    assert is_valid("HE-LO") == False
