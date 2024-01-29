from uncertainties import ufloat
from uncertainties.umath import *


field_values = [595, 604, 600, 588, 601]

values_with_uncertainties = [ufloat(value, 0.5) for value in field_values]

field_average = sum(values_with_uncertainties)/len(values_with_uncertainties)

print("Field average: ", field_average)
