import numpy as np

def dice_expected_value(n=10000):
    """
    Estimates the expected value of a fair six-sided die
    using Monte Carlo simulation.

    The theoretical value is 3.5.
    """
    total = 0
    for _ in range(n):
        total += np.random.randint(1, 7)
        
    expected_value = total/n
    print(f"The expected value is {expected_value} ")

if __name__ == "__main__":
    dice_expected_value()
