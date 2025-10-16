import pandas as pd
import os

def safe_append_to_csv(filepath, data_dict):
    try:
        if not isinstance(data_dict, dict):
            raise ValueError("Data must be a dictionary.")

        df_new = pd.DataFrame([data_dict])

        if not os.path.exists(filepath):
            df_new.to_csv(filepath, mode='w', header=True, index=False)
            print(f"File '{filepath}' created with success.")
        else:
            df_new.to_csv(filepath, mode='a', header=False, index=False)
            print(f"Data successfully added to '{filepath}'.")
    except PermissionError:
        print(f"Error: Permission denied for file '{filepath}'.")
    except IOError as e:
        print(f"Error accessing the file '{filepath}' : {e}")
    except Exception as e:
        print(f"Error: unexpected error reading '{filepath}' : {e}")

def safe_read_csv(filepath):
    if not os.path.exists(filepath):
        print(f"Error: file '{filepath}' not found.")
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

# Dataset standardization
mu = sum(data['km']) / len(data['km'])
sigma = (sum((data['km'] - mu) **2) / len(data['km']))**0.5
data['scaled'] = (data['km'] - mu) / sigma

# Theta initilization
theta0 = 0
theta1 = 0

def model(input):
    output = theta0 + input * theta1
    return output

def error(predictions):
    err = predictions - data['price']
    return err

def gradient_descent(error0, error1, learning_rate, theta0, theta1):
    theta0 = theta0 - learning_rate * error0
    theta1 = theta1 - learning_rate * error1
    return theta0, theta1

i = 0

while i < 1000:
    learning_rate = 0.07
    predictions = model(data['scaled'])
    error0 = sum(error(predictions)) / len(error(predictions))
    error1 = sum(error(predictions) * data['scaled'] / len(error(predictions)))
    theta0, theta1 = gradient_descent(error0, error1, learning_rate, theta0, theta1)
    if i % 100 == 0:
        print(f"MAE for iteration {i}: {error0}")
    i += 1
    if i == 500 | i == 250:
        learning_rate /= 10

safe_append_to_csv('model.csv', {'col1': theta0, 'col2': theta1})