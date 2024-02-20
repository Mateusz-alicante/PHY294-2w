import numpy as np

no_field = [0.23, 0.0, -0.24, -0.41, -0.6, -0.76, -0.91]

fields = {
    '4A': [(0.02, -0.08), (-0.22, -0.31), (-0.41, -0.49), (-0.59, -0.68), (-0.73, -0.82), (-0.90, -0.96)],
    '8A': [(0.03, -0.09), (-0.21, -0.33), (-0.41, -0.50), (-0.57, -0.66), (-0.73, -0.83), (-0.87, -0.96)],
    '12A': [(0.06, -0.13), (-0.19, -0.33), (-0.38, -0.51), (-0.56, -0.70), (-0.73, -0.85), (-0.88, -0.97)],
    '14A': [(0.08, -0.11), (-0.19, -0.37), (-0.40, -0.54), (-0.59, -0.67), (-0.72, -0.83), (-0.86, -0.96)],
    '16A': [(0.09, -0.14), (-0.19, -0.35), (-0.40, -0.51), (-0.56, -0.68), (-0.74, -0.83), (-0.87, -0.97)]
}

# For each field (current) value
for key, value in fields.items():
    # For each line in the field value
    zeeman_shifts = []
    for i, line in enumerate(value):
        # get Zeeman shift
        zeeman_shifts.append((line[0] - line[1]) / 2)

    # Print the average and standard deviation
    std_dev = np.std(zeeman_shifts)
    mean = np.mean(zeeman_shifts)

    # report average with 3 sig figs and standard deviation with 2
    print(f"{key} average: {mean:.3f} \pm {std_dev:.2f}")
