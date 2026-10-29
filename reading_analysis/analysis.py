"""Calculate a statistic without performing input or output."""


def analyze(values):
    """Return range for a nonempty decimal sequence."""
    if not values:
        raise ValueError("No values")
    return max(values) - min(values)
