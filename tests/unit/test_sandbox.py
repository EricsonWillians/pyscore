# tests/unit/test_sandbox.py

import pytest
from pyscored.core.sandbox import Sandbox


@pytest.fixture
def sandbox():
    return Sandbox()


def test_add_and_execute_rule(sandbox):
    sandbox.add_rule("multiply", lambda x, y: x * y)
    result = sandbox.execute_rule("multiply", x=3, y=4)
    assert result == 12


def test_add_existing_rule(sandbox):
    sandbox.add_rule("add", lambda x, y: x + y)
    with pytest.raises(ValueError):
        sandbox.add_rule("add", lambda x, y: x + y)


def test_execute_nonexistent_rule(sandbox):
    with pytest.raises(ValueError):
        sandbox.execute_rule("nonexistent_rule", x=1, y=2)


def test_remove_rule(sandbox):
    sandbox.add_rule("subtract", lambda x, y: x - y)
    sandbox.remove_rule("subtract")
    with pytest.raises(ValueError):
        sandbox.execute_rule("subtract", x=5, y=3)


def test_list_rules(sandbox):
    sandbox.add_rule("divide", lambda x, y: x / y)
    rules = sandbox.list_rules()
    assert "divide" in rules
    assert callable(rules["divide"])