def check_number_status(n: float) -> str:
    if not isinstance(n, (int, float)):
        raise ValueError("Input must be a numeric value (int or float).")

    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero".
