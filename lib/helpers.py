from datetime import datetime

def parse_date(date_str):
    """Convert a date string to a date object."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format.")

def print_header(title):
    print("\n" + "=" * 40)
    print(f"{title.upper()}")
    print("=" * 40)