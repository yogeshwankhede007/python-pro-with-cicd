# 📗 GitHub Best Practices Guide

> **A comprehensive guide to industry-standard GitHub workflows, conventions, and best practices for professional software development.**

---

## 📑 Table of Contents

1. [Repository Setup](#1-repository-setup)
2. [Branching Strategy](#2-branching-strategy)
3. [Commit Conventions](#3-commit-conventions)
4. [Pull Request Best Practices](#4-pull-request-best-practices)
5. [Code Review Guidelines](#5-code-review-guidelines)
6. [Issue Management](#6-issue-management)
7. [Release Management](#7-release-management)
8. [Security Best Practices](#8-security-best-practices)
9. [Documentation Standards](#9-documentation-standards)
10. [Team Collaboration](#10-team-collaboration)

---

## 1. Repository Setup

### 1.1 Essential Files Every Repository Should Have

| File | Purpose |
|------|---------|
| `README.md` | Project overview, setup instructions, usage examples |
| `LICENSE` | Legal terms for using the code |
| `.gitignore` | Files and folders Git should ignore |
| `CONTRIBUTING.md` | Guidelines for contributors |
| `CODE_OF_CONDUCT.md` | Community behavior expectations |
| `CHANGELOG.md` | History of changes and releases |
| `SECURITY.md` | Security policy and vulnerability reporting |

### 1.2 Repository Settings Checklist

```markdown
✅ Enable branch protection for `main`
✅ Require pull request reviews before merging
✅ Require status checks to pass before merging
✅ Require signed commits (recommended)
✅ Enable automatic deletion of head branches
✅ Set up CODEOWNERS file
✅ Configure security alerts
✅ Enable Dependabot for dependency updates
```

### 1.3 Branch Protection Rules

Configure these settings for your `main` branch:

```yaml
Branch Protection Settings:
  - Require pull request reviews: Yes
    - Required approving reviews: 1 (or more for larger teams)
    - Dismiss stale PR approvals: Yes
  - Require status checks: Yes
    - Required checks:
      - CI Pipeline
      - Code Quality
      - Tests
  - Require branches to be up to date: Yes
  - Include administrators: Yes (recommended)
  - Restrict who can push: Yes
```

---

## 2. Branching Strategy

### 2.1 GitHub Flow (Recommended for Most Projects)

```
┌─────────────────────────────────────────────────────────────────┐
│                        GITHUB FLOW                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  main ─────●─────●─────●─────●─────●─────●─────●────────────►   │
│            │     ↑     │     ↑     │     ↑     │                │
│            │     │     │     │     │     │     │                │
│  feature   └──●──┘     │     │     │     │     │                │
│                        │     │     │     │     │                │
│  bugfix                └──●──┘     │     │     │                │
│                                    │     │     │                │
│  hotfix                            └──●──┘     │                │
│                                                │                │
│  feature                                       └──●──●──●       │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘

Flow:
1. Create branch from main
2. Make changes and commit
3. Open Pull Request
4. Review and discuss
5. Merge to main
6. Delete branch
```

### 2.2 Branch Naming Conventions

```bash
# Feature branches
feature/add-user-authentication
feature/implement-search-api
feature/JIRA-123-user-profile

# Bug fix branches
bugfix/fix-login-redirect
bugfix/resolve-memory-leak
bugfix/JIRA-456-form-validation

# Hotfix branches (urgent production fixes)
hotfix/critical-security-patch
hotfix/database-connection-fix

# Release branches
release/v1.0.0
release/v2.1.0-beta

# Documentation branches
docs/update-api-reference
docs/add-installation-guide

# Experimental branches
experiment/new-algorithm
spike/evaluate-new-framework
```

### 2.3 Branch Naming Rules

| Rule | Good ✅ | Bad ❌ |
|------|---------|--------|
| Use lowercase | `feature/add-login` | `Feature/Add-Login` |
| Use hyphens | `bugfix/fix-memory-leak` | `bugfix/fix_memory_leak` |
| Be descriptive | `feature/user-authentication` | `feature/auth` |
| Include ticket ID | `feature/JIRA-123-add-login` | `feature/add-login` |
| Keep it short | `feature/add-search` | `feature/add-search-functionality-to-main-page` |

---

## 3. Commit Conventions

### 3.1 Conventional Commits Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### 3.2 Commit Types

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(auth): add OAuth2 login` |
| `fix` | Bug fix | `fix(api): resolve null pointer exception` |
| `docs` | Documentation | `docs(readme): update installation steps` |
| `style` | Code style (formatting) | `style: fix indentation in utils.py` |
| `refactor` | Code refactoring | `refactor(db): optimize query performance` |
| `test` | Adding tests | `test(auth): add unit tests for login` |
| `chore` | Maintenance | `chore(deps): update dependencies` |
| `perf` | Performance | `perf(api): cache database queries` |
| `ci` | CI/CD changes | `ci: add Python 3.12 to test matrix` |
| `build` | Build system | `build: update webpack config` |
| `revert` | Revert changes | `revert: revert commit abc123` |

### 3.3 Commit Message Examples

```bash
# Good commit messages ✅
feat(calculator): add power function for exponentiation

Add a new power() method to Calculator class that raises
a base number to a given exponent. Includes support for
negative exponents.

Closes #42

# ---

fix(validators): handle empty string in email validation

Previously, passing an empty string would cause a regex
error. Now returns False for empty strings.

Fixes #58

# ---

docs(api): add examples for all public methods

- Add docstrings with examples
- Include edge case documentation
- Add type hints

# Bad commit messages ❌
- "fixed stuff"
- "WIP"
- "asdfasdf"
- "changes"
- "update"
```

### 3.4 Commit Best Practices

```markdown
✅ DO:
- Write clear, descriptive messages
- Use present tense ("add" not "added")
- Reference issues and PRs
- Keep commits atomic (one logical change per commit)
- Sign your commits (git commit -S)

❌ DON'T:
- Commit large changes without explanation
- Mix unrelated changes in one commit
- Use vague messages like "fix bug"
- Commit commented-out code
- Commit sensitive information
```

---

## 4. Pull Request Best Practices

### 4.1 PR Title Format

```
<type>(<scope>): <description>

Examples:
feat(auth): implement two-factor authentication
fix(api): resolve rate limiting issue
docs(readme): add deployment instructions
```

### 4.2 PR Description Template

```markdown
## 📋 Description
Brief description of what this PR does.

## 🎯 Related Issue
Fixes #(issue number)

## 🔄 Type of Change
- [ ] 🐛 Bug fix (non-breaking change fixing an issue)
- [ ] ✨ New feature (non-breaking change adding functionality)
- [ ] 💥 Breaking change (fix or feature causing existing functionality to break)
- [ ] 📚 Documentation update
- [ ] 🔧 Configuration change
- [ ] ♻️ Refactoring (no functional changes)

## 🧪 How Has This Been Tested?
Describe the tests you ran to verify your changes.

- [ ] Unit tests
- [ ] Integration tests
- [ ] Manual testing

## 📸 Screenshots (if applicable)
Add screenshots to help explain your changes.

## ✅ Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or my feature works
- [ ] New and existing unit tests pass locally with my changes
```

### 4.3 PR Size Guidelines

| Size | Lines Changed | Review Time | Recommendation |
|------|---------------|-------------|----------------|
| 🟢 Small | < 200 | < 30 min | Ideal |
| 🟡 Medium | 200-400 | 30-60 min | Acceptable |
| 🟠 Large | 400-800 | 1-2 hours | Consider splitting |
| 🔴 X-Large | > 800 | > 2 hours | Must split |

### 4.4 PR Checklist

```markdown
Before submitting:
✅ Branch is up to date with main
✅ All tests pass locally
✅ Code follows style guidelines
✅ No console.log/print statements left
✅ No commented-out code
✅ Documentation updated if needed
✅ PR title follows conventions
✅ Description is complete
✅ Related issues are linked
```

---

## 5. Code Review Guidelines

### 5.1 For Reviewers

```markdown
## Review Checklist

### Code Quality
- [ ] Code is readable and self-documenting
- [ ] Functions/methods are focused and concise
- [ ] No code duplication (DRY principle)
- [ ] Proper error handling
- [ ] No security vulnerabilities

### Testing
- [ ] Tests cover the changes
- [ ] Edge cases are tested
- [ ] Tests are readable and maintainable

### Documentation
- [ ] Public APIs are documented
- [ ] Complex logic has comments
- [ ] README updated if needed

### Performance
- [ ] No obvious performance issues
- [ ] Database queries are optimized
- [ ] No memory leaks
```

### 5.2 Review Comment Prefixes

| Prefix | Meaning | Action Required |
|--------|---------|-----------------|
| `[BLOCKER]` | Must fix before merge | Yes |
| `[SUGGESTION]` | Nice to have improvement | Optional |
| `[QUESTION]` | Need clarification | Response needed |
| `[NIT]` | Minor style/preference | Optional |
| `[PRAISE]` | Good work! | None |

### 5.3 Giving Constructive Feedback

```markdown
# Good feedback ✅
"Consider using a dictionary comprehension here for better readability:
```python
result = {k: v for k, v in items if v > 0}
```
This would reduce the code from 5 lines to 1."

# Bad feedback ❌
"This code is wrong."
"Why did you do it this way?"
"This doesn't make sense."
```

### 5.4 Review Response Time SLA

| PR Priority | Response Time |
|-------------|---------------|
| 🔴 Critical/Hotfix | < 2 hours |
| 🟠 High | < 4 hours |
| 🟡 Normal | < 24 hours |
| 🟢 Low | < 48 hours |

---

## 6. Issue Management

### 6.1 Issue Templates

#### Bug Report Template

```markdown
---
name: 🐛 Bug Report
about: Report a bug to help us improve
labels: bug, needs-triage
---

## 🐛 Bug Description
A clear description of the bug.

## 📝 Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## ✅ Expected Behavior
What you expected to happen.

## ❌ Actual Behavior
What actually happened.

## 🖥️ Environment
- OS: [e.g., macOS 14.0]
- Python version: [e.g., 3.11]
- Package version: [e.g., 1.0.0]

## 📸 Screenshots
If applicable, add screenshots.

## 📋 Additional Context
Any other relevant information.
```

#### Feature Request Template

```markdown
---
name: ✨ Feature Request
about: Suggest a new feature
labels: enhancement, needs-triage
---

## ✨ Feature Description
A clear description of the feature.

## 🎯 Problem Statement
What problem does this solve?

## 💡 Proposed Solution
How should this work?

## 🔄 Alternatives Considered
Other solutions you've considered.

## 📋 Additional Context
Any other relevant information.
```

### 6.2 Issue Labels

| Label | Color | Description |
|-------|-------|-------------|
| `bug` | 🔴 Red | Something isn't working |
| `enhancement` | 🔵 Blue | New feature request |
| `documentation` | 📘 Light Blue | Documentation improvements |
| `good first issue` | 🟢 Green | Good for newcomers |
| `help wanted` | 🟡 Yellow | Extra attention needed |
| `priority: critical` | 🔴 Red | Must fix immediately |
| `priority: high` | 🟠 Orange | Fix soon |
| `priority: medium` | 🟡 Yellow | Normal priority |
| `priority: low` | 🟢 Green | Nice to have |
| `wontfix` | ⚪ White | Will not be addressed |
| `duplicate` | ⚪ Grey | Duplicate issue |

---

## 7. Release Management

### 7.1 Semantic Versioning (SemVer)

```
MAJOR.MINOR.PATCH

1.0.0 → 1.0.1 (Patch: Bug fixes)
1.0.1 → 1.1.0 (Minor: New features, backward compatible)
1.1.0 → 2.0.0 (Major: Breaking changes)
```

### 7.2 Version Bump Guidelines

| Change Type | Version Bump | Example |
|-------------|--------------|---------|
| Bug fix | PATCH | 1.0.0 → 1.0.1 |
| New feature (backward compatible) | MINOR | 1.0.1 → 1.1.0 |
| Breaking change | MAJOR | 1.1.0 → 2.0.0 |
| Pre-release | Suffix | 2.0.0-alpha.1 |

### 7.3 Release Process

```bash
# 1. Update version in pyproject.toml and __init__.py
# 2. Update CHANGELOG.md
# 3. Commit changes
git add .
git commit -m "chore(release): prepare v1.2.0"

# 4. Create tag
git tag -a v1.2.0 -m "Release v1.2.0"

# 5. Push with tags
git push origin main --tags
```

### 7.4 Changelog Format

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

## [1.2.0] - 2026-01-09

### Added
- New feature X (#123)
- Support for Python 3.12 (#124)

### Changed
- Improved performance of function Y (#125)

### Fixed
- Bug in validation logic (#126)

### Deprecated
- Old API endpoint (will be removed in v2.0.0)

### Removed
- Legacy support for Python 3.8

### Security
- Fixed XSS vulnerability (#127)

## [1.1.0] - 2025-12-01
...
```

---

## 8. Security Best Practices

### 8.1 Never Commit These

```gitignore
# Secrets and credentials
.env
.env.local
*.pem
*.key
secrets.json
credentials.json
config.local.py

# API keys
**/api_keys.*
**/secrets.*

# Database
*.db
*.sqlite
```

### 8.2 Use GitHub Secrets

```yaml
# In GitHub Actions workflow
env:
  API_KEY: ${{ secrets.API_KEY }}
  DATABASE_URL: ${{ secrets.DATABASE_URL }}
```

### 8.3 Security Checklist

```markdown
✅ Enable Dependabot alerts
✅ Enable secret scanning
✅ Enable code scanning (CodeQL)
✅ Require signed commits
✅ Use branch protection rules
✅ Review access permissions regularly
✅ Use environment secrets, not repository secrets
✅ Rotate credentials regularly
✅ Use OIDC for cloud deployments
```

### 8.4 Security Policy (SECURITY.md)

```markdown
# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.x.x   | :white_check_mark: |
| < 1.0   | :x:                |

## Reporting a Vulnerability

Please report security vulnerabilities to: security@example.com

Do NOT create a public issue for security vulnerabilities.

We will respond within 48 hours and work with you to
understand and address the issue.
```

---

## 9. Documentation Standards

### 9.1 Code Documentation

```python
def calculate_interest(
    principal: float,
    rate: float,
    time: int,
    compound: bool = True
) -> float:
    """
    Calculate interest on a principal amount.

    This function calculates either simple or compound interest
    based on the provided parameters.

    Args:
        principal: The initial amount of money.
        rate: Annual interest rate as a decimal (e.g., 0.05 for 5%).
        time: Time period in years.
        compound: If True, calculate compound interest; otherwise simple.

    Returns:
        The calculated interest amount.

    Raises:
        ValueError: If principal or rate is negative, or time is not positive.

    Examples:
        >>> calculate_interest(1000, 0.05, 2)
        102.5
        >>> calculate_interest(1000, 0.05, 2, compound=False)
        100.0

    Note:
        Compound interest is calculated annually.
    """
```

### 9.2 README Structure

```markdown
# Project Name

Brief description (1-2 sentences)

## Badges
CI status, version, license, etc.

## Table of Contents
For longer READMEs

## Features
What does this project do?

## Installation
How to install

## Quick Start
Get running in 5 minutes

## Usage
Detailed usage examples

## Configuration
Available options

## API Reference
For libraries

## Contributing
How to contribute

## License
License information
```

---

## 10. Team Collaboration

### 10.1 CODEOWNERS File

```
# .github/CODEOWNERS

# Default owners for everything
* @team-lead @senior-dev

# Frontend code
/src/frontend/ @frontend-team

# Backend code
/src/backend/ @backend-team

# Documentation
/docs/ @tech-writer @team-lead

# CI/CD configuration
/.github/ @devops-team

# Security-sensitive files
/src/auth/ @security-team @team-lead
```

### 10.2 Team Communication

| Situation | Channel |
|-----------|---------|
| Code discussion | PR comments |
| Quick questions | Slack/Teams |
| Design decisions | GitHub Discussions |
| Bug reports | GitHub Issues |
| Knowledge sharing | Documentation |
| Urgent issues | Direct message + Issue |

### 10.3 Response Time Expectations

| Activity | Expected Response |
|----------|-------------------|
| PR review request | Within 24 hours |
| Issue assignment | Within 48 hours |
| Critical bug | Within 2 hours |
| Direct mention | Within 4 hours |
| General question | Within 24 hours |

---

## 📚 Additional Resources

- [GitHub Flow Guide](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)
- [Keep a Changelog](https://keepachangelog.com/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

---

<div align="center">

**Following these best practices will make your team more efficient and your codebase more maintainable! 🚀**

</div>
