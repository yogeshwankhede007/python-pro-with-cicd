# 🤝 Contributing to Python CI/CD Demo

First off, thank you for considering contributing to this project! 🎉

This document provides guidelines and steps for contributing. Following these guidelines helps maintain code quality and makes the contribution process smooth for everyone.

---

## 📑 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Code Style Guide](#code-style-guide)
- [Testing Guidelines](#testing-guidelines)
- [Documentation](#documentation)
- [Getting Help](#getting-help)

---

## 📜 Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the maintainers.

---

## 🚀 Getting Started

### Types of Contributions

We welcome many types of contributions:

| Type | Description |
|------|-------------|
| 🐛 **Bug Reports** | Report bugs with detailed reproduction steps |
| ✨ **Feature Requests** | Suggest new features or improvements |
| 📚 **Documentation** | Improve or add documentation |
| 🧪 **Tests** | Add or improve test coverage |
| 🔧 **Code** | Fix bugs or implement features |
| 🎨 **Design** | Improve UI/UX or architecture |

### Good First Issues

Look for issues labeled `good first issue` - these are great for newcomers!

```
https://github.com/yogeshwankhede007/python-pro-with-cicd/labels/good%20first%20issue
```

---

## 💻 Development Setup

### Prerequisites

- Python 3.10 or higher
- Git
- A GitHub account

### Step-by-Step Setup

```bash
# 1. Fork the repository on GitHub
# Click the "Fork" button at https://github.com/yogeshwankhede007/python-pro-with-cicd

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/python-pro-with-cicd.git
cd python-pro-with-cicd

# 3. Add upstream remote
git remote add upstream https://github.com/yogeshwankhede007/python-pro-with-cicd.git

# 4. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 5. Install dependencies
pip install -r requirements-dev.txt
pip install -e .

# 6. Install pre-commit hooks
pre-commit install

# 7. Verify setup
pytest  # All tests should pass
```

### Keeping Your Fork Updated

```bash
# Fetch upstream changes
git fetch upstream

# Update your main branch
git checkout main
git merge upstream/main

# Push to your fork
git push origin main
```

---

## ✏️ Making Changes

### Branch Naming Convention

```bash
# Feature
git checkout -b feature/add-new-validator

# Bug fix
git checkout -b bugfix/fix-divide-by-zero

# Documentation
git checkout -b docs/improve-readme

# Refactoring
git checkout -b refactor/optimize-string-utils
```

### Development Workflow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CONTRIBUTION WORKFLOW                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  1. Fork & Clone                                                             │
│       │                                                                      │
│       ▼                                                                      │
│  2. Create Branch                                                            │
│       │                                                                      │
│       ▼                                                                      │
│  3. Make Changes ◄──────┐                                                    │
│       │                 │                                                    │
│       ▼                 │                                                    │
│  4. Run Tests ──────────┤ (If tests fail, fix and repeat)                   │
│       │                 │                                                    │
│       ▼                 │                                                    │
│  5. Run Linters ────────┘ (If linting fails, fix and repeat)                │
│       │                                                                      │
│       ▼                                                                      │
│  6. Commit Changes                                                           │
│       │                                                                      │
│       ▼                                                                      │
│  7. Push to Fork                                                             │
│       │                                                                      │
│       ▼                                                                      │
│  8. Create Pull Request                                                      │
│       │                                                                      │
│       ▼                                                                      │
│  9. Code Review ◄───────┐                                                    │
│       │                 │                                                    │
│       ▼                 │                                                    │
│  10. Address Feedback ──┘ (If changes requested)                            │
│       │                                                                      │
│       ▼                                                                      │
│  11. Merge! 🎉                                                               │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Before Submitting

Run these checks locally:

```bash
# Format code
black src/ tests/

# Sort imports
isort src/ tests/

# Lint code
flake8 src/ tests/

# Type check
mypy src/

# Run tests with coverage
pytest --cov=src --cov-report=term-missing

# Or run all checks at once with pre-commit
pre-commit run --all-files
```

---

## 📝 Commit Guidelines

We follow [Conventional Commits](https://www.conventionalcommits.org/).

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

| Type | Description |
|------|-------------|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation changes |
| `style` | Code style changes (formatting) |
| `refactor` | Code refactoring |
| `test` | Adding or updating tests |
| `chore` | Maintenance tasks |
| `perf` | Performance improvements |
| `ci` | CI/CD changes |

### Examples

```bash
# Good ✅
feat(calculator): add modulo operation

Add modulo (%) operation to Calculator class with full test coverage.

Closes #42

# Good ✅
fix(validators): handle empty email string

Previously, passing an empty string to validate_email would raise
an exception. Now it returns False as expected.

Fixes #58

# Bad ❌
fixed stuff

# Bad ❌
WIP

# Bad ❌
update code
```

---

## 🔀 Pull Request Process

### Creating a Pull Request

1. **Push your branch** to your fork
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create a Pull Request** on GitHub
   - Go to the original repository
   - Click "New Pull Request"
   - Select your fork and branch
   - Fill out the PR template

### PR Title Format

```
<type>(<scope>): <description>

Examples:
feat(calculator): add power function
fix(validators): handle edge cases in email validation
docs(readme): add installation instructions
```

### PR Description Template

```markdown
## 📋 Description
Brief description of what this PR does.

## 🎯 Related Issue
Fixes #(issue number)

## 🔄 Type of Change
- [ ] 🐛 Bug fix
- [ ] ✨ New feature
- [ ] 📚 Documentation
- [ ] ♻️ Refactoring
- [ ] 🧪 Tests

## 🧪 How Has This Been Tested?
Describe the tests you ran.

## ✅ Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have added tests for my changes
- [ ] All new and existing tests pass
- [ ] I have updated the documentation
- [ ] My changes generate no new warnings
```

### Review Process

1. **Automated Checks**: CI pipeline runs automatically
2. **Code Review**: Maintainers review your code
3. **Feedback**: Address any requested changes
4. **Approval**: Get approval from at least one maintainer
5. **Merge**: PR is merged into main

### After Merge

```bash
# Clean up your local branch
git checkout main
git pull upstream main
git branch -d feature/your-feature-name

# Delete remote branch (optional)
git push origin --delete feature/your-feature-name
```

---

## 🎨 Code Style Guide

### Python Style

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) with these tools:

- **Black**: Code formatting (line length: 88)
- **isort**: Import sorting (black profile)
- **flake8**: Linting

### Code Examples

```python
# Good ✅
from typing import Optional, Union

Number = Union[int, float]


def calculate_average(numbers: list[Number]) -> Optional[float]:
    """
    Calculate the average of a list of numbers.

    Args:
        numbers: A list of numbers to average.

    Returns:
        The average value, or None if the list is empty.

    Examples:
        >>> calculate_average([1, 2, 3, 4, 5])
        3.0
        >>> calculate_average([])
        None
    """
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


# Bad ❌
def calcAvg(nums):
    if len(nums) == 0: return None
    return sum(nums)/len(nums)
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Functions | snake_case | `calculate_total()` |
| Variables | snake_case | `user_count` |
| Classes | PascalCase | `Calculator` |
| Constants | UPPER_SNAKE_CASE | `MAX_RETRIES` |
| Private | Leading underscore | `_internal_method()` |

### Type Hints

Always use type hints:

```python
# Good ✅
def add(a: int, b: int) -> int:
    return a + b

# Bad ❌
def add(a, b):
    return a + b
```

---

## 🧪 Testing Guidelines

### Test Structure

```
tests/
├── __init__.py
├── test_calculator.py      # Tests for calculator.py
├── test_string_utils.py    # Tests for string_utils.py
└── test_validators.py      # Tests for validators.py
```

### Writing Tests

```python
import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""

    @pytest.fixture
    def calculator(self):
        """Create a Calculator instance for tests."""
        return Calculator()

    def test_add_positive_numbers(self, calculator):
        """Test adding two positive numbers."""
        result = calculator.add(2, 3)
        assert result == 5

    def test_divide_by_zero_raises_error(self, calculator):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(10, 0)


# Parametrized tests for multiple inputs
@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (-1, 1, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    """Test addition with various inputs."""
    calc = Calculator()
    assert calc.add(a, b) == expected
```

### Test Naming

```python
# Pattern: test_<what>_<condition>_<expected>

def test_add_positive_numbers_returns_sum():
    ...

def test_divide_by_zero_raises_value_error():
    ...

def test_validate_email_with_invalid_format_returns_false():
    ...
```

### Coverage Requirements

- **Minimum**: 80% coverage
- **Target**: 90% coverage
- New code should have test coverage

```bash
# Check coverage
pytest --cov=src --cov-report=term-missing --cov-fail-under=80
```

---

## 📚 Documentation

### Docstring Format

We use Google-style docstrings:

```python
def validate_email(email: str) -> bool:
    """
    Validate an email address format.

    This function checks if the provided string matches a valid
    email address pattern.

    Args:
        email: The email address to validate.

    Returns:
        True if the email format is valid, False otherwise.

    Raises:
        TypeError: If email is not a string.

    Examples:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False

    Note:
        This performs format validation only, not deliverability checking.
    """
```

### README Updates

If your change affects usage, update the README:

- New features → Add usage examples
- API changes → Update documentation
- Dependencies → Update installation instructions

---

## ❓ Getting Help

### Resources

- 📖 [Documentation](../README.md)
- 💬 [GitHub Discussions](https://github.com/yogeshwankhede007/python-pro-with-cicd/discussions)
- 🐛 [Issue Tracker](https://github.com/yogeshwankhede007/python-pro-with-cicd/issues)

### Questions?

- Search existing issues first
- Check the documentation
- Open a new issue with the `question` label

---

## 🙏 Recognition

Contributors are recognized in:

- The GitHub contributors page
- Release notes for significant contributions
- README acknowledgments section

---

<div align="center">

**Thank you for contributing! Your efforts make this project better for everyone. 🚀**

</div>
