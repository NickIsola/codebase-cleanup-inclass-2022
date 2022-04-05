# this is the "tests/utils_test.py" file...

from app.utils import to_usd

def test_to_usd():
    # rounds to two decomal places and have a dollar sign
    # if large number should use thousands separator
    assert to_usd(0.45555) == "$0.46"
    assert to_usd(123456789.98) == "$123,456,789.98"

