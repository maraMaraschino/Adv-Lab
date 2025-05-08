import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def linear_equation(x, m, b):
    return (m*x) + b

def find_resistance(current_data, voltage_data):
    # R = V/I
    popt, pcov = curve_fit(linear_equation, current_data, voltage_data)
    resistance, intercept = popt
    resistance_sigma, intercept_sigma = np.sqrt(np.diag(pcov))
    return resistance, intercept, resistance_sigma

def plot_resistance(csv_file, B, R, Magnet=True):
    resistance_data = pd.read_csv(f'{csv_file}', skiprows=8, index_col=0)
    current = resistance_data.iloc[:,13]
    voltage = resistance_data.iloc[:,0]

    resistance, intercept, resistance_sigma = find_resistance(current, voltage)
    
    if Magnet:
        plt.scatter(current, voltage, label=f"Magnetized Data")
        plt.title(f'Resistance ({B} to {R} - Magnet)')
    else:
        plt.scatter(current, voltage,label = f"No Magnet Data" )
        plt.title(f'Resistance ({B} to {R} - No Magnet)')
        
    # Plot line of best fit
    y_fit = linear_equation(current, resistance, intercept)
    plt.plot(current, y_fit, color='red', label='Best fit line')

    plt.xlabel('Current (A)')
    plt.ylabel('Voltage')
    plt.legend(title=f'Resistance = {resistance:.3f} ohms +/- {resistance_sigma:.3f} ohms')

    plt.show()

    return resistance, resistance_sigma

def calc_rho_from_R(avg_R, avg_R_sigma):
    # State R +/- R_sigma & R
    R1 = avg_R - avg_R_sigma
    R2 = avg_R
    R3 = avg_R + avg_R_sigma

    # Dimensions of wafer
    t = 5e-6 # m
    w = 0.008 # m
    l = 0.002 # m
    a = t*w

    # Finding rho ranges
    rho1 = a * R1 / l
    rho2 = a * R2 / l
    rho3 = a * R3 / l

    rho = rho2
    rho_sigma = rho3-rho1

    return rho, rho_sigma