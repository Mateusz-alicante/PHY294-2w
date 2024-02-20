import numpy as np

import itertools
import matplotlib.pyplot as plt
import matplotlib
from statistics import linear_regression

no_field = [0.23, 0.0, -0.24, -0.41, -0.6, -0.76, -0.91]

fields = {
    136.7: [(0.02, -0.08), (-0.22, -0.31), (-0.41, -0.49), (-0.59, -0.68), (-0.73, -0.82), (-0.90, -0.96)],
    325.8: [(0.03, -0.09), (-0.21, -0.33), (-0.41, -0.50), (-0.57, -0.66), (-0.73, -0.83), (-0.87, -0.96)],
    512.9: [(0.06, -0.13), (-0.19, -0.33), (-0.38, -0.51), (-0.56, -0.70), (-0.73, -0.85), (-0.88, -0.97)],
    583.4: [(0.08, -0.11), (-0.19, -0.37), (-0.40, -0.54), (-0.59, -0.67), (-0.72, -0.83), (-0.86, -0.96)],
    583.1: [(0.09, -0.14), (-0.19, -0.35), (-0.40, -0.51), (-0.56, -0.68), (-0.74, -0.83), (-0.87, -0.97)]
}

fig, ax = plt.subplots()
ax.margins(0.05)  # Optional, just adds 5% padding to the autoscaling


# For each field (current) value
averages_fields = []
averages_shifts = []
averages_std = []

all_shifts = []
all_fields = []

for key, value in fields.items():
    # For each line in the field value
    shifts = []
    fields = []
    for i, line in enumerate(value):
        # get Zeeman shift
        shift = (line[0] - line[1]) / 2

        shifts.append(shift)
        fields.append(key)

    # Mean and standard deviation for the combined field
    std_dev = np.std(shifts)
    mean = np.mean(shifts)

    # Arrray with all individual measurements
    averages_fields.append(key)
    averages_std.append(std_dev)
    averages_shifts.append(mean)

    all_shifts.extend(shifts)
    all_fields.extend(fields)

# Compute linear fit for the zeeman split values (force zero intercept):
slope, _ = linear_regression(all_fields, all_shifts, proportional=True)
x = np.linspace(min(all_fields), max(all_fields), 100)
y = x * slope


# add slioght jiggle to the x values
all_fields_jiggle = [x + np.random.normal(0, 10) for x in all_fields]

# Plot all the individual measurements
ax.errorbar(all_fields_jiggle, all_shifts, yerr=np.std(
    all_shifts), fmt='x', label='Single measurements', ms=6, zorder=0, elinewidth=0.5)

# Plot the averages for each field
ax.errorbar(averages_fields, averages_shifts,  yerr=averages_std, fmt='o',
            label='Averages', ms=8, zorder=10, elinewidth=1.5)

# Plot the linear fit
ax.plot(x, y, label='Linear fit', zorder=20)

ax.legend()

ax.set_xlabel('Magnetic field (mT)')
ax.set_ylabel('Zeeman shift (mm)')

ax.set_title('Zeeman shift for different measured fields')

plt.savefig('Results/img/zeeman_shift_scatter.png', dpi=300)


# Now plot the residuals

fig, ax = plt.subplots()
ax.margins(0.05)

# residuals for all measurements:
residuals = np.array(all_shifts) - np.array(all_fields) * slope
ax.errorbar(all_fields_jiggle, residuals, yerr=np.std(
    all_shifts), fmt='x', label='Residuals for individual measurments', ms=6, zorder=0, elinewidth=0.5)

# residuals for the averages
residuals = np.array(averages_shifts) - np.array(averages_fields) * slope
ax.errorbar(averages_fields, residuals, yerr=averages_std, fmt='o',
            label='Residuals for averages for each field value', ms=8, zorder=10, elinewidth=1.5)

# add line at y = 0
ax.axhline(0, color='black', lw=0.5)

ax.legend()
ax.set_xlabel('Magnetic field (mT)')
ax.set_ylabel('Residuals (mm)')
ax.set_title('Residuals for Zeeman shift linear fit')

plt.savefig('Results/img/zeeman_shift_residuals.png', dpi=300)
