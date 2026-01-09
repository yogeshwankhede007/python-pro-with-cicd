#!/usr/bin/env python3
"""
Demo Script - Demonstrates the functionality of all modules

This script is for learning purposes and shows examples of using
the calculator, string utilities, and validator functions.
"""

from src.calculator import Calculator
from src.string_utils import (
    capitalize_words,
    count_words,
    extract_emails,
    find_common_prefix,
    is_palindrome,
    mask_sensitive_data,
    reverse_string,
    slugify,
    truncate,
)
from src.validators import (
    validate_credit_card,
    validate_date,
    validate_email,
    validate_password,
    validate_phone,
    validate_url,
)


def print_section(title: str) -> None:
    """Print a section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def demo_calculator() -> None:
    """Demonstrate calculator functionality."""
    print_section("Calculator Demo")

    calc = Calculator()

    print("\n1. Basic Arithmetic Operations:")
    result = calc.add(15, 25)
    print(f"   15 + 25 = {result}")

    result = calc.subtract(50, 23)
    print(f"   50 - 23 = {result}")

    result = calc.multiply(7, 8)
    print(f"   7 × 8 = {result}")

    result = calc.divide(100, 4)
    print(f"   100 ÷ 4 = {result}")

    result = calc.power(2, 10)
    print(f"   2^10 = {result}")

    result = calc.modulo(17, 5)
    print(f"   17 % 5 = {result}")

    print("\n2. Operation History:")
    history = calc.get_history()
    for i, op in enumerate(history, 1):
        print(f"   {i}. {op}")


def demo_string_utils() -> None:
    """Demonstrate string utilities functionality."""
    print_section("String Utilities Demo")

    print("\n1. String Reversal:")
    text = "Hello, Python!"
    print(f"   Original: {text}")
    print(f"   Reversed: {reverse_string(text)}")

    print("\n2. Palindrome Check:")
    words = ["racecar", "hello", "A man a plan a canal Panama"]
    for word in words:
        result = is_palindrome(word)
        print(f"   '{word}' is {'a' if result else 'not a'} palindrome")

    print("\n3. Word Counting:")
    sentence = "This is a sample sentence for word counting"
    print(f"   Sentence: '{sentence}'")
    print(f"   Word count: {count_words(sentence)}")

    print("\n4. Text Truncation:")
    long_text = "This is a very long text that needs to be truncated"
    print(f"   Original: {long_text}")
    print(f"   Truncated: {truncate(long_text, 30)}")

    print("\n5. URL Slugification:")
    titles = ["Hello World!", "Python CI/CD Guide", "Best Practices 2026"]
    for title in titles:
        print(f"   '{title}' → '{slugify(title)}'")

    print("\n6. Email Extraction:")
    text = "Contact us at support@example.com or info@company.org"
    emails = extract_emails(text)
    print(f"   Text: '{text}'")
    print(f"   Emails found: {emails}")

    print("\n7. Sensitive Data Masking:")
    card_number = "1234567890123456"
    print(f"   Original: {card_number}")
    print(f"   Masked: {mask_sensitive_data(card_number)}")

    print("\n8. Common Prefix Finding:")
    words_list = ["flower", "flow", "flight"]
    prefix = find_common_prefix(words_list)
    print(f"   Words: {words_list}")
    print(f"   Common prefix: '{prefix}'")


def demo_validators() -> None:
    """Demonstrate validator functionality."""
    print_section("Validators Demo")

    print("\n1. Email Validation:")
    emails = ["user@example.com", "invalid-email", "test@domain.co.uk"]
    for email in emails:
        is_valid = validate_email(email)
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"   {status}: {email}")

    print("\n2. Phone Validation:")
    phones = ["2125551234", "123", "+12125551234"]
    for phone in phones:
        is_valid = validate_phone(phone, "US")
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"   {status}: {phone}")

    print("\n3. Password Strength Check:")
    passwords = ["SecurePass123!", "weak", "NoDigits!"]
    for pwd in passwords:
        result = validate_password(pwd)
        if result["valid"]:
            print(f"   ✓ Strong password")
        else:
            print(f"   ✗ Weak password: {', '.join(result['errors'])}")

    print("\n4. Date Validation:")
    dates = ["2026-01-09", "2026-13-45", "01/09/2026"]
    for date in dates:
        is_valid, parsed = validate_date(date)
        if is_valid:
            print(f"   ✓ Valid date: {date} → {parsed}")
        else:
            print(f"   ✗ Invalid date: {date}")

    print("\n5. URL Validation:")
    urls = ["https://example.com", "not-a-url", "http://localhost:8080"]
    for url in urls:
        is_valid = validate_url(url)
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"   {status}: {url}")

    print("\n6. Credit Card Validation:")
    cards = ["4532015112830366", "1234567890123456"]
    for card in cards:
        result = validate_credit_card(card)
        if result["valid"]:
            print(f"   ✓ Valid {result['card_type']}: {card}")
        else:
            print(f"   ✗ {result['error']}: {card}")


def main() -> None:
    """Main demo function."""
    print("\n" + "=" * 60)
    print("  Python CI/CD Project - Functionality Demo")
    print("  Learning Python with Automated Testing")
    print("=" * 60)

    demo_calculator()
    demo_string_utils()
    demo_validators()

    print("\n" + "=" * 60)
    print("  Demo Complete! All modules working correctly.")
    print("  Check the tests/ directory for comprehensive test cases.")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
