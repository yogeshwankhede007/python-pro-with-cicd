"""
Data Validator Module - Input validation utilities.

This module provides validation functions commonly needed in web applications
and data processing pipelines.
"""

import re
from datetime import datetime
from typing import Any, Optional


class ValidationError(Exception):
    """Custom exception for validation errors."""

    pass


def validate_email(email: str) -> bool:
    """
    Validate an email address format.

    Args:
        email: The email address to validate

    Returns:
        True if valid, False otherwise

    Examples:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def validate_phone(phone: str, country_code: str = "US") -> bool:
    """
    Validate a phone number format.

    Args:
        phone: The phone number to validate
        country_code: The country code for validation rules

    Returns:
        True if valid, False otherwise
    """
    # Remove common separators
    cleaned = re.sub(r"[\s\-\(\)\.]", "", phone)

    if country_code == "US":
        # US phone: 10 digits, optionally starting with +1
        pattern = r"^(\+1)?[2-9]\d{9}$"
    else:
        # Generic international: 7-15 digits
        pattern = r"^\+?\d{7,15}$"

    return bool(re.match(pattern, cleaned))


def validate_password(
    password: str,
    min_length: int = 8,
    require_uppercase: bool = True,
    require_lowercase: bool = True,
    require_digit: bool = True,
    require_special: bool = True,
) -> dict[str, Any]:
    """
    Validate password strength.

    Args:
        password: The password to validate
        min_length: Minimum required length
        require_uppercase: Require at least one uppercase letter
        require_lowercase: Require at least one lowercase letter
        require_digit: Require at least one digit
        require_special: Require at least one special character

    Returns:
        Dictionary with 'valid' boolean and 'errors' list
    """
    errors = []

    if len(password) < min_length:
        errors.append(f"Password must be at least {min_length} characters")

    if require_uppercase and not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter")

    if require_lowercase and not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter")

    if require_digit and not re.search(r"\d", password):
        errors.append("Password must contain at least one digit")

    if require_special and not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password must contain at least one special character")

    return {"valid": len(errors) == 0, "errors": errors}


def validate_date(
    date_string: str, date_format: str = "%Y-%m-%d"
) -> tuple[bool, Optional[datetime]]:
    """
    Validate and parse a date string.

    Args:
        date_string: The date string to validate
        date_format: Expected date format

    Returns:
        Tuple of (is_valid, parsed_datetime or None)
    """
    try:
        parsed = datetime.strptime(date_string, date_format)
        return True, parsed
    except ValueError:
        return False, None


def validate_url(url: str) -> bool:
    """
    Validate a URL format.

    Args:
        url: The URL to validate

    Returns:
        True if valid, False otherwise
    """
    pattern = (
        r"^https?://"  # http:// or https://
        r"(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|"  # domain
        r"localhost|"  # localhost
        r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"  # or IP
        r"(?::\d+)?"  # optional port
        r"(?:/?|[/?]\S+)$"
    )
    return bool(re.match(pattern, url, re.IGNORECASE))


def validate_credit_card(card_number: str) -> dict[str, Any]:
    """
    Validate a credit card number using Luhn algorithm.

    Args:
        card_number: The card number to validate

    Returns:
        Dictionary with 'valid', 'card_type', and any errors
    """
    # Remove spaces and dashes
    cleaned = re.sub(r"[\s-]", "", card_number)

    # Check if all digits
    if not cleaned.isdigit():
        return {
            "valid": False,
            "card_type": None,
            "error": "Card number must contain only digits",
        }

    # Detect card type
    card_type = None
    if cleaned.startswith("4"):
        card_type = "Visa"
    elif cleaned.startswith(("51", "52", "53", "54", "55")):
        card_type = "Mastercard"
    elif cleaned.startswith(("34", "37")):
        card_type = "American Express"
    elif cleaned.startswith("6011"):
        card_type = "Discover"

    # Luhn algorithm
    def luhn_check(num: str) -> bool:
        digits = [int(d) for d in num]
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]

        total = sum(odd_digits)
        for d in even_digits:
            total += sum(divmod(d * 2, 10))

        return total % 10 == 0

    is_valid = luhn_check(cleaned)

    return {
        "valid": is_valid,
        "card_type": card_type,
        "error": None if is_valid else "Invalid card number",
    }


def validate_json_schema(data: dict, schema: dict) -> dict[str, Any]:
    """
    Simple JSON schema validation.

    Args:
        data: The data dictionary to validate
        schema: Schema with 'required' fields and 'types'

    Returns:
        Dictionary with 'valid' and 'errors'
    """
    errors = []

    # Check required fields
    required_fields = schema.get("required", [])
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    # Check types
    field_types = schema.get("types", {})
    for field, expected_type in field_types.items():
        if field in data and not isinstance(data[field], expected_type):
            errors.append(
                f"Field '{field}' should be {expected_type.__name__}, "
                f"got {type(data[field]).__name__}"
            )

    return {"valid": len(errors) == 0, "errors": errors}
