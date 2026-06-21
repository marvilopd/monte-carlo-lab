import numpy as np

def coin_toss(n=1000):
    heads = 0

    for _ in range(n):
        toss = np.random.randint(2)
        if toss == 1:
            heads += 1
    
    probability = heads / n

    print(f"In {n} coin tosses, the coin landed {heads} times on heads")
    print(f"The probabilty for heads was {probability:4f}")

if __name__ == "__main__":
    coin_toss()
