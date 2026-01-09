# 📒 Development Environment Setup

> **A detailed guide to setting up your development environment for contributing to this project.**

---

## 📑 Table of Contents

- [Prerequisites](#prerequisites)
- [Quick Setup](#quick-setup)
- [Detailed Setup](#detailed-setup)
- [IDE Configuration](#ide-configuration)
- [Troubleshooting](#troubleshooting)
- [Next Steps](#next-steps)

---

## Prerequisites

### Required Software

| Software | Minimum Version | Purpose |
|----------|----------------|---------|
| **Python** | 3.10+ | Runtime environment |
| **Git** | 2.x | Version control |
| **pip** | Latest | Package management |

### Optional but Recommended

| Software | Purpose |
|----------|---------|
| **VS Code** | Code editor with excellent Python support |
| **PyCharm** | Full-featured Python IDE |
| **Docker** | Containerization (for advanced testing) |

### Check Your Environment

```bash
# Check Python version
python --version
# Should be 3.10 or higher

# Check Git
git --version

# Check pip
pip --version
```

---

## Quick Setup

For experienced developers:

```bash
git clone https://github.com/yogeshwankhede007/python-pro-with-cicd.git
cd python-pro-with-cicd
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements-dev.txt
pip install -e .
pre-commit install
pytest
```

---

## Detailed Setup

### Step 1: Clone the Repository

```bash
# Clone from GitHub
git clone https://github.com/yogeshwankhede007/python-pro-with-cicd.git

# Navigate to the project directory
cd python-pro-with-cicd

# Check the remote
git remote -v
# Should show:
# origin  https://github.com/yogeshwankhede007/python-pro-with-cicd.git (fetch)
# origin  https://github.com/yogeshwankhede007/python-pro-with-cicd.git (push)
```

### Step 2: Create Virtual Environment

**Why?** Virtual environments isolate project dependencies.

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate

# You should see (venv) in your prompt
(venv) $
```

### Step 3: Upgrade pip

```bash
# Upgrade pip to latest version
python -m pip install --upgrade pip
```

### Step 4: Install Dependencies

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install the project in editable mode
pip install -e .

# Verify installation
pip list
```

**What you should see:**
```
Package         Version
--------------- -------
pytest          7.4.0
black           23.0.0
isort           5.12.0
flake8          6.1.0
mypy            1.5.0
... and more
```

### Step 5: Install Pre-commit Hooks

```bash
# Install pre-commit hooks
pre-commit install

# Test pre-commit hooks
pre-commit run --all-files
```

**What are pre-commit hooks?**
- Automatically run checks before each commit
- Catch issues before they reach CI
- Ensure code quality standards

### Step 6: Verify Setup

```bash
# Run tests
pytest

# Check code formatting
black --check src/ tests/

# Check imports
isort --check-only src/ tests/

# Lint code
flake8 src/ tests/

# Type check
mypy src/
```

**All checks should pass! ✅**

---

## IDE Configuration

### Visual Studio Code

#### Recommended Extensions

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-python.black-formatter",
    "ms-python.isort",
    "ms-python.flake8",
    "charliermarsh.ruff",
    "GitHub.copilot",
    "eamodio.gitlens"
  ]
}
```

#### Settings (.vscode/settings.json)

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.linting.mypyEnabled": true,
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": false,
  "python.testing.pytestArgs": [
    "tests"
  ]
}
```

#### Launch Configuration (.vscode/launch.json)

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Current File",
      "type": "python",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true
    },
    {
      "name": "Python: Pytest",
      "type": "python",
      "request": "launch",
      "module": "pytest",
      "args": [
        "tests/",
        "-v"
      ],
      "console": "integratedTerminal",
      "justMyCode": false
    }
  ]
}
```

### PyCharm

#### Configure Python Interpreter

1. Open **Settings** → **Project** → **Python Interpreter**
2. Click the gear icon → **Add**
3. Select **Existing environment**
4. Browse to `venv/bin/python` (or `venv\Scripts\python.exe` on Windows)

#### Configure Tools

**Black:**
- **Settings** → **Tools** → **External Tools** → **+**
- Name: Black
- Program: `$PyInterpreterDirectory$/black`
- Arguments: `$FilePath$`
- Working directory: `$ProjectFileDir$`

**isort:**
- Similar to Black, but with `isort` as program

#### Enable pytest

1. **Settings** → **Tools** → **Python Integrated Tools**
2. Set **Default test runner** to **pytest**

---

## Troubleshooting

### Common Issues

#### Issue: "python: command not found"

**Solution:**
```bash
# macOS/Linux
which python python3

# Try python3 instead
python3 -m venv venv

# Windows - ensure Python is in PATH
```

#### Issue: "pip: command not found"

**Solution:**
```bash
# Use python -m pip instead
python -m pip install --upgrade pip
```

#### Issue: "Permission denied" when installing packages

**Solution:**
```bash
# Don't use sudo with virtual environment
# Make sure virtual environment is activated
source venv/bin/activate

# Then install
pip install -r requirements-dev.txt
```

#### Issue: Pre-commit hooks failing

**Solution:**
```bash
# Update pre-commit
pip install --upgrade pre-commit

# Reinstall hooks
pre-commit uninstall
pre-commit install

# Update hook revisions
pre-commit autoupdate
```

#### Issue: Tests failing with import errors

**Solution:**
```bash
# Install project in editable mode
pip install -e .

# Verify PYTHONPATH
echo $PYTHONPATH

# Or set it explicitly
export PYTHONPATH="${PYTHONPATH}:${PWD}"
```

#### Issue: mypy errors about missing imports

**Solution:**
```bash
# Create py.typed file (already included)
# Or add to mypy config
# mypy_path = src
```

---

## Environment Variables

### Development

Create a `.env` file (already in .gitignore):

```bash
# .env
PYTHONDONTWRITEBYTECODE=1
PYTHONUNBUFFERED=1
DEBUG=True
```

### Loading Environment Variables

```python
# Using python-dotenv (optional)
from dotenv import load_dotenv
import os

load_dotenv()
debug = os.getenv("DEBUG", "False") == "True"
```

---

## Development Tools Cheat Sheet

### Running Tests

```bash
# All tests
pytest

# Specific file
pytest tests/test_calculator.py

# Specific test
pytest tests/test_calculator.py::test_add

# With coverage
pytest --cov=src

# With HTML coverage report
pytest --cov=src --cov-report=html

# Verbose output
pytest -v

# Show print statements
pytest -s

# Parallel execution
pytest -n auto
```

### Code Formatting

```bash
# Check formatting
black --check src/ tests/

# Format code
black src/ tests/

# Check only changed files
black --check $(git diff --name-only --diff-filter=ACM | grep '\.py$')
```

### Import Sorting

```bash
# Check import order
isort --check-only src/ tests/

# Sort imports
isort src/ tests/

# Show differences
isort --diff src/ tests/
```

### Linting

```bash
# Lint all code
flake8 src/ tests/

# Lint specific file
flake8 src/calculator.py

# With statistics
flake8 --statistics src/ tests/
```

### Type Checking

```bash
# Check types
mypy src/

# Verbose output
mypy -v src/

# Generate HTML report
mypy src/ --html-report ./mypy-report
```

### Security Scanning

```bash
# Scan code for security issues
bandit -r src/

# Generate JSON report
bandit -r src/ -f json -o bandit-report.json

# Check dependencies
safety check -r requirements.txt
```

---

## Next Steps

Now that your environment is set up:

1. 📖 Read the [Contributing Guide](CONTRIBUTING.md)
2. 🐛 Find a [good first issue](https://github.com/yogeshwankhede007/python-pro-with-cicd/labels/good%20first%20issue)
3. 🌿 Create a feature branch
4. ✍️ Make your changes
5. ✅ Run tests and checks
6. 📝 Commit with a good message
7. 🚀 Create a pull request

---

<div align="center">

**Happy coding! 🎉**

If you encounter any issues, please [open an issue](https://github.com/yogeshwankhede007/python-pro-with-cicd/issues).

</div>
