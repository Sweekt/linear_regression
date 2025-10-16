import pandas as pd
import matplotlib.pyplot as plt
import os

def safe_read_csv(filepath):
    if not os.path.exists(filepath):
        print(f"Error : file '{filepath}' not found.")
        return None
    try:
        df = pd.read_csv(filepath)
        print(f"File '{filepath}' loaded with success.")
        return df
    except pd.errors.EmptyDataError:
        print(f"Error: file '{filepath}' empty.")
    except pd.errors.ParserError:
        print(f"Error: file '{filepath}' includes bad data.")
    except Exception as e:
        print(f"Error: unexpected error reading '{filepath}' : {e}")
    return None

# Reading the CSV files :
data = safe_read_csv('data.csv')
theta = safe_read_csv('model.csv')

# Dataset standardization
mu = sum(data['km']) / len(data['km'])
sigma = (sum((data['km'] - mu) **2) / len(data['km']))**0.5

# Creating the linear plot
data['approx'] = theta['theta0'].iloc[-1] + ((data['km'] - mu) / sigma) * theta['theta1'].iloc[-1]

# Plotting the data
plt.scatter(data['km'], data['price'], color="green")
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.xlabel('Mileage')
plt.ylabel('Price')

plt.plot(data['km'], data['approx'], color="red")

plt.show()

while True:
    try:
        target = int(input('Enter the target mileage: '))
        if target > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input: please enter a positive number.")
print(target)
output = theta['theta0'].iloc[-1] + ((target - mu) / sigma) * theta['theta1'].iloc[-1]
if output < 0:
    print(f'Your car is worth nothing.')
else:
    print(f'Your car can be saled for {output} dollars.')