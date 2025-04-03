import matplotlib.pyplot as plt
import numpy as np

# Data
exposure_dosage = np.array([1.075, 1.29, 1.505, 1.72, 2.15, 2.58, 3.01, 3.44])
thickness = np.array([0.11, 0.18, 0.19, 0.22, 0.33, 0.36, 0.54, 0.62])

# Fit a linear regression model to the log-transformed x values
log_exposure_dosage = np.log(exposure_dosage)
coefficients = np.polyfit(log_exposure_dosage, thickness, 1)
trendline = np.poly1d(coefficients)

# Generate x values for the trendline
x_trend = np.linspace(min(log_exposure_dosage), max(log_exposure_dosage), 100)
y_trend = trendline(x_trend)

# Compute trendline equation
slope, intercept = coefficients
equation = f'Thickness = {slope:.4f} * log(Exposure) + {intercept:.4f}'

# Plot data points
plt.figure(figsize=(8, 5))
plt.scatter(exposure_dosage, thickness, color='b', label='Data Points')

# Plot trendline
plt.plot(np.exp(x_trend), y_trend, linestyle='--', color='r', label=equation)

# Set log scale for x-axis
plt.xscale('log')

# Labels and title
plt.xlabel('Exposure Dosage (mJ/s) [Log Scale]')
plt.ylabel('Thickness (mm)')
plt.title('Thickness vs Exposure Dosage')

# Show legend with equation
plt.legend()

# Show grid
plt.grid(True, which="both", linestyle="--", linewidth=0.5)

# Show plot
plt.show()