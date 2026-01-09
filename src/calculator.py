"""Calculator Module - Provides basic arithmetic operations.

This module demonstrates how to write clean, testable code that can be
easily validated through automated CI/CD pipelines.
"""

from typing import Union

Number = Union[int, float]


class Calculator:
    """A simple calculator class demonstrating OOP principles."""

    def __init__(self):
        """Initialize the calculator with a history of operations."""
        self.history: list[str] = []

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers together.

        Args:
            a: First number
            b: Second number

        Returns:
            The sum of a and b

        Examples:
            >>> calc = Calculator()
            >>> calc.add(2, 3)
            5
        """
        result = a + b
        self._record_operation(f"{a} + {b} = {result}")
        return result

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract second number from first.

        Args:
            a: First number (minuend)
            b: Second number (subtrahend)

        Returns:
            The difference of a and b
        """
        result = a - b
        self._record_operation(f"{a} - {b} = {result}")
        return result

    def multiply(self, a: Number, b: Number) -> Number:
        """Multiply two numbers.

        Args:
            a: First number
            b: Second number

        Returns:
            The product of a and b
        """
        result = a * b
        self._record_operation(f"{a} * {b} = {result}")
        return result

    def divide(self, a: Number, b: Number) -> float:
        """Divide first number by second.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            The quotient of a divided by b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self._record_operation(f"{a} / {b} = {result}")
        return result

    def power(self, base: Number, exponent: Number) -> Number:
        """Raise base to the power of exponent.

        Args:
            base: The base number
            exponent: The exponent

        Returns:
            base raised to the power of exponent
        """
        result = base**exponent
        self._record_operation(f"{base} ^ {exponent} = {result}")
        return result

    def modulo(self, a: Number, b: Number) -> Number:
        """Calculate remainder of division.

        Args:
            a: Dividend
            b: Divisor

        Returns:
            The remainder of a divided by b

        Raises:
            ValueError: If b is zero
        """
        if b == 0:
            raise ValueError("Cannot calculate modulo with zero!")
        result = a % b
        self._record_operation(f"{a} % {b} = {result}")
        return result

    def _record_operation(self, operation: str) -> None:
        """Record an operation in history."""
        self.history.append(operation)

    def get_history(self) -> list[str]:
        """Get the history of all operations performed.

        Returns:
            List of operation strings
        """
        return self.history.copy()

    def clear_history(self) -> None:
        """Clear the operation history."""
        self.history.clear()


# Standalone functions for functional programming style
def add(a: Number, b: Number) -> Number:
    """Add two numbers."""
    return a + b


def subtract(a: Number, b: Number) -> Number:
    """Subtract b from a."""
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """Multiply two numbers."""
    return a * b


def divide(a: Number, b: Number) -> float:
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
