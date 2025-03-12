# ARCHITECTURE.md

## Architecture Overview

The **pyscored** architecture is modular, robust, and flexible, designed specifically to integrate smoothly into various Python-based applications, including traditional games and modern web applications. Below, each key component is explained in detail to provide a clear understanding of how the system is structured and operates.

---

## Core Components

### Scoring Engine

The **Scoring Engine** acts as the primary interface and central hub, responsible for managing score initialization, updates, retrieval, and resets. It serves as the primary interaction point for all scoring-related operations.

### Key Responsibilities:
- Player score management.
- Dynamic scoring rule configuration.
- Plugin registration and execution.

## Sandbox Environment

The Sandbox securely encapsulates all scoring rule execution to prevent unauthorized code execution, ensuring robustness and safety within dynamic scoring scenarios.

### Key Responsibilities:
- Rule registration, execution, and management.
- Secure execution of scoring logic.

## Plugin System

A versatile and extensible plugin-based architecture that enhances scoring functionalities without altering the core engine. Each plugin extends the `BasePlugin` abstract class, providing specific, targeted functionality.

### Example Plugins:
- **ComboBonusPlugin:** Rewards consecutive successful actions.
- **StreakRewardPlugin:** Rewards streaks of successful actions.
- **TimeDecayPlugin:** Implements time-sensitive scoring mechanics.

## Adapter Layers

Adapters provide the bridge between the core scoring system and external frameworks or applications, simplifying the integration process.

### Game Framework Adapter
Facilitates integration with traditional game frameworks like Pygame and Pyglet.

### Web Framework Adapter
Facilitates asynchronous integration into modern web frameworks such as FastAPI, enabling real-time gamification.

## Utility Functions

Reusable helper functions enhance the robustness and consistency of scoring operations:
- **Score validation**
- **Configuration merging**
- **Score formatting and clamping**

## Detailed Component Interaction Diagram

```
                ┌───────────────────┐
                │   Application     │
                └─────────┬─────────┘
                          │
                          ▼
                  ┌───────────────────────┐
                  │   Adapter Layer          │
                  │ (Game/Web Frameworks)   │
                  └───────────┬─────────────┘
                              │
                  ┌───────────▼─────────────┐
                  │     Scoring Engine      │
                  └───────┬───────────┬─────┘
                          │           │
              ┌───────────▼───┐   ┌───▼───────┐
              │   Sandbox      │   │ Plugins   │
              └───────────┬───┘    └──────────┘
                           │
                  ┌────────▼──────────┐
                  │ Utility Functions │
                  └───────────────────┘

## Design Principles

- **Modularity:** Clearly defined boundaries between components.
- **Extensibility:** Plugin-based architecture allows easy functionality expansion.
- **Security:** Sandbox ensures safe execution of dynamic scoring logic.
- **Universality:** Flexible adapters ensure compatibility with various external systems.

This comprehensive architecture ensures pyscored remains robust, secure, and flexible, facilitating seamless integration across diverse applications and environments.

