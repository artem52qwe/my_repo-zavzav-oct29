"""Convert a comma-separated line into finite decimal numbers."""
from decimal import Decimal, InvalidOperation


def parse_values(text):
    """Reject empty and malformed input instead of guessing values."""
    parts = text.split(",")
    if not text.strip() or any(not part.strip() for part in parts):
        raise ValueError("Empty value")
    try:
        values = [Decimal(part.strip()) for part in parts]
    except InvalidOperation as exc:
        raise ValueError("Invalid number") from exc
    if any(not value.is_finite() for value in values):
        raise ValueError("Non-finite number")
    return values
