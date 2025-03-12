# tests/unit/test_helpers.py

import pytest
from pyscored.utils.helpers import validate_score, merge_config, format_score, clamp_score

def test_merge_config():
    default = {"a": 1, "b": 2}
    custom = {"b": 3, "c": 4}
    merged = merge_config(default, custom)
    assert merged == {"a": 1, "b": 3, "c": 4}

def test_format_score():
    formatted_score = format_score(12.34567)
    assert formatted_score == "12.35"

def test_format_score_custom_decimals():
    score = 123.456789
    formatted_score = format_score(score, decimals=4)
    assert formatted_score == "123.4568"

def test_validate_score_positive():
    assert validate_score(10)
    assert validate_score(0)

def test_validate_score_negative():
    assert not validate_score(-5)

def test_clamp_score():
    assert clamp_score(10, 0, 5) == 5
    assert clamp_score(-1, 0, 5) == 0
    assert clamp_score(3, 0, 5) == 3
