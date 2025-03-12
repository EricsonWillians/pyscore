# Usage Guide for pyscore

This guide provides comprehensive examples demonstrating how to effectively integrate and utilize the `pyscore` library in your Python applications.

## Installation

Ensure you have Poetry installed, then run:

```bash
poetry add pyscore
```

## Basic Usage

### Initialize Scoring Engine

```python
from pyscore.core.scoring_engine import ScoringEngine

engine = ScoringEngine()
engine.initialize_score(player_id="player1", initial_score=100)
```

### Update and Retrieve Score

```python
engine.update_score("player1", points=25)
current_score = engine.get_score("player1")
print(f"Player1's current score: {current_score}")
```

## Configuring and Using Sandbox Rules

```python
engine.configure_rule("double_points", lambda points: points * 2)
result = engine.apply_rule("double_points", points=15)
print(f"Double points result: {result}")
```

## Plugins

### Register and Execute ComboBonusPlugin

```python
from pyscore.plugins.combo_bonus_plugin import ComboBonusPlugin

combo_plugin = ComboBonusPlugin(name="combo_bonus", bonus_threshold=3, bonus_multiplier=1.5)
engine.register_plugin(combo_plugin)

engine.execute_plugin("combo_bonus", player_id="player1", action_successful=True, base_points=10)
```

### Register and Execute StreakRewardPlugin

```python
from pyscore.plugins.streak_reward_plugin import StreakRewardPlugin

streak_plugin = StreakRewardPlugin(name="streak_reward", reward_streak=5, reward_points=50)
engine.register_plugin(streak_plugin)

engine.execute_plugin("streak_reward", player_id="player1", action_successful=True)
```

## Game Framework Integration

### Using GameFrameworkAdapter

```python
from pyscore.adapters.game_frameworks import GameFrameworkAdapter

adapter = GameFrameworkAdapter(engine)
adapter.setup_player("player1", initial_score=50)
adapter.update_player_score("player1", points=20)
score = adapter.get_player_score("player1")
print(f"Game player score: {score}")
```

## Web Framework Integration

### Using WebFrameworkAdapter (FastAPI example)

```python
from fastapi import FastAPI
from pyscore.adapters.web_frameworks import WebFrameworkAdapter

app = FastAPI()
web_adapter = WebFrameworkAdapter(engine)

@app.post("/user/{user_id}/score")
async def update_user_score(user_id: str, points: float):
    await web_adapter.update_user_score(user_id, points)
    current_score = await web_adapter.get_user_score(user_id)
    return {"user_id": user_id, "score": current_score}
```

## Utility Functions

```python
from pyscore.utils.helpers import format_score, validate_score

score = 123.4567
if validate_score(score):
    formatted_score = format_score(score)
    print(f"Formatted score: {formatted_score}")
else:
    print("Invalid score provided.")
```

These usage examples illustrate integrating the `pyscore` library into various Python applications, showcasing its flexibility and extensibility.

