"""Integrate parsing and analysis through explicit parameters."""
import sys

from analysis import analyze
from parser import parse_values


def calculate(text):
    """Pass parsed values to the calculation module."""
    return analyze(parse_values(text))


if __name__ == "__main__":
    try:
        print(calculate(sys.argv[1] if len(sys.argv) > 1 else "2,4,6"))
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
