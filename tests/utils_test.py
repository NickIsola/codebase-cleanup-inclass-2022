# this is the "tests/utils_test.py" file...

from app.utlis import to_usd

def test_to_usd():
    # rounds to two decomal places and have a dollar sign
    # if large number should use thousands separator
    assert to_usd(1234.79) == "$1,234.79"

