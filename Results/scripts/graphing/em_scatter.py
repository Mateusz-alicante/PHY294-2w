import numpy as np
from uncertainties import ufloat
from uncertainties.umath import *
from statistics import linear_regression
import matplotlib.pyplot as plt

fields = {
    136.7: [(0.02, -0.08), (-0.22, -0.31), (-0.41, -0.49), (-0.59, -0.68), (-0.73, -0.82), (-0.90, -0.96)],
    325.8: [(0.03, -0.09), (-0.21, -0.33), (-0.41, -0.50), (-0.57, -0.66), (-0.73, -0.83), (-0.87, -0.96)],
    512.9: [(0.06, -0.13), (-0.19, -0.33), (-0.38, -0.51), (-0.56, -0.70), (-0.73, -0.85), (-0.88, -0.97)],
    583.4: [(0.08, -0.11), (-0.19, -0.37), (-0.40, -0.54), (-0.59, -0.67), (-0.72, -0.83), (-0.86, -0.96)],
    583.1: [(0.09, -0.14), (-0.19, -0.35), (-0.40, -0.51), (-0.56, -0.68), (-0.74, -0.83), (-0.87, -0.97)]
}

# Define constants

D_A = ufloat(0.20, 0.03)
D = 4.04 * 10**-3
N = 1.4567
L = 643.8 * 10**-9
c = 3 * 10**8


# compute the zeeman shift for each value

all_shifts = []
all_fields = []

for key, value in fields.items():
    # For each line in the field value
    shifts = []
    fields = []
    for i, line in enumerate(value):
        # get Zeeman shift
        shift = (line[0] - line[1]) / 2 * 10**-3

        shifts.append(shift)
        fields.append(key)

    # Mean and standard deviation for the combined field
    std_dev = np.std(shifts)

    all_shifts.extend([ufloat(shift, std_dev) for shift in shifts])
    all_fields.extend(fields)

# construct y values

y = [4 * np.pi * c * D_A * 2 * D *
     np.sqrt(N ** 2 - 1) / (2 * shift * L ** 2) for shift in all_shifts]


# fit linear relationship
slope, _ = linear_regression(
    all_fields, [u.nominal_value for u in y], proportional=True)
x = np.linspace(min(all_fields), max(all_fields), 100)
y_fit = x * slope


# add slight jiggle to the x values
all_fields_jiggle = [x + np.random.normal(0, 10) for x in all_fields]

# Plot all the individual measurements
fig, ax = plt.subplots()
ax.margins(0.05)  # Optional, just adds 5% padding to the autoscaling

ax.errorbar(all_fields_jiggle, [u.nominal_value for u in y], yerr=[
            u.std_dev for u in y], fmt='x', label='Single measurements', ms=6, zorder=0, elinewidth=0.5)


# Plot the linear fit
ax.plot(x, y_fit, label='Linear fit', zorder=20)

ax.legend()

ax.set_xlabel('Magnetic field (mT)')
ax.set_ylabel('RHS constant (C*(Kg * T)^-1)')

ax.set_title('Zeeman shift for different measured fields')

plt.savefig('Results/img/em_scatter.png', dpi=300)
