# tests/unit/test_scoring_engine.py

import pytest
from pyscore.core.scoring_engine import ScoringEngine
from pyscore.core.sandbox import Sandbox


@pytest.fixture
def scoring_engine():
    sandbox = Sandbox()
    return ScoringEngine(sandbox=sandbox)


def test_initialize_score(scoring_engine):
    scoring_engine.initialize_score("player1", 10.0)
    assert scoring_engine.get_score("player1") == 10.0


def test_update_score(scoring_engine):
    scoring_engine.initialize_score("player1", 5.0)
    scoring_engine.update_score("player1", 15.0)
    assert scoring_engine.get_score("player1") == 20.0


def test_update_score_uninitialized_player(scoring_engine):
    with pytest.raises(ValueError):
        scoring_engine.update_score("player2", 5.0)


def test_reset_score(scoring_engine):
    scoring_engine.initialize_score("player1", 20.0)
    scoring_engine.reset_score("player1")
    assert scoring_engine.get_score("player1") == 0.0


def test_configure_and_apply_rule(scoring_engine):
    scoring_engine.configure_rule("double_points", lambda points: points * 2)
    result = scoring_engine.apply_rule("double_points", points=5)
    assert result == 10


def test_register_and_execute_plugin(scoring_engine, mocker):
    mock_plugin = mocker.Mock()
    mock_plugin.name = "bonus_plugin"
    scoring_engine.register_plugin(mock_plugin)
    scoring_engine.execute_plugin("bonus_plugin", points=5)
    mock_plugin.execute.assert_called_once_with(points=5)