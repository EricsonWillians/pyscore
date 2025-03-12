# API Documentation for pyscored

## Scoring Engine

### Class: `ScoringEngine`

#### Methods
- **`initialize_score(player_id: str, initial_score: float = 0.0)`**  
  Initializes or resets the player's score.

- **`update_score(player_id: str, points: float)`**  
  Updates the score for the specified player.

- **`get_score(player_id: str) -> float`**  
  Retrieves the current score of the specified player.

- **`reset_score(player_id: str)`**  
  Resets the player's score to zero.

- **`configure_rule(rule_name: str, rule_logic: Callable[..., Any])`**  
  Configures scoring rules dynamically within the sandbox environment.

- **`apply_rule(rule_name: str, **kwargs) -> Any`**  
  Executes a configured scoring rule.

- **`register_plugin(plugin: BasePlugin)`**  
  Registers a new plugin to extend scoring functionalities.

- **`execute_plugin(plugin_name: str, **kwargs) -> Any`**  
  Executes functionality provided by a registered plugin.

## Sandbox Environment

### Class: `Sandbox`

#### Methods
- **`add_rule(rule_name: str, rule_logic: Callable[..., Any])`**  
  Adds a new scoring rule to the sandbox.

- **`execute_rule(rule_name: str, **kwargs) -> Any`**  
  Executes a scoring rule securely.

- **`remove_rule(rule_name: str)`**  
  Removes a rule from the sandbox.

- **`list_rules() -> Dict[str, Callable[..., Any]]`**  
  Lists all configured rules.

## Plugins

### BasePlugin

#### Methods
- **`execute(**kwargs) -> Any`**  
  Executes the core functionality of the plugin (must be overridden).

- **`config() -> dict`**  
  Retrieves the configuration details of the plugin.

### ComboBonusPlugin

Awards bonus points for consecutive successful actions or combos.

#### Methods
- **`execute(player_id: str, action_successful: bool, base_points: float)`**  
  Applies bonus points based on consecutive successful actions.

- **`config() -> dict`**  
  Provides configuration details including bonus thresholds and multipliers.

### StreakRewardPlugin

Awards special rewards for achieving specific streaks of successful actions.

#### Methods
- **`execute(player_id: str, action_successful: bool)`**  
  Awards reward points based on achieving successful action streaks.

- **`config() -> dict`**  
  Provides configuration details for reward streak thresholds and reward points.

## Adapters

### GameFrameworkAdapter

Integrates the Scoring Engine with traditional Python game frameworks (Pygame, Pyglet).

#### Methods
- **`setup_player(player_id: str, initial_score: float = 0.0)`**
- **`update_player_score(player_id: str, points: float)`**
- **`get_player_score(player_id: str) -> float`**
- **`apply_game_rule(rule_name: str, **kwargs) -> Any`**
- **`execute_plugin_feature(plugin_name: str, **kwargs) -> Any`**

### WebFrameworkAdapter

Facilitates integration with web frameworks such as FastAPI.

#### Methods (async)
- **`setup_user(user_id: str, initial_score: float = 0.0)`**
- **`update_user_score(user_id: str, points: float)`**
- **`get_user_score(user_id: str) -> float`**
- **`apply_web_rule(rule_name: str, **kwargs) -> Any`**
- **`execute_plugin_feature(plugin_name: str, **kwargs) -> Any`**

## Utilities

### Functions
- **`validate_score(score: float) -> bool`**  
  Validates that a score is non-negative.

- **`merge_config(default_config: Dict[str, Any], custom_config: Dict[str, Any]) -> Dict[str, Any]`**  
  Merges custom configurations into default settings.

- **`clamp_score(score: float, min_score: float, max_score: float) -> float`**  
  Clamps the score within specified bounds.

- **`format_score(score: float, decimals: int = 2) -> str`**  
  Formats a score to a specified number of decimal places.