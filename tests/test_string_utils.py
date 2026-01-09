"""Unit tests for the String Utilities module.

These tests demonstrate testing various string manipulation functions
with different edge cases and scenarios.
"""

import pytest

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


class TestReverseString:
    """Test suite for reverse_string function."""

    def test_reverse_simple_string(self):
        """Test reversing a simple string."""
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty_string(self):
        """Test reversing an empty string."""
        assert reverse_string("") == ""

    def test_reverse_single_char(self):
        """Test reversing a single character."""
        assert reverse_string("a") == "a"

    def test_reverse_palindrome(self):
        """Test reversing a palindrome."""
        assert reverse_string("racecar") == "racecar"

    def test_reverse_with_spaces(self):
        """Test reversing string with spaces."""
        assert reverse_string("hello world") == "dlrow olleh"


class TestIsPalindrome:
    """Test suite for is_palindrome function."""

    def test_simple_palindrome(self):
        """Test simple palindrome."""
        assert is_palindrome("racecar") is True

    def test_not_palindrome(self):
        """Test non-palindrome."""
        assert is_palindrome("hello") is False

    def test_palindrome_with_spaces(self):
        """Test palindrome with spaces."""
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_palindrome_case_sensitive(self):
        """Test palindrome with case sensitivity."""
        assert is_palindrome("RaceCar", ignore_case=False) is False
        assert is_palindrome("RaceCar", ignore_case=True) is True

    def test_palindrome_with_spaces_strict(self):
        """Test palindrome without ignoring spaces."""
        assert is_palindrome("race car", ignore_spaces=False) is False

    def test_empty_string_palindrome(self):
        """Test empty string as palindrome."""
        assert is_palindrome("") is True


class TestCountWords:
    """Test suite for count_words function."""

    def test_count_simple_sentence(self):
        """Test counting words in simple sentence."""
        assert count_words("Hello world") == 2

    def test_count_empty_string(self):
        """Test counting words in empty string."""
        assert count_words("") == 0

    def test_count_whitespace_only(self):
        """Test counting words in whitespace-only string."""
        assert count_words("   ") == 0

    def test_count_multiple_spaces(self):
        """Test counting words with multiple spaces."""
        assert count_words("Hello    world") == 2

    def test_count_single_word(self):
        """Test counting single word."""
        assert count_words("Hello") == 1


class TestTruncate:
    """Test suite for truncate function."""

    def test_truncate_long_string(self):
        """Test truncating a long string."""
        result = truncate("Hello World", 8)
        assert result == "Hello..."
        assert len(result) == 8

    def test_truncate_short_string(self):
        """Test truncating string shorter than max length."""
        assert truncate("Hello", 10) == "Hello"

    def test_truncate_exact_length(self):
        """Test truncating string at exact max length."""
        assert truncate("Hello", 5) == "Hello"

    def test_truncate_custom_suffix(self):
        """Test truncating with custom suffix."""
        assert truncate("Hello World", 9, suffix=">>") == "Hello W>>"

    def test_truncate_invalid_max_length(self):
        """Test truncating with invalid max length."""
        with pytest.raises(ValueError):
            truncate("Hello", 2, suffix="...")


class TestSlugify:
    """Test suite for slugify function."""

    def test_slugify_simple(self):
        """Test slugifying simple string."""
        assert slugify("Hello World") == "hello-world"

    def test_slugify_special_chars(self):
        """Test slugifying string with special characters."""
        assert slugify("Hello World!") == "hello-world"

    def test_slugify_multiple_spaces(self):
        """Test slugifying string with multiple spaces."""
        assert slugify("Hello   World") == "hello-world"

    def test_slugify_already_slug(self):
        """Test slugifying an already slugified string."""
        assert slugify("hello-world") == "hello-world"

    def test_slugify_numbers(self):
        """Test slugifying string with numbers."""
        assert slugify("Product 123") == "product-123"

    def test_slugify_leading_trailing_special(self):
        """Test slugifying with leading/trailing special chars."""
        assert slugify("!Hello World!") == "hello-world"


class TestCapitalizeWords:
    """Test suite for capitalize_words function."""

    def test_capitalize_simple(self):
        """Test capitalizing simple string."""
        assert capitalize_words("hello world") == "Hello World"

    def test_capitalize_already_capitalized(self):
        """Test capitalizing already capitalized string."""
        assert capitalize_words("Hello World") == "Hello World"

    def test_capitalize_all_caps(self):
        """Test capitalizing all caps string."""
        assert capitalize_words("HELLO WORLD") == "Hello World"


class TestExtractEmails:
    """Test suite for extract_emails function."""

    def test_extract_single_email(self):
        """Test extracting single email."""
        text = "Contact us at info@example.com"
        assert extract_emails(text) == ["info@example.com"]

    def test_extract_multiple_emails(self):
        """Test extracting multiple emails."""
        text = "Contact info@example.com or support@test.org"
        result = extract_emails(text)
        assert "info@example.com" in result
        assert "support@test.org" in result

    def test_extract_no_emails(self):
        """Test extracting from text with no emails."""
        assert extract_emails("No emails here") == []

    def test_extract_complex_emails(self):
        """Test extracting complex email formats."""
        text = "Email: user.name+tag@sub.domain.com"
        assert "user.name+tag@sub.domain.com" in extract_emails(text)


class TestMaskSensitiveData:
    """Test suite for mask_sensitive_data function."""

    def test_mask_default(self):
        """Test masking with default settings."""
        assert mask_sensitive_data("1234567890") == "******7890"

    def test_mask_custom_char(self):
        """Test masking with custom character."""
        assert mask_sensitive_data("1234567890", mask_char="#") == "######7890"

    def test_mask_custom_visible(self):
        """Test masking with custom visible chars."""
        assert mask_sensitive_data("1234567890", visible_chars=2) == "********90"

    def test_mask_short_string(self):
        """Test masking string shorter than visible chars."""
        assert mask_sensitive_data("123", visible_chars=4) == "123"


class TestFindCommonPrefix:
    """Test suite for find_common_prefix function."""

    def test_common_prefix_simple(self):
        """Test finding common prefix in simple list."""
        strings = ["flower", "flow", "flight"]
        assert find_common_prefix(strings) == "fl"

    def test_common_prefix_none(self):
        """Test when there is no common prefix."""
        strings = ["dog", "racecar", "car"]
        assert find_common_prefix(strings) == ""

    def test_common_prefix_all_same(self):
        """Test when all strings are the same."""
        strings = ["test", "test", "test"]
        assert find_common_prefix(strings) == "test"

    def test_common_prefix_empty_list(self):
        """Test with empty list."""
        assert find_common_prefix([]) == ""

    def test_common_prefix_single_string(self):
        """Test with single string."""
        assert find_common_prefix(["hello"]) == "hello"
