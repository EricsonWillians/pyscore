# PUBLISHING_GUIDE.md

## Publishing pyscored to PyPI

Follow these comprehensive steps to publish the **pyscored** Python package to PyPI, ensuring it's accessible for easy installation by anyone.

### Prerequisites

- **Poetry**: Ensure Poetry is installed. If not, install it from [Poetry's official website](https://python-poetry.org/docs/#installation).
- **PyPI Account**: Create an account at [PyPI](https://pypi.org/) if you don't have one already.

--- 

### Step-by-Step Publishing Process

#### Step 1: Verify pyproject.toml
Ensure your `pyproject.toml` has correct metadata:

```toml
[tool.poetry]
name = "pyscored"
version = "0.1.0"
description = "Universal, Plug-in-Play Scoring System"
authors = ["Your Name <your.email@example.com>"]
license = "GNU"
readme = "README.md"
repository = "https://github.com/yourusername/pyscored"
documentation = "https://pyscored.readthedocs.io"

[tool.poetry.dependencies]
python = "^3.8"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

---

#### Step 2: Prepare for Distribution

Build the distribution files (wheel and source distributions):

```bash
poetry build
```

Check the generated files in `dist/` directory:

```bash
ls dist/
```

You should see files similar to:

```
pyscored-0.1.0-py3-none-any.whl
pyscored-0.1.0.tar.gz
```

---

#### Step 3: Configure Poetry for PyPI

Configure Poetry to connect to your PyPI account:

```bash
poetry config pypi-token.pypi YOUR_PYPI_API_TOKEN
```

Replace `YOUR_PYPI_API_TOKEN` with the token obtained from your PyPI account settings (Account Settings → API tokens → Add API token).

---

#### Step 4: Publish to PyPI

Publish the package:

```bash
poetry publish
```

To publish a pre-release (beta/alpha), add the `--build` and `--dry-run` options first to ensure the process is error-free:

```bash
poetry publish --build --dry-run
```

If the dry run succeeds, remove `--dry-run`:

```bash
poetry publish --build
```

---

### Post-Publishing

After successful publishing, verify by visiting your project URL at:

```
https://pypi.org/project/pyscored/
```

---

### Installing Your Published Package

Anyone can now install your package directly from PyPI:

```bash
pip install pyscored
```

or

```bash
poetry add pyscored
```

---

### Updating Your Package

To release updates:

1. Increment the version number in `pyproject.toml` (use semantic versioning).
2. Run `poetry build` to rebuild the distribution.
3. Publish again with `poetry publish`.

---

### Troubleshooting

- **Duplicate version:** Ensure version increments correctly for every release.
- **Authentication errors:** Verify your PyPI API token and Poetry configuration.

---

Congratulations! Your `pyscored` package is now live and accessible to the entire Python community.