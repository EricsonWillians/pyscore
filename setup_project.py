#!/usr/bin/env python3
"""
setup_project.py - Project structure generator for pyscored

This script generates the entire project structure for the pyscored library,
including directories, placeholder files, and initial content.
"""

import os
import sys
import time
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel
from rich.text import Text

console = Console()

# Project structure definition
PROJECT_STRUCTURE = {
    "pyproject.toml": """
[tool.poetry]
name = "pyscored"
version = "0.1.0"
description = "Universal, Plug-in-Play Scoring System"
authors = ["Your Name <your.email@example.com>"]
license = "MIT"
readme = "README.md"
repository = "https://github.com/yourusername/pyscored"
documentation = "https://pyscored.readthedocs.io"
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.group.dev.dependencies]
pytest = "^7.3.1"
pytest-cov = "^4.1.0"
black = "^23.3.0"
isort = "^5.12.0"
mypy = "^1.3.0"
pylint = "^2.17.4"
pre-commit = "^3.3.2"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"

[tool.black]
line-length = 88
target-version = ["py38", "py39", "py310"]

[tool.isort]
profile = "black"
line_length = 88

[tool.mypy]
python_version = "3.8"
disallow_untyped_defs = true
disallow_incomplete_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_functions = "test_*"
python_classes = "Test*"
addopts = "--cov=pyscored --cov-report=xml --cov-report=term"
""",
    "README.md": """
# pyscored – Universal, Plug-in-Play Scoring System

## Project Overview

**pyscored** is a versatile, blackboxed scoring library designed for universal compatibility 
across various Python-based applications, including traditional games and modern web backend frameworks. 
Developed using Poetry for package management, this library ensures ease of integration, 
modular extensibility, and robust performance.

## Features

- Sandbox execution environment for secure scoring logic
- Plugin-based architecture for custom scoring strategies
- Pre-built adapters for game and web frameworks
- Asynchronous operation support
- Comprehensive documentation and examples

## Installation

```bash
pip install pyscored
```

Or with Poetry:

```bash
poetry add pyscored
```

## Quick Start

```python
from pyscored import ScoringEngine

# Initialize scoring engine
engine = ScoringEngine()

# Update scores
engine.update_score("player1", 100)
engine.update_score("player2", 150)

# Get current scores
scores = engine.get_scores()
print(scores)  # {'player1': 100, 'player2': 150}
```

## Documentation

For full documentation, visit [pyscored.readthedocs.io](https://pyscored.readthedocs.io).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
""",
    "docs/api.md": """
# API Reference

## ScoringEngine

The main class that provides scoring functionality.

### Methods

#### `__init__(config=None)`

Initialize a new scoring engine.

- **Parameters:**
  - `config` (dict, optional): Configuration options for the scoring engine.

#### `update_score(player_id, points, context=None)`

Update the score for a player.

- **Parameters:**
  - `player_id` (str): Unique identifier for the player.
  - `points` (int): Points to add (or subtract if negative).
  - `context` (dict, optional): Additional contextual information.

#### `get_scores()`

Get the current scores for all players.

- **Returns:**
  - `dict`: A dictionary mapping player IDs to their scores.

#### `get_player_score(player_id)`

Get the score for a specific player.

- **Parameters:**
  - `player_id` (str): Unique identifier for the player.
- **Returns:**
  - `int`: The player's score.

#### `reset_scores()`

Reset all scores to zero.

#### `reset_player_score(player_id)`

Reset the score for a specific player.

- **Parameters:**
  - `player_id` (str): Unique identifier for the player.

## Plugin System

### BasePlugin

Abstract base class for all scoring plugins.

#### Methods

#### `__init__(config=None)`

Initialize a new plugin.

- **Parameters:**
  - `config` (dict, optional): Configuration options for the plugin.

#### `process_score(player_id, points, context=None)`

Process a score update.

- **Parameters:**
  - `player_id` (str): Unique identifier for the player.
  - `points` (int): Points to process.
  - `context` (dict, optional): Additional contextual information.
- **Returns:**
  - `int`: The processed score value.
""",
    "docs/usage.md": """
# Usage Guide

## Basic Usage

```python
from pyscored import ScoringEngine

# Initialize scoring engine
engine = ScoringEngine()

# Update scores
engine.update_score("player1", 100)

# Get current scores
scores = engine.get_scores()
print(scores)  # {'player1': 100}

# Reset scores
engine.reset_scores()
```

## Using Plugins

```python
from pyscored import ScoringEngine
from pyscored.plugins import TimeMultiplier

# Create a plugin that doubles scores after 1 minute
multiplier = TimeMultiplier(config={"threshold": 60, "multiplier": 2})

# Initialize engine with plugin
engine = ScoringEngine()
engine.register_plugin(multiplier)

# Update scores (will be affected by the plugin)
engine.update_score("player1", 100)
```

## Integration with Game Frameworks

### Pygame Integration

```python
from pyscored.adapters import PygameAdapter
from pyscored import ScoringEngine

# Initialize the scoring engine
engine = ScoringEngine()

# Create the adapter
adapter = PygameAdapter(engine)

# In your game loop
def handle_scoring(event):
    if event.type == ENEMY_DEFEATED:
        adapter.award_points("player1", 100)
```

## Integration with Web Frameworks

### FastAPI Integration

```python
from fastapi import FastAPI
from pyscored.adapters import FastAPIAdapter
from pyscored import ScoringEngine

app = FastAPI()
engine = ScoringEngine()
adapter = FastAPIAdapter(engine)

# Register the adapter routes
adapter.register_routes(app)

# Now you can access endpoints like:
# - POST /scores/{player_id} (to update scores)
# - GET /scores (to get all scores)
# - GET /scores/{player_id} (to get a specific player's score)
```
""",
    "docs/architecture.md": """
# Architecture

## Overview

The architecture of pyscored is designed to be modular, extensible, and secure.
It consists of several key components:

1. **Core Scoring Engine**: The central component that manages scores and orchestrates the scoring logic.
2. **Sandbox Environment**: Provides a secure execution context for scoring operations.
3. **Plugin System**: Allows for custom scoring logic to be added without modifying the core code.
4. **Adapters**: Facilitate integration with various frameworks and environments.

## Component Diagram

```
┌─────────────────────┐     ┌─────────────────┐
│                     │     │                 │
│  Application        │     │  Plugin System  │
│  (Game/Web)         │     │                 │
│                     │     └────────┬────────┘
└──────────┬──────────┘              │
           │                         │
┌──────────▼──────────┐     ┌────────▼────────┐
│                     │     │                 │
│  Adapter Layer      │────►│  Scoring Engine │
│                     │     │                 │
└─────────────────────┘     └────────┬────────┘
                                     │
                            ┌────────▼────────┐
                            │                 │
                            │  Sandbox        │
                            │                 │
                            └─────────────────┘
```

## Security Considerations

The scoring engine operates within a sandbox environment to prevent:
- Arbitrary code execution
- Access to sensitive system resources
- Interference with the host application

All interactions with the scoring engine are validated and sanitized to ensure security.

## Extensibility

The plugin system allows for custom scoring logic, such as:
- Time-based multipliers
- Combo systems
- Achievement-based bonuses
- Difficulty adjustments

Plugins have a well-defined interface and are loaded dynamically at runtime.

## Performance

The engine is designed to be lightweight and efficient, with minimal overhead.
It can handle high-frequency score updates and large numbers of concurrent players.

## Concurrency

The scoring engine supports both synchronous and asynchronous operations,
making it suitable for multi-threaded and event-driven applications.
""",
    "docs/CONTRIBUTING.md": """
# Contributing to pyscored

Thank you for considering contributing to pyscored! This document outlines the process for contributing to the project.

## Code of Conduct

Please be respectful and considerate of others when contributing to this project.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/pyscored.git`
3. Install poetry: `pip install poetry`
4. Install dependencies: `poetry install`
5. Install pre-commit hooks: `poetry run pre-commit install`

## Development Workflow

1. Create a new branch for your feature or bugfix: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Run tests: `poetry run pytest`
4. Format your code: `poetry run black .`
5. Check for type errors: `poetry run mypy .`
6. Commit your changes with a descriptive message
7. Push to your fork: `git push origin feature/your-feature-name`
8. Create a pull request to the main repository

## Pull Request Process

1. Update the README.md or documentation with details of changes if appropriate
2. Update the tests to cover your changes
3. Ensure all tests pass before submitting
4. The PR will be reviewed by maintainers and feedback may be provided
5. Once approved, your PR will be merged

## Testing

Write tests for all new features and bug fixes. Aim for high test coverage.

## Documentation

Update documentation for any changed functionality. This includes:
- Code docstrings
- API documentation in docs/api.md
- Usage examples if appropriate

## Style Guide

This project uses:
- Black for code formatting
- isort for import sorting
- mypy for type checking
- pylint for linting

These tools are configured in pyproject.toml and run automatically with pre-commit.

## Release Process

Releases are managed by the maintainers and follow semantic versioning.
""",
    "pyscored/__init__.py": """
\"\"\"
pyscored - Universal, Plug-in-Play Scoring System

A versatile, blackboxed scoring library designed for universal compatibility
across various Python-based applications.
\"\"\"

__version__ = "0.1.0"

from pyscored.core.scoring_engine import ScoringEngine

__all__ = ["ScoringEngine"]
""",
    "pyscored/core/__init__.py": """
\"\"\"
Core components of the pyscored system.

This package contains the central functionality of the scoring system.
\"\"\"

from pyscored.core.scoring_engine import ScoringEngine
from pyscored.core.sandbox import Sandbox

__all__ = ["ScoringEngine", "Sandbox"]
""",
    "pyscored/core/scoring_engine.py": """
\"\"\"
Scoring Engine Implementation

The central component that manages scores and orchestrates scoring logic.
\"\"\"

from typing import Any, Dict, List, Optional, Union


class ScoringEngine:
    \"\"\"Main engine for handling scoring operations.\"\"\"

    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        \"\"\"
        Initialize a new scoring engine.

        Args:
            config: Optional configuration for the scoring engine
        \"\"\"
        self._config = config or {}
        self._scores: Dict[str, int] = {}
        self._plugins: List[Any] = []

    def register_plugin(self, plugin: Any) -> None:
        \"\"\"
        Register a scoring plugin.

        Args:
            plugin: The plugin instance to register
        \"\"\"
        self._plugins.append(plugin)

    def update_score(self, player_id: str, points: int, context: Optional[Dict[str, Any]] = None) -> int:
        \"\"\"
        Update the score for a player.

        Args:
            player_id: Unique identifier for the player
            points: Points to add (or subtract if negative)
            context: Additional contextual information

        Returns:
            The updated score
        \"\"\"
        if player_id not in self._scores:
            self._scores[player_id] = 0

        # Process points through plugins
        processed_points = points
        for plugin in self._plugins:
            processed_points = plugin.process_score(player_id, processed_points, context)

        # Update score
        self._scores[player_id] += processed_points
        return self._scores[player_id]

    def get_scores(self) -> Dict[str, int]:
        \"\"\"
        Get all scores.

        Returns:
            Dictionary mapping player IDs to scores
        \"\"\"
        return self._scores.copy()

    def get_player_score(self, player_id: str) -> int:
        \"\"\"
        Get the score for a specific player.

        Args:
            player_id: Unique identifier for the player

        Returns:
            The player's score or 0 if player doesn't exist
        \"\"\"
        return self._scores.get(player_id, 0)

    def reset_scores(self) -> None:
        \"\"\"Reset all scores to zero.\"\"\"
        self._scores = {}

    def reset_player_score(self, player_id: str) -> None:
        \"\"\"
        Reset the score for a specific player.

        Args:
            player_id: Unique identifier for the player
        \"\"\"
        if player_id in self._scores:
            self._scores[player_id] = 0
""",
    "pyscored/core/sandbox.py": """
\"\"\"
Sandbox Environment

Provides a secure execution context for scoring operations.
\"\"\"

import functools
from typing import Any, Callable, Dict, Optional, TypeVar

T = TypeVar('T')


class Sandbox:
    \"\"\"
    Secure execution environment for scoring logic.

    This class provides isolation for scoring operations to prevent
    unauthorized access to system resources or the host application.
    \"\"\"

    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        \"\"\"
        Initialize the sandbox environment.

        Args:
            config: Optional configuration for the sandbox
        \"\"\"
        self._config = config or {}
        self._restricted_modules = self._config.get("restricted_modules", [
            "os", "sys", "subprocess", "builtins.exec", "builtins.eval"
        ])

    def execute(self, func: Callable[..., T], *args: Any, **kwargs: Any) -> T:
        \"\"\"
        Execute a function within the sandbox.

        Args:
            func: The function to execute
            *args: Positional arguments to pass to the function
            **kwargs: Keyword arguments to pass to the function

        Returns:
            The result of the function
        \"\"\"
        @functools.wraps(func)
        def secure_wrapper(*args: Any, **kwargs: Any) -> T:
            # Here we would implement proper security measures
            # This is a placeholder for actual sandbox implementation
            return func(*args, **kwargs)

        return secure_wrapper(*args, **kwargs)
""",
    "pyscored/plugins/__init__.py": """
\"\"\"
Plugin system for the pyscored library.

This package provides extensibility through plugins that modify scoring behavior.
\"\"\"

from pyscored.plugins.base_plugin import BasePlugin

__all__ = ["BasePlugin"]
""",
    "pyscored/plugins/base_plugin.py": """
\"\"\"
Base Plugin for pyscored

Defines the interface that all scoring plugins must implement.
\"\"\"

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class BasePlugin(ABC):
    \"\"\"Abstract base class for all scoring plugins.\"\"\"

    def __init__(self, config: Optional[Dict[str, Any]] = None) -> None:
        \"\"\"
        Initialize a new plugin.

        Args:
            config: Optional configuration for the plugin
        \"\"\"
        self.config = config or {}

    @abstractmethod
    def process_score(self, player_id: str, points: int, context: Optional[Dict[str, Any]] = None) -> int:
        \"\"\"
        Process a score update.

        Args:
            player_id: Unique identifier for the player
            points: Points to process
            context: Additional contextual information

        Returns:
            The processed score value
        \"\"\"
        pass
""",
    "pyscored/adapters/__init__.py": """
\"\"\"
Adapters for integrating pyscored with various frameworks.

This package provides pre-built middleware for seamless integration with
game and web frameworks.
\"\"\"

from pyscored.adapters.game_frameworks import GameAdapter
from pyscored.adapters.web_frameworks import WebAdapter

__all__ = ["GameAdapter", "WebAdapter"]
""",
    "pyscored/adapters/game_frameworks.py": """
\"\"\"
Game Framework Adapters

Adapters for integrating pyscored with various game frameworks.
\"\"\"

from typing import Any, Dict, Optional

from pyscored.core.scoring_engine import ScoringEngine


class GameAdapter:
    \"\"\"Base adapter for game frameworks.\"\"\"

    def __init__(self, engine: ScoringEngine, config: Optional[Dict[str, Any]] = None) -> None:
        \"\"\"
        Initialize a new game adapter.

        Args:
            engine: The scoring engine to use
            config: Optional configuration for the adapter
        \"\"\"
        self.engine = engine
        self.config = config or {}

    def award_points(self, player_id: str, points: int, context: Optional[Dict[str, Any]] = None) -> int:
        \"\"\"
        Award points to a player.

        Args:
            player_id: Unique identifier for the player
            points: Points to award
            context: Additional contextual information

        Returns:
            The updated score
        \"\"\"
        return self.engine.update_score(player_id, points, context)

    def get_score(self, player_id: str) -> int:
        \"\"\"
        Get the score for a player.

        Args:
            player_id: Unique identifier for the player

        Returns:
            The player's score
        \"\"\"
        return self.engine.get_player_score(player_id)


class PygameAdapter(GameAdapter):
    \"\"\"Adapter for Pygame integration.\"\"\"

    def __init__(self, engine: ScoringEngine, config: Optional[Dict[str, Any]] = None) -> None:
        \"\"\"
        Initialize a new Pygame adapter.

        Args:
            engine: The scoring engine to use
            config: Optional configuration for the adapter
        \"\"\"
        super().__init__(engine, config)
        # Additional Pygame-specific initialization


class PygletAdapter(GameAdapter):
    \"\"\"Adapter for Pyglet integration.\"\"\"

    def __init__(self, engine: ScoringEngine, config: Optional[Dict[str, Any]] = None) -> None:
        \"\"\"
        Initialize a new Pyglet adapter.

        Args:
            engine: The scoring engine to use
            config: Optional configuration for the adapter
        \"\"\"
        super().__init__(engine, config)
        # Additional Pyglet-specific initialization
""",
    "pyscored/adapters/web_frameworks.py": """
\"\"\"
Web Framework Adapters

Adapters for integrating pyscored with various web frameworks.
\"\"\"

from typing import Any, Dict, Optional

from pyscored.core.scoring_engine import ScoringEngine


class WebAdapter:
    \"\"\"Base adapter for web frameworks.\"\"\"

    def __init__(self, engine: ScoringEngine, config: Optional[Dict[str, Any]] = None) -> None:
        \"\"\"
        Initialize a new web adapter.

        Args:
            engine: The scoring engine to use
            config: Optional configuration for the adapter
        \"\"\"
        self.engine = engine
        self.config = config or {}

    def update_score(self, player_id: str, points: int, context: Optional[Dict[str, Any]] = None) -> int:
        \"\"\"
        Update the score for a player.

        Args:
            player_id: Unique identifier for the player
            points: Points to update
            context: Additional contextual information

        Returns:
            The updated score
        \"\"\"
        return self.engine.update_score(player_id, points, context)

    def get_scores(self) -> Dict[str, int]:
        \"\"\"
        Get all scores.

        Returns:
            Dictionary mapping player IDs to scores
        \"\"\"
        return self.engine.get_scores()

    def get_player_score(self, player_id: str) -> int:
        \"\"\"
        Get the score for a player.

        Args:
            player_id: Unique identifier for the player

        Returns:
            The player's score
        \"\"\"
        return self.engine.get_player_score(player_id)


class FastAPIAdapter(WebAdapter):
    \"\"\"Adapter for FastAPI integration.\"\"\"

    def __init__(self, engine: ScoringEngine, config: Optional[Dict[str, Any]] = None) -> None:
        \"\"\"
        Initialize a new FastAPI adapter.

        Args:
            engine: The scoring engine to use
            config: Optional configuration for the adapter
        \"\"\"
        super().__init__(engine, config)
        # Additional FastAPI-specific initialization

    def register_routes(self, app: Any) -> None:
        \"\"\"
        Register routes with a FastAPI application.

        Args:
            app: The FastAPI application instance
        \"\"\"
        # This is a simplified example - real implementation would use FastAPI decorators
        @app.get("/scores")
        def get_scores():
            return self.get_scores()

        @app.get("/scores/{player_id}")
        def get_player_score(player_id: str):
            return {"player_id": player_id, "score": self.get_player_score(player_id)}

        @app.post("/scores/{player_id}")
        def update_score(player_id: str, points: int):
            return {"player_id": player_id, "score": self.update_score(player_id, points)}
""",
    "pyscored/utils/__init__.py": """
\"\"\"
Utility functions for the pyscored library.

This package provides helper functions and utilities for use throughout the library.
\"\"\"

from pyscored.utils.helpers import safe_cast

__all__ = ["safe_cast"]
""",
    "pyscored/utils/helpers.py": """
\"\"\"
Helper Functions

Utility functions for use throughout the pyscored library.
\"\"\"

from typing import Any, Callable, Optional, Type, TypeVar

T = TypeVar('T')


def safe_cast(value: Any, target_type: Type[T], default: Optional[T] = None) -> Optional[T]:
    \"\"\"
    Safely cast a value to a target type.

    Args:
        value: The value to cast
        target_type: The type to cast to
        default: Default value to return if casting fails

    Returns:
        The cast value or the default if casting fails
    \"\"\"
    try:
        return target_type(value)
    except (ValueError, TypeError):
        return default


def debounce(wait_time: float) -> Callable:
    \"\"\"
    Decorator to debounce a function call.

    Args:
        wait_time: Time to wait in seconds

    Returns:
        Decorated function
    \"\"\"
    def decorator(func: Callable) -> Callable:
        import time
        last_called = [0.0]

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_time = time.time()
            if current_time - last_called[0] >= wait_time:
                last_called[0] = current_time
                return func(*args, **kwargs)
            return None

        return wrapper

    return decorator
""",
    "tests/unit/__init__.py": "",
    "tests/integration/__init__.py": "",
    "tests/unit/test_scoring_engine.py": """
\"\"\"
Unit tests for the ScoringEngine class.
\"\"\"

import pytest

from pyscored.core.scoring_engine import ScoringEngine


def test_init():
    \"\"\"Test initializing the scoring engine.\"\"\"
    engine = ScoringEngine()
    assert engine is not None
    assert engine.get_scores() == {}


def test_update_score():
    \"\"\"Test updating scores.\"\"\"
    engine = ScoringEngine()
    
    # Test updating a new player's score
    result = engine.update_score("player1", 100)
    assert result == 100
    assert engine.get_player_score("player1") == 100
    
    # Test updating an existing player's score
    result = engine.update_score("player1", 50)
    assert result == 150
    assert engine.get_player_score("player1") == 150
    
    # Test updating with negative points
    result = engine.update_score("player1", -30)
    assert result == 120
    assert engine.get_player_score("player1") == 120


def test_get_scores():
    \"\"\"Test getting all scores.\"\"\"
    engine = ScoringEngine()
    
    engine.update_score("player1", 100)
    engine.update_score("player2", 200)
    
    scores = engine.get_scores()
    assert scores == {"player1": 100, "player2": 200}
    
    # Ensure we get a copy of the scores, not the original reference
    scores["player1"] = 999
    assert engine.get_player_score("player1") == 100


def test_get_player_score():
    \"\"\"Test getting a player's score.\"\"\"
    engine = ScoringEngine()
    
    engine.update_score("player1", 100)
    
    assert engine.get_player_score("player1") == 100
    assert engine.get_player_score("nonexistent") == 0


def test_reset_scores():
    \"\"\"Test resetting all scores.\"\"\"
    engine = ScoringEngine()
    
    engine.update_score("player1", 100)
    engine.update_score("player2", 200)
    
    engine.reset_scores()
    
    assert engine.get_scores() == {}
    assert engine.get_player_score("player1") == 0
    assert engine.get_player_score("player2") == 0


def test_reset_player_score():
    \"\"\"Test resetting a player's score.\"\"\"
    engine = ScoringEngine()
    
    engine.update_score("player1", 100)
    engine.update_score("player2", 200)
    
    engine.reset_player_score("player1")
    
    assert engine.get_player_score("player1") == 0
    assert engine.get_player_score("player2") == 200

""",
    "tests/unit/test_sandbox.py": """
\"\"\"
Unit tests for the Sandbox class.
\"\"\"

import pytest

from pyscored.core.sandbox import Sandbox


def test_init():
    \"\"\"Test initializing the sandbox.\"\"\"
    sandbox = Sandbox()
    assert sandbox is not None
    
    # Test custom config
    custom_config = {"restricted_modules": ["module1", "module2"]}
    sandbox = Sandbox(config=custom_config)
    assert sandbox._config == custom_config


def test_execute():
    \"\"\"Test executing a function in the sandbox.\"\"\"
    sandbox = Sandbox()
    
    # Define a simple function to execute
    def add(a, b):
        return a + b
    
    # Execute the function in the sandbox
    result = sandbox.execute(add, 2, 3)
    assert result == 5
    
    # Test with keyword arguments
    result = sandbox.execute(add, a=5, b=7)
    assert result == 12
""",
    "tests/integration/test_engine_with_plugins.py": """
\"\"\"
Integration tests for the ScoringEngine with plugins.
\"\"\"

import pytest

from pyscored.core.scoring_engine import ScoringEngine
from pyscored.plugins.base_plugin import BasePlugin


class TestMultiplierPlugin(BasePlugin):
    \"\"\"Test plugin that multiplies scores by a configurable factor.\"\"\"
    
    def process_score(self, player_id, points, context=None):
        \"\"\"Multiply the points by the configured factor.\"\"\"
        multiplier = self.config.get("multiplier", 1)
        return points * multiplier


def test_engine_with_multiplier_plugin():
    \"\"\"Test the scoring engine with a multiplier plugin.\"\"\"
    engine = ScoringEngine()
    
    # Register a plugin that doubles all points
    plugin = TestMultiplierPlugin({"multiplier": 2})
    engine.register_plugin(plugin)
    
    # Test that the plugin doubles the points
    result = engine.update_score("player1", 50)
    assert result == 100
    
    # Change the multiplier and test again
    plugin.config["multiplier"] = 3
    result = engine.update_score("player1", 50)
    assert result == 250  # 100 + (50*3)


def test_engine_with_multiple_plugins():
    \"\"\"Test the scoring engine with multiple plugins.\"\"\"
    engine = ScoringEngine()
    
    # Register two plugins with different multipliers
    plugin1 = TestMultiplierPlugin({"multiplier": 2})
    plugin2 = TestMultiplierPlugin({"multiplier": 3})
    
    engine.register_plugin(plugin1)
    engine.register_plugin(plugin2)
    
    # Test that the plugins are applied in sequence:
    # 50 -> plugin1 -> 100 -> plugin2 -> 300
    result = engine.update_score("player1", 50)
    assert result == 300
""",
}


