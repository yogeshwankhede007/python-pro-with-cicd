"""
Unit tests for the Calculator module.

These tests demonstrate:
- Testing individual methods
- Testing edge cases
- Testing exception handling
- Using pytest fixtures
"""

import pytest
from src.calculator import Calculator, add, subtract, multiply, divide


class TestCalculator:
    """Test suite for Calculator class."""

    @pytest.fixture
    def calculator(self):
        """Fixture to create a fresh Calculator instance for each test."""
        return Calculator()

    # Addition tests
    def test_add_positive_numbers(self, calculator):
        """Test adding two positive numbers."""
        assert calculator.add(2, 3) == 5

    def test_add_negative_numbers(self, calculator):
        """Test adding two negative numbers."""
        assert calculator.add(-2, -3) == -5

    def test_add_mixed_numbers(self, calculator):
        """Test adding positive and negative numbers."""
        assert calculator.add(-2, 3) == 1

    def test_add_floats(self, calculator):
        """Test adding floating point numbers."""
        result = calculator.add(2.5, 3.7)
        assert pytest.approx(result, 0.01) == 6.2

    def test_add_zero(self, calculator):
        """Test adding zero."""
        assert calculator.add(5, 0) == 5

    # Subtraction tests
    def test_subtract_positive_numbers(self, calculator):
        """Test subtracting two positive numbers."""
        assert calculator.subtract(5, 3) == 2

    def test_subtract_negative_result(self, calculator):
        """Test subtraction resulting in negative number."""
        assert calculator.subtract(3, 5) == -2

    def test_subtract_negative_numbers(self, calculator):
        """Test subtracting negative numbers."""
        assert calculator.subtract(-5, -3) == -2

    # Multiplication tests
    def test_multiply_positive_numbers(self, calculator):
        """Test multiplying two positive numbers."""
        assert calculator.multiply(4, 5) == 20

    def test_multiply_by_zero(self, calculator):
        """Test multiplication by zero."""
        assert calculator.multiply(5, 0) == 0

    def test_multiply_negative_numbers(self, calculator):
        """Test multiplying negative numbers."""
        assert calculator.multiply(-3, -4) == 12

    def test_multiply_mixed_signs(self, calculator):
        """Test multiplying numbers with different signs."""
        assert calculator.multiply(-3, 4) == -12

    # Division tests
    def test_divide_positive_numbers(self, calculator):
        """Test dividing two positive numbers."""
        assert calculator.divide(10, 2) == 5.0

    def test_divide_by_zero_raises_error(self, calculator):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculator.divide(10, 0)

    def test_divide_with_remainder(self, calculator):
        """Test division with remainder."""
        result = calculator.divide(7, 2)
        assert result == 3.5

    def test_divide_negative_numbers(self, calculator):
        """Test dividing negative numbers."""
        assert calculator.divide(-10, -2) == 5.0

    # Power tests
    def test_power_positive_exponent(self, calculator):
        """Test power with positive exponent."""
        assert calculator.power(2, 3) == 8

    def test_power_zero_exponent(self, calculator):
        """Test power with zero exponent."""
        assert calculator.power(5, 0) == 1

    def test_power_negative_exponent(self, calculator):
        """Test power with negative exponent."""
        assert calculator.power(2, -2) == 0.25

    # Modulo tests
    def test_modulo_positive_numbers(self, calculator):
        """Test modulo with positive numbers."""
        assert calculator.modulo(10, 3) == 1

    def test_modulo_by_zero_raises_error(self, calculator):
        """Test that modulo by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate modulo with zero"):
            calculator.modulo(10, 0)

    # History tests
    def test_history_recording(self, calculator):
        """Test that operations are recorded in history."""
        calculator.add(2, 3)
        calculator.multiply(4, 5)
        history = calculator.get_history()
        assert len(history) == 2
        assert "2 + 3 = 5" in history[0]
        assert "4 * 5 = 20" in history[1]

    def test_clear_history(self, calculator):
        """Test clearing operation history."""
        calculator.add(2, 3)
        calculator.clear_history()
        assert len(calculator.get_history()) == 0

    def test_history_immutability(self, calculator):
        """Test that returned history is a copy."""
        calculator.add(2, 3)
        history = calculator.get_history()
        history.append("fake operation")
        assert len(calculator.get_history()) == 1


class TestStandaloneFunctions:
    """Test suite for standalone calculator functions."""

    def test_add_function(self):
        """Test standalone add function."""
        assert add(5, 3) == 8

    def test_subtract_function(self):
        """Test standalone subtract function."""
        assert subtract(5, 3) == 2

    def test_multiply_function(self):
        """Test standalone multiply function."""
        assert multiply(5, 3) == 15

    def test_divide_function(self):
        """Test standalone divide function."""
        assert divide(6, 3) == 2.0

    def test_divide_by_zero_function(self):
        """Test standalone divide function with zero."""
        with pytest.raises(ValueError):
            divide(5, 0)


# Parametrized tests for comprehensive coverage
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 1, 2),
        (0, 0, 0),
        (-1, 1, 0),
        (100, 200, 300),
        (1.5, 2.5, 4.0),
    ],
)
def test_add_parametrized(a, b, expected):
    """Parametrized test for addition."""
    calc = Calculator()
    assert calc.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 2, 3.0),
        (9, 3, 3.0),
        (10, 4, 2.5),
        (-6, 2, -3.0),
        (6, -2, -3.0),
    ],
)
def test_divide_parametrized(a, b, expected):
    """Parametrized test for division."""
    calc = Calculator()
    assert calc.divide(a, b) == expected
