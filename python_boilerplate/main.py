def add(a: int, b: int) -> int:
    """
    Add two integers.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        The sum of a and b.
    """
    return a + b


def calculate_average(values: list[float]) -> float:
    """
    Calculate the arithmetic mean of a list of numbers.

    This function computes the average by summing all values
    and dividing by the number of elements.

    Args:
        values: A non-empty list of floating-point numbers.

    Returns:
        The arithmetic mean of the input values.

    Raises:
        ValueError: If the input list is empty.

    Examples:
        >>> calculate_average([1.0, 2.0, 3.0])
        2.0
    """
    if not values:
        raise ValueError("values must not be empty")

    return sum(values) / len(values)