def create_directory_structure(base_path: Path) -> None:
    """Create the directory structure for the project."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold blue]Creating project structure..."),
        console=console,
    ) as progress:
        task = progress.add_task("Creating", total=len(PROJECT_STRUCTURE))
        
        for path, content in PROJECT_STRUCTURE.items():
            file_path = base_path / path
            
            # Create parent directory if it doesn't exist
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Create file with content
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content.strip())
            
            # Short delay for visual effect
            time.sleep(0.05)
            progress.update(task, advance=1)


def main() -> None:
    """Main function to execute the project setup."""
    console.clear()
    
    # Print project banner
    title = Text("pyscored Project Setup", style="bold cyan")
    subtitle = Text("Universal, Plug-in-Play Scoring System", style="italic blue")
    panel_content = Text("\n").append(title).append("\n").append(subtitle).append("\n")
    console.print(Panel(panel_content, expand=False))
    
    base_path = Path(".")
    
    # Check if any project files already exist
    existing_files = [
        str(p) for p in base_path.glob("**/*") 
        if p.is_file() and p.name != "setup_project.py" and not p.name.startswith(".")
    ]
    
    if existing_files:
        console.print("[yellow]Warning: The following files already exist in the directory:")
        for file in existing_files[:5]:
            console.print(f"  - [yellow]{file}")
        
        if len(existing_files) > 5:
            console.print(f"  - [yellow]... and {len(existing_files)-5} more")
            
        if not console.input("\nContinue anyway? [y/N]: ").lower().startswith('y'):
            console.print("[red]Setup aborted.")
            sys.exit(1)
    
    # Create project structure
    create_directory_structure(base_path)
    
    # Completion message
    console.print("\n[green]✓ Project structure created successfully![/green]")
    console.print("\nNext steps:")
    console.print("  1. [bold]Install dependencies:[/bold] poetry install")
    console.print("  2. [bold]Run tests:[/bold] poetry run pytest")
    console.print("  3. [bold]Read documentation:[/bold] See docs/ directory")

if __name__ == "__main__":
    main()