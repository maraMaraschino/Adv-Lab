import pandas as pd
import numpy as np

co60 = pd.read_csv("CalCO60 01GA.csv", skiprows = 21, usecols = [0, 2])
co57 = pd.read_csv("", skiprows = 21, usecols = [0,2])
na22 = pd.read_csv("", skiprows = 21, usecols = [0,2])
cd109 = pd.read_csv("", skiprows = 21, usecols = [0,2])
mn54 = pd.read_csv("", skiprows = 21, usecols = [0,2])
ba133 = pd.read_csv("", skiprows = 21, usecols = [0,2])
unknownSource = pd.read_csv("", skiprows = 21, usecols = [0,2])

# Creating gaussian functions
def gaussian(x, amplitude, mu, sigma, y_offset):
    return amplitude * np.exp(-((x - mu)**2) / (2 * sigma**2)) + y_offset

# Second gaussian
def gaussian2(x, amp1, amp2, mu1, mu2, sigma1, sigma2, y_offset):
    return (amp1 * np.exp(-((x - mu1) ** 2) / (2 * sigma1 ** 2)
                         + amp2 * np.exp(-((x - mu2) ** 2) / (2 * sigma2 ** 2)) + y_offset))


