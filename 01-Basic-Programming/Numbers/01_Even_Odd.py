def is_even(n:int) -> bool:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    # "Even" if n%2==0 else "Odd"   -  Slightly Slower
    return (n&1)==0  # Extremely Fast (CPU level)

