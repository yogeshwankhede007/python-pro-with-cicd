# 🚀 Python Project with CI/CD - A Complete Learning Guide

[![CI Pipeline](https://github.com/yogeshwankhede007/python-pro-with-cicd/actions/workflows/ci.yml/badge.svg)](https://github.com/yogeshwankhede007/python-pro-with-cicd/actions/workflows/ci.yml)
[![CD Pipeline](https://github.com/yogeshwankhede007/python-pro-with-cicd/actions/workflows/cd.yml/badge.svg)](https://github.com/yogeshwankhede007/python-pro-with-cicd/actions/workflows/cd.yml)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](docs/CONTRIBUTING.md)

> **A comprehensive, production-ready Python project demonstrating CI/CD best practices with GitHub Actions. Built for software engineers who want to understand how modern DevOps pipelines work in real-world scenarios.**

---

## 📑 Table of Contents

- [🎯 What is This Project?](#-what-is-this-project)
- [🤔 Why CI/CD?](#-why-cicd)
- [🏗️ Project Architecture](#️-project-architecture)
- [🚀 Quick Start](#-quick-start)
- [📚 Documentation](#-documentation)
- [🔄 CI/CD Pipeline Overview](#-cicd-pipeline-overview)
- [🛠️ Development Workflow](#️-development-workflow)
- [📊 Code Quality Standards](#-code-quality-standards)
- [🧪 Testing Strategy](#-testing-strategy)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🎯 What is This Project?

This is a **real-world demonstration project** that showcases:

| Component | Description |
|-----------|-------------|
| **Python Application** | A clean, well-structured Python package with calculator, string utilities, and validators |
| **Automated Testing** | Comprehensive unit tests with pytest achieving 80%+ code coverage |
| **CI Pipeline** | Automated code quality checks, security scanning, and multi-version testing |
| **CD Pipeline** | Automated deployment to staging/production with release management |
| **Best Practices** | Industry-standard coding conventions, documentation, and Git workflows |

### 🎓 Who is This For?

- **Software Engineers** learning CI/CD concepts
- **DevOps Engineers** looking for GitHub Actions templates
- **Team Leads** establishing development best practices
- **Students** understanding modern software development lifecycle

---

## 🤔 Why CI/CD?

### The Problem Without CI/CD

```
❌ "It works on my machine" - Different environments cause bugs
❌ Manual testing is slow and error-prone
❌ Deployments are risky and stressful
❌ Code quality degrades over time
❌ Integration issues discovered late in development
```

### The Solution With CI/CD

```
✅ Consistent environments across all stages
✅ Automated testing on every code change
✅ Confident, repeatable deployments
✅ Enforced code quality standards
✅ Early detection of integration issues
```

### 📈 CI/CD Benefits at a Glance

| Metric | Without CI/CD | With CI/CD |
|--------|---------------|------------|
| Bug Detection | Days/Weeks | Minutes |
| Deployment Frequency | Weekly/Monthly | Multiple times daily |
| Deployment Risk | High | Low |
| Developer Feedback | Slow | Instant |
| Code Quality | Inconsistent | Consistently High |

> 📖 **Deep Dive**: Read our [Complete CI/CD Guide](docs/CICD_GUIDE.md) for detailed explanations.

---

## 🏗️ Project Architecture

```
python-pro-with-cicd/
│
├── 📁 .github/                    # GitHub-specific configurations
│   ├── 📁 workflows/              # CI/CD Pipeline definitions
│   │   ├── ci.yml                 # Continuous Integration workflow
│   │   ├── cd.yml                 # Continuous Deployment workflow
│   │   └── pr-checks.yml          # Pull Request validation
│   ├── ISSUE_TEMPLATE/            # Issue templates
│   ├── PULL_REQUEST_TEMPLATE.md   # PR template
│   └── CODEOWNERS                 # Code ownership rules
│
├── 📁 src/                        # Source code
│   ├── __init__.py                # Package initialization
│   ├── calculator.py              # Arithmetic operations module
│   ├── string_utils.py            # String manipulation utilities
│   └── validators.py              # Input validation functions
│
├── 📁 tests/                      # Test suite
│   ├── __init__.py
│   ├── test_calculator.py         # Calculator tests
│   ├── test_string_utils.py       # String utils tests
│   └── test_validators.py         # Validator tests
│
├── 📁 docs/                       # Documentation
│   ├── CICD_GUIDE.md              # Complete CI/CD explanation
│   ├── GITHUB_BEST_PRACTICES.md   # GitHub workflow best practices
│   ├── CONTRIBUTING.md            # Contribution guidelines
│   ├── CODE_OF_CONDUCT.md         # Community guidelines
│   └── DEVELOPMENT_SETUP.md       # Development environment setup
│
├── 📄 pyproject.toml              # Project configuration (PEP 518)
├── 📄 requirements.txt            # Production dependencies
├── 📄 requirements-dev.txt        # Development dependencies
├── 📄 .pre-commit-config.yaml     # Pre-commit hooks
├── 📄 .flake8                     # Linter configuration
├── 📄 .gitignore                  # Git ignore rules
├── 📄 LICENSE                     # MIT License
└── 📄 README.md                   # This file
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Git
- GitHub account

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/yogeshwankhede007/python-pro-with-cicd.git
cd python-pro-with-cicd

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements-dev.txt
pip install -e .

# 4. Set up pre-commit hooks
pre-commit install

# 5. Run tests to verify setup
pytest
```

### Verify Installation

```bash
# Run a quick test
python -c "from src.calculator import Calculator; c = Calculator(); print(f'2 + 3 = {c.add(2, 3)}')"
# Output: 2 + 3 = 5
```

> 📖 **Detailed Setup**: See [Development Setup Guide](docs/DEVELOPMENT_SETUP.md) for complete instructions.

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| 📘 [CI/CD Complete Guide](docs/CICD_GUIDE.md) | Deep dive into CI/CD concepts, workflows, and implementation |
| 📗 [GitHub Best Practices](docs/GITHUB_BEST_PRACTICES.md) | Industry-standard GitHub workflows and conventions |
| 📙 [Contributing Guidelines](docs/CONTRIBUTING.md) | How to contribute to this project |
| 📕 [Code of Conduct](docs/CODE_OF_CONDUCT.md) | Community guidelines and expectations |
| 📒 [Development Setup](docs/DEVELOPMENT_SETUP.md) | Complete development environment setup |

---

## 🔄 CI/CD Pipeline Overview

### Continuous Integration (CI)

Our CI pipeline runs automatically on every push and pull request:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            CI PIPELINE                                       │
│                     Triggered on: push, pull_request                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐   ┌─────────────────┐   ┌─────────────────┐            │
│  │  CODE QUALITY   │   │    SECURITY     │   │     TESTS       │            │
│  │                 │   │                 │   │                 │            │
│  │ • Black         │   │ • Bandit        │   │ • Python 3.10   │            │
│  │ • isort         │   │ • Safety        │   │ • Python 3.11   │            │
│  │ • flake8        │   │                 │   │ • Python 3.12   │            │
│  │ • mypy          │   │                 │   │ • Multi-OS      │            │
│  └────────┬────────┘   └────────┬────────┘   └────────┬────────┘            │
│           │                     │                     │                      │
│           └─────────────────────┼─────────────────────┘                      │
│                                 │                                            │
│                                 ▼                                            │
│                    ┌─────────────────────┐                                   │
│                    │   BUILD PACKAGE     │                                   │
│                    │   (if all pass)     │                                   │
│                    └─────────────────────┘                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Continuous Deployment (CD)

Our CD pipeline handles releases and deployments:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            CD PIPELINE                                       │
│                 Triggered on: push to main, version tags                     │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐                                                         │
│  │    VALIDATE     │ ◄── All tests must pass                                │
│  └────────┬────────┘                                                         │
│           │                                                                  │
│           ▼                                                                  │
│  ┌─────────────────┐        ┌─────────────────┐                             │
│  │ DEPLOY STAGING  │───────►│  SMOKE TESTS    │                             │
│  └─────────────────┘        └────────┬────────┘                             │
│                                      │                                       │
│           ┌──────────────────────────┘                                       │
│           │                                                                  │
│           ▼         (on version tag v*.*.*)                                 │
│  ┌─────────────────┐                                                         │
│  │ CREATE RELEASE  │ ◄── Automatic changelog generation                     │
│  └────────┬────────┘                                                         │
│           │                                                                  │
│           ├─────────────────┐                                               │
│           ▼                 ▼                                               │
│  ┌─────────────────┐  ┌─────────────────┐                                   │
│  │ PUBLISH TO PYPI │  │DEPLOY PRODUCTION│ ◄── Manual approval required      │
│  └─────────────────┘  └─────────────────┘                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

> 📖 **Full Details**: See [CI/CD Complete Guide](docs/CICD_GUIDE.md) for workflow explanations.

---

## 🛠️ Development Workflow

We follow the **GitHub Flow** branching strategy:

```
main (protected)
  │
  ├── feature/add-new-function
  │     └── Create PR → CI runs → Code review → Merge
  │
  ├── bugfix/fix-validation-error
  │     └── Create PR → CI runs → Code review → Merge
  │
  └── release/v1.0.0
        └── Tag → CD runs → Deploy
```

### Making Changes

```bash
# 1. Create a feature branch
git checkout -b feature/your-feature-name

# 2. Make your changes
# ... edit files ...

# 3. Run quality checks locally
black src/ tests/          # Format code
isort src/ tests/          # Sort imports
flake8 src/ tests/         # Lint code
pytest --cov=src           # Run tests

# 4. Commit (pre-commit hooks run automatically)
git add .
git commit -m "feat: add your feature description"

# 5. Push and create PR
git push origin feature/your-feature-name
```

> 📖 **Guidelines**: See [Contributing Guide](docs/CONTRIBUTING.md) for detailed workflow.

---

## 📊 Code Quality Standards

### Tools We Use

| Tool | Purpose | Configuration |
|------|---------|---------------|
| **Black** | Code formatting | `pyproject.toml` |
| **isort** | Import sorting | `pyproject.toml` |
| **flake8** | Linting | `.flake8` |
| **mypy** | Type checking | `pyproject.toml` |
| **Bandit** | Security scanning | `pyproject.toml` |
| **pytest** | Testing | `pyproject.toml` |
| **pre-commit** | Git hooks | `.pre-commit-config.yaml` |

### Quality Gates

All code must pass:
- ✅ **Formatting**: Black-compliant code style
- ✅ **Imports**: isort-organized imports
- ✅ **Linting**: Zero flake8 errors
- ✅ **Types**: mypy type checking
- ✅ **Security**: No Bandit warnings
- ✅ **Tests**: 80%+ code coverage
- ✅ **Build**: Successful package build

---

## 🧪 Testing Strategy

### Test Categories

```python
# Unit Tests - Test individual functions
def test_add_positive_numbers():
    calc = Calculator()
    assert calc.add(2, 3) == 5

# Parametrized Tests - Test multiple inputs
@pytest.mark.parametrize("a,b,expected", [(1,1,2), (0,0,0), (-1,1,0)])
def test_add_parametrized(a, b, expected):
    assert Calculator().add(a, b) == expected

# Edge Case Tests - Test boundaries
def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator().divide(10, 0)
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_calculator.py

# Run tests in parallel
pytest -n auto

# Run with verbose output
pytest -v
```

### Coverage Requirements

- **Minimum Coverage**: 80%
- **Coverage Report**: Generated on every CI run
- **Coverage Visualization**: HTML report in `htmlcov/`

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. ✍️ Make your changes following our coding standards
4. ✅ Ensure all tests pass (`pytest`)
5. 📝 Commit with a descriptive message
6. 🚀 Push to your fork (`git push origin feature/amazing-feature`)
7. 🔀 Create a Pull Request

> 📖 **Full Guide**: See [Contributing Guidelines](docs/CONTRIBUTING.md)

---

## 🔗 Quick Links

| Resource | Link |
|----------|------|
| 📦 GitHub Repository | [python-pro-with-cicd](https://github.com/yogeshwankhede007/python-pro-with-cicd) |
| 🐛 Issue Tracker | [Issues](https://github.com/yogeshwankhede007/python-pro-with-cicd/issues) |
| 📋 Project Board | [Projects](https://github.com/yogeshwankhede007/python-pro-with-cicd/projects) |
| 🔄 CI/CD Status | [Actions](https://github.com/yogeshwankhede007/python-pro-with-cicd/actions) |

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with ❤️ for the developer community
- Inspired by industry best practices from leading tech companies
- Special thanks to all contributors

---

<div align="center">

**⭐ If this project helped you learn CI/CD, please give it a star! ⭐**

Made with 💻 by [Yogesh Wankhede](https://github.com/yogeshwankhede007)

</div>
