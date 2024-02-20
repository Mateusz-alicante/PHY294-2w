import numpy as np

no_field = [0.23, 0.0, -0.24, -0.41, -0.6, -0.76, -0.91]

sep = []

for i in range(1, 6):
    sep.append(np.abs(no_field[i] - no_field[i - 1]))


for sep_item in sep:
    print(f"{sep_item:.2f}")

# print the line separation with 2 decimal places
print(f"Average line separation: {np.mean(sep):.2f} \pm {np.std(sep):.2f}")
