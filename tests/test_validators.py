"""
Unit tests for the Validators module.

These tests demonstrate testing validation functions
with various valid and invalid inputs.
"""

import pytest
from datetime import datetime
from src.validators import (
    validate_email,
    validate_phone,
    validate_password,
    validate_date,
    validate_url,
    validate_credit_card,
    validate_json_schema,
)


class TestValidateEmail:
    """Test suite for email validation."""

    @pytest.mark.parametrize(
        "email",
        [
            "user@example.com",
            "user.name@example.com",
            "user+tag@example.com",
            "user@sub.domain.com",
            "user123@example.co.uk",
        ],
    )
    def test_valid_emails(self, email):
        """Test valid email formats."""
        assert validate_email(email) is True

    @pytest.mark.parametrize(
        "email",
        [
            "invalid",
            "invalid@",
            "@example.com",
            "user@.com",
            "user@example",
            "",
        ],
    )
    def test_invalid_emails(self, email):
        """Test invalid email formats."""
        assert validate_email(email) is False


class TestValidatePhone:
    """Test suite for phone validation."""

    @pytest.mark.parametrize(
        "phone",
        [
            "2125551234",
            "212-555-1234",
            "(212) 555-1234",
            "+12125551234",
            "212.555.1234",
        ],
    )
    def test_valid_us_phones(self, phone):
        """Test valid US phone formats."""
        assert validate_phone(phone, "US") is True

    @pytest.mark.parametrize(
        "phone",
        [
            "123",  # Too short
            "123456",  # Still too short
            "12345678901234567",  # Too long for generic
        ],
    )
    def test_invalid_phones(self, phone):
        """Test invalid phone formats."""
        assert validate_phone(phone, "US") is False

    def test_international_phone(self):
        """Test international phone format."""
        assert validate_phone("+441onal234567890", "UK") is True


class TestValidatePassword:
    """Test suite for password validation."""

    def test_strong_password(self):
        """Test a strong password."""
        result = validate_password("SecurePass123!")
        assert result["valid"] is True
        assert len(result["errors"]) == 0

    def test_weak_password_short(self):
        """Test password too short."""
        result = validate_password("Short1!")
        assert result["valid"] is False
        assert any("at least 8 characters" in e for e in result["errors"])

    def test_password_no_uppercase(self):
        """Test password without uppercase."""
        result = validate_password("lowercase123!")
        assert result["valid"] is False
        assert any("uppercase" in e for e in result["errors"])

    def test_password_no_lowercase(self):
        """Test password without lowercase."""
        result = validate_password("UPPERCASE123!")
        assert result["valid"] is False
        assert any("lowercase" in e for e in result["errors"])

    def test_password_no_digit(self):
        """Test password without digit."""
        result = validate_password("NoDigitsHere!")
        assert result["valid"] is False
        assert any("digit" in e for e in result["errors"])

    def test_password_no_special(self):
        """Test password without special character."""
        result = validate_password("NoSpecial123")
        assert result["valid"] is False
        assert any("special" in e for e in result["errors"])

    def test_password_custom_requirements(self):
        """Test password with custom requirements."""
        result = validate_password(
            "simplepassword",
            min_length=8,
            require_uppercase=False,
            require_digit=False,
            require_special=False,
        )
        assert result["valid"] is True


class TestValidateDate:
    """Test suite for date validation."""

    def test_valid_date_default_format(self):
        """Test valid date with default format."""
        is_valid, parsed = validate_date("2024-01-15")
        assert is_valid is True
        assert parsed == datetime(2024, 1, 15)

    def test_valid_date_custom_format(self):
        """Test valid date with custom format."""
        is_valid, parsed = validate_date("15/01/2024", "%d/%m/%Y")
        assert is_valid is True
        assert parsed.day == 15

    def test_invalid_date_format(self):
        """Test invalid date format."""
        is_valid, parsed = validate_date("not-a-date")
        assert is_valid is False
        assert parsed is None

    def test_invalid_date_wrong_format(self):
        """Test date with wrong format."""
        is_valid, parsed = validate_date("01-15-2024", "%Y-%m-%d")
        assert is_valid is False


class TestValidateUrl:
    """Test suite for URL validation."""

    @pytest.mark.parametrize(
        "url",
        [
            "http://example.com",
            "https://example.com",
            "https://www.example.com",
            "https://sub.domain.example.com",
            "http://localhost",
            "http://localhost:8080",
            "https://example.com/path",
            "https://example.com/path?query=value",
            "http://192.168.1.1",
            "http://192.168.1.1:8080",
        ],
    )
    def test_valid_urls(self, url):
        """Test valid URL formats."""
        assert validate_url(url) is True

    @pytest.mark.parametrize(
        "url",
        [
            "not-a-url",
            "ftp://example.com",  # Only http/https
            "http://",
            "example.com",  # Missing protocol
            "",
        ],
    )
    def test_invalid_urls(self, url):
        """Test invalid URL formats."""
        assert validate_url(url) is False


class TestValidateCreditCard:
    """Test suite for credit card validation."""

    def test_valid_visa(self):
        """Test valid Visa card."""
        result = validate_credit_card("4111111111111111")
        assert result["valid"] is True
        assert result["card_type"] == "Visa"

    def test_valid_mastercard(self):
        """Test valid Mastercard."""
        result = validate_credit_card("5500000000000004")
        assert result["valid"] is True
        assert result["card_type"] == "Mastercard"

    def test_valid_with_spaces(self):
        """Test card number with spaces."""
        result = validate_credit_card("4111 1111 1111 1111")
        assert result["valid"] is True

    def test_valid_with_dashes(self):
        """Test card number with dashes."""
        result = validate_credit_card("4111-1111-1111-1111")
        assert result["valid"] is True

    def test_invalid_card(self):
        """Test invalid card number."""
        result = validate_credit_card("1234567890123456")
        assert result["valid"] is False

    def test_non_digit_card(self):
        """Test card with non-digit characters."""
        result = validate_credit_card("4111-abcd-1111-1111")
        assert result["valid"] is False


class TestValidateJsonSchema:
    """Test suite for JSON schema validation."""

    def test_valid_schema(self):
        """Test data matching schema."""
        schema = {
            "required": ["name", "email"],
            "types": {"name": str, "email": str, "age": int},
        }
        data = {"name": "John", "email": "john@example.com", "age": 30}
        result = validate_json_schema(data, schema)
        assert result["valid"] is True

    def test_missing_required_field(self):
        """Test data missing required field."""
        schema = {"required": ["name", "email"]}
        data = {"name": "John"}
        result = validate_json_schema(data, schema)
        assert result["valid"] is False
        assert any("email" in e for e in result["errors"])

    def test_wrong_type(self):
        """Test data with wrong type."""
        schema = {"types": {"age": int}}
        data = {"age": "thirty"}
        result = validate_json_schema(data, schema)
        assert result["valid"] is False
        assert any("age" in e for e in result["errors"])

    def test_empty_schema(self):
        """Test with empty schema (everything valid)."""
        result = validate_json_schema({"any": "data"}, {})
        assert result["valid"] is True
