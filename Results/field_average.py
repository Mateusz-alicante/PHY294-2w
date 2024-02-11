from uncertainties import ufloat
from uncertainties.umath import *


field_values = [
    [151, 146, 145, 139, 139, 138, 136, 132, 123, 118],
    [347, 345, 343, 347, 320, 324, 318, 317, 318, 317, 316, 313, 311],
    [512, 523, 521, 520, 518, 516, 513, 511, 508, 506, 504, 503],

    [532, 567, 584, 561, 564, 595, 613, 587, 608, 604, 590, 596],
    [580, 592, 624, 571, 567, 559, 548, 558, 583, 621,
        608, 614, 604, 598, 602, 531, 541, 586, 592],
]

for i, trial in enumerate(field_values):
    field_sum = 0
    for value in trial:
        field_sum += ufloat(value, 0.5)
    print("Trial", i + 1, "average:", field_sum / len(trial))
