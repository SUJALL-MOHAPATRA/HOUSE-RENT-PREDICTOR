# Modules and Libraries
import pandas as pd
import numpy as np
from sklearn import linear_model
import warnings


warnings.filterwarnings("ignore", category=UserWarning)                                 # User warning handling

df = pd.read_excel("D:\\SPREADSHEETS\\HouseRent.xlsx", "Sheet1")                        # DataFrame

reg = linear_model.LinearRegression()                                                   # Linear regression model

x = df[['BHK', 'Size', 'Bathroom']]                                                     # Features and Target
y = df['Rent']

reg.fit(x, y)                                                                           # Training

# Welcome Message
print("\t\t\tWELCOME\n\t\tHOUSE RENT PREDICTOR")

# Specifications
while True:
    # User Inputs
    print("\nEnter these specifications")
    bhk = int(input("BHK: "))
    size = float(input("Size (in sq feet): "))
    bth = int(input("Number of bathrooms: "))

    rent = reg.predict([[bhk, size, bth]])                                              # Prediction
    print("House rent as per the specifications: ", rent[0])

    # Continue or Exit
    c = input("Enter 'y' to predict again, 'n' to exit the program: ")
    if c in ['y', 'Y', 'Yes', 'YES', 'yes']:
        continue
    elif c in ['n', 'N', 'No', 'NO', 'no']:
        break

# Closing Message
print("\t\tPREDICTOR CLOSED")

