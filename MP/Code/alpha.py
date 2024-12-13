#Python code
import numpy as np
from scipy.optimize import curve_fit
# Example data
analog_readings = [1856, 1153]
weights = [1.0, 5.0]
# Power-law model
def power_law(x, a, b):
 return a * (x ** b)
# Fit the curve
params, _ = curve_fit(power_law, analog_readings, weights)
a, b = params
print(f"a = {a}, b = {b}")