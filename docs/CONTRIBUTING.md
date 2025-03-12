# docs/CONTRIBUTING.md

## Contributing to pyscored

Thank you for your interest in contributing to **pyscored**! This document outlines clear guidelines and best practices to help you contribute effectively.

### Getting Started

1. **Fork the repository:** Click the "Fork" button at the top right of the repository page on GitHub.
2. **Clone your fork:**
   ```bash
   git clone https://github.com/<your-username>/pyscored.git
   cd pyscored
   ```
3. **Set up the development environment:**
   ```bash
   poetry install
   ```

### Making Changes

- **Create a new branch:** Always create a new branch from the `main` branch for your feature or fix:
  ```bash
  git checkout -b feature/my-new-feature
  ```

- **Implement your changes:** Ensure you follow PEP 8 guidelines and maintain the existing coding style.

- **Write tests:** Add unit and integration tests for new features or bug fixes.

### Testing

- **Run tests locally:**
  ```bash
  poetry run pytest
  ```

- **Check test coverage:**
  ```bash
  poetry run pytest --cov=pyscored
  ```

### Code Quality

Before committing your changes, ensure code quality checks pass:

- **Format your code:**
  ```bash
  poetry run black .
  poetry run isort .
  ```

- **Type checking and linting:**
  ```bash
  poetry run mypy .
  poetry run pylint pyscored tests
  ```

### Committing Changes

- Commit messages should be clear and descriptive. Follow the conventional format:
  ```
  feat: Add combo bonus plugin
  fix: Resolve scoring rule execution issue
  docs: Update usage examples
  ```

### Submitting a Pull Request

- Push your branch to your fork:
  ```bash
  git push origin feature/my-new-feature
  ```

- Open a pull request on GitHub targeting the `main` branch of the main repository.
- Clearly describe the purpose of your changes and reference any relevant issues or discussions.

### Reviewing Process

- Your pull request will be reviewed by maintainers. Engage in discussions and promptly address requested changes.
- Once approved, your changes will be merged into the `main` branch.

### Reporting Issues

- Report bugs or suggest enhancements through GitHub Issues. Clearly describe steps to reproduce and expected behavior.

### Code of Conduct

Please follow respectful and professional conduct in all interactions within the project community.

Thank you for contributing to **pyscored**!