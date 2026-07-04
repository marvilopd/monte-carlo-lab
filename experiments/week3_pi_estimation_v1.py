import random

inside = 0
points = 100000

for _ in range(points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x*x + y*y <= 1:
        inside += 1

pi_estimate = 4 * inside / points

print("Pi ≈", pi_estimate)
