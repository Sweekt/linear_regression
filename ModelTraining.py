import pandas as pd

# Reading the dataset
data = pd.read_csv('data.csv')

# Dataset standardization
mu = sum(data['km']) / len(data['km'])
sigma = (sum((data['km'] - mu) **2) / len(data['km']))**0.5
data['scaled'] = (data['km'] - mu) / sigma

# Theta initilization
theta0 = 0
theta1 = 0

def model(input):
    output = theta0 + input * theta1 # output = theta0 * input + theta1
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
    predictions = model(data['scaled'])
    error0 = sum(error(predictions)) / len(error(predictions))
    print(error0)
    error1 = sum(error(predictions) * data['scaled'] / len(error(predictions)))
    theta0, theta1 = gradient_descent(error0, error1, 0.07, theta0, theta1)
    print(theta0, theta1)
    i += 1

newline = pd.DataFrame([{'col1': theta0, 'col2': theta1}])
newline.to_csv('model.csv', mode='a', header=False, index=False)