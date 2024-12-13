#Python code
import numpy as np
from scipy.optimize import curve_fit
# Example data
analog_readings = [1856, 1475, 1317, 1226, 1153]
weights = [1.0, 2.0, 3.0, 4.0, 5.0]
a_initial = 0
b_initial = 0
# Power-law model
def power_law(x, a, b):
 return a * (x ** b)
# Fit the curve
params, _ = curve_fit(power_law, analog_readings, weights)
a, b = params
print(f"Initial values: a = {a_initial}, b = {b_initial}")
print(f"Fitted values: a = {a}, b = {b}")