from decimal import ROUND_HALF_UP, Decimal


def round_half_up(value: float | Decimal, places: int = 2) -> Decimal:
    """
    Round a number using "round half up" method.

    Args:
        value (float | Decimal): The number to round.
        places (int): Number of decimal places to keep (default: 2).

    Returns:
        Decimal: Rounded number.

    Example:
        round_half_up(2.345, 2) -> Decimal('2.35')
        round_half_up(-2.555, 2) -> Decimal('-2.56')
    """
    if not isinstance(value, Decimal):
        value = Decimal(str(value))

    quantize_str = f"1.{'0' * places}"  # e.g. '1.00' for 2 decimal places
    return value.quantize(Decimal(quantize_str), rounding=ROUND_HALF_UP)
