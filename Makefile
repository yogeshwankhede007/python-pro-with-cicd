# Makefile for Python CI/CD Demo Project
# =======================================
# This Makefile provides convenient shortcuts for common development tasks.
# Usage: make <target>

.PHONY: help install install-dev test test-cov lint format type-check security clean build all

# Default target - show help
help:
	@echo "Python CI/CD Demo - Available Commands"
	@echo "======================================="
	@echo ""
	@echo "Setup:"
	@echo "  make install       Install production dependencies"
	@echo "  make install-dev   Install development dependencies"
	@echo "  make setup         Complete project setup"
	@echo ""
	@echo "Testing:"
	@echo "  make test          Run tests"
	@echo "  make test-cov      Run tests with coverage report"
	@echo "  make test-fast     Run tests in parallel"
	@echo ""
	@echo "Code Quality:"
	@echo "  make lint          Run all linters"
	@echo "  make format        Format code with black and isort"
	@echo "  make type-check    Run mypy type checker"
	@echo "  make security      Run security checks"
	@echo "  make check         Run all quality checks"
	@echo ""
	@echo "Build:"
	@echo "  make build         Build the package"
	@echo "  make clean         Remove build artifacts"
	@echo ""
	@echo "CI/CD Simulation:"
	@echo "  make ci            Simulate full CI pipeline locally"
	@echo ""

# =============================================================================
# Setup Targets
# =============================================================================

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pip install -e .
	pre-commit install

setup: install-dev
	@echo "✅ Development environment set up successfully!"

# =============================================================================
# Testing Targets
# =============================================================================

test:
	pytest tests/ -v

test-cov:
	pytest tests/ -v --cov=src --cov-report=html --cov-report=term-missing
	@echo ""
	@echo "📊 Coverage report generated: htmlcov/index.html"

test-fast:
	pytest tests/ -v -n auto

test-ci:
	pytest tests/ -v --cov=src --cov-report=xml --cov-fail-under=80

# =============================================================================
# Code Quality Targets
# =============================================================================

lint:
	@echo "🔎 Running flake8..."
	flake8 src/ tests/
	@echo "✅ Linting passed!"

format:
	@echo "🎨 Formatting code with black..."
	black src/ tests/
	@echo "📑 Sorting imports with isort..."
	isort src/ tests/
	@echo "✅ Code formatted!"

format-check:
	@echo "🎨 Checking code formatting..."
	black --check --diff src/ tests/
	@echo "📑 Checking import sorting..."
	isort --check-only --diff src/ tests/
	@echo "✅ Format check passed!"

type-check:
	@echo "🔤 Running mypy type checker..."
	mypy src/ --ignore-missing-imports
	@echo "✅ Type check passed!"

security:
	@echo "🛡️ Running bandit security scan..."
	bandit -r src/ -f txt
	@echo "✅ Security scan passed!"

check: format-check lint type-check security
	@echo ""
	@echo "✅ All quality checks passed!"

# =============================================================================
# Build Targets
# =============================================================================

build: clean
	@echo "📦 Building package..."
	python -m build
	@echo "🔍 Checking package..."
	twine check dist/*
	@echo "✅ Build complete!"

clean:
	@echo "🧹 Cleaning build artifacts..."
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .mypy_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf coverage.xml
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Clean complete!"

# =============================================================================
# CI/CD Simulation
# =============================================================================

ci: clean format-check lint type-check security test-ci build
	@echo ""
	@echo "============================================="
	@echo "🎉 CI Pipeline Simulation Complete!"
	@echo "============================================="
	@echo ""
	@echo "All checks passed. Your code is ready for:"
	@echo "  ✅ Committing"
	@echo "  ✅ Creating a Pull Request"
	@echo "  ✅ Merging to main"
	@echo ""

# =============================================================================
# Development Helpers
# =============================================================================

# Run pre-commit on all files
pre-commit:
	pre-commit run --all-files

# Watch for changes and run tests (requires pytest-watch)
watch:
	ptw -- -v

# Generate documentation
docs:
	mkdocs serve

# Create a new release tag
release-patch:
	@echo "Creating patch release..."
	bumpversion patch

release-minor:
	@echo "Creating minor release..."
	bumpversion minor

release-major:
	@echo "Creating major release..."
	bumpversion major
