import numpy as np

def dice_expected_value(n=10000):
    total = 0
    for _ in range(n):
        total += np.random.randint(1, 7)
        
    expected_value = total/n
    print(f"The expected value is {expected_value} ")

if __name__ == "__main__":
    dice_expected_value()
