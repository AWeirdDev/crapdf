import pytest
import crapdf


def test_sum_as_string():
    assert crapdf.sum_as_string(1, 1) == "2"
