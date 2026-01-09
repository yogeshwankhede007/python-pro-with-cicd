"""
String Utilities Module - Common string manipulation functions.

This module provides utility functions for string operations,
demonstrating how to write reusable, well-tested utility code.
"""

import re


def reverse_string(text: str) -> str:
    """
    Reverse a string.

    Args:
        text: The string to reverse

    Returns:
        The reversed string

    Examples:
        >>> reverse_string("hello")
        'olleh'
    """
    return text[::-1]


def is_palindrome(
    text: str, ignore_case: bool = True, ignore_spaces: bool = True
) -> bool:
    """
    Check if a string is a palindrome.

    Args:
        text: The string to check
        ignore_case: Whether to ignore case when checking
        ignore_spaces: Whether to ignore spaces when checking

    Returns:
        True if the string is a palindrome, False otherwise

    Examples:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("A man a plan a canal Panama")
        True
    """
    processed = text
    if ignore_spaces:
        processed = processed.replace(" ", "")
    if ignore_case:
        processed = processed.lower()
    return processed == processed[::-1]


def count_words(text: str) -> int:
    """
    Count the number of words in a string.

    Args:
        text: The string to count words in

    Returns:
        The number of words

    Examples:
        >>> count_words("Hello world")
        2
    """
    if not text or not text.strip():
        return 0
    return len(text.split())


def truncate(text: str, max_length: int, suffix: str = "...") -> str:
    """
    Truncate a string to a maximum length.

    Args:
        text: The string to truncate
        max_length: Maximum length of the result (including suffix)
        suffix: The suffix to add when truncating

    Returns:
        The truncated string

    Raises:
        ValueError: If max_length is less than the length of suffix

    Examples:
        >>> truncate("Hello World", 8)
        'Hello...'
    """
    if max_length < len(suffix):
        raise ValueError(f"max_length must be at least {len(suffix)}")

    if len(text) <= max_length:
        return text

    return text[: max_length - len(suffix)] + suffix


def slugify(text: str) -> str:
    """
    Convert a string to a URL-friendly slug.

    Args:
        text: The string to slugify

    Returns:
        A URL-friendly slug

    Examples:
        >>> slugify("Hello World!")
        'hello-world'
    """
    # Convert to lowercase
    slug = text.lower()
    # Replace spaces with hyphens
    slug = slug.replace(" ", "-")
    # Remove non-alphanumeric characters (except hyphens)
    slug = re.sub(r"[^a-z0-9-]", "", slug)
    # Remove multiple consecutive hyphens
    slug = re.sub(r"-+", "-", slug)
    # Remove leading and trailing hyphens
    slug = slug.strip("-")
    return slug


def capitalize_words(text: str) -> str:
    """
    Capitalize the first letter of each word.

    Args:
        text: The string to capitalize

    Returns:
        The string with each word capitalized

    Examples:
        >>> capitalize_words("hello world")
        'Hello World'
    """
    return text.title()


def extract_emails(text: str) -> list[str]:
    """
    Extract all email addresses from a string.

    Args:
        text: The string to search for emails

    Returns:
        A list of email addresses found

    Examples:
        >>> extract_emails("Contact us at info@example.com or support@test.org")
        ['info@example.com', 'support@test.org']
    """
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(email_pattern, text)


def mask_sensitive_data(text: str, mask_char: str = "*", visible_chars: int = 4) -> str:
    """
    Mask sensitive data, showing only the last few characters.

    Args:
        text: The sensitive string to mask
        mask_char: The character to use for masking
        visible_chars: Number of characters to leave visible at the end

    Returns:
        The masked string

    Examples:
        >>> mask_sensitive_data("1234567890")
        '******7890'
    """
    if len(text) <= visible_chars:
        return text
    masked_length = len(text) - visible_chars
    return mask_char * masked_length + text[-visible_chars:]


def find_common_prefix(strings: list[str]) -> str:
    """
    Find the longest common prefix among a list of strings.

    Args:
        strings: List of strings to find common prefix

    Returns:
        The longest common prefix, or empty string if none

    Examples:
        >>> find_common_prefix(["flower", "flow", "flight"])
        'fl'
    """
    if not strings:
        return ""

    prefix = strings[0]
    for string in strings[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
