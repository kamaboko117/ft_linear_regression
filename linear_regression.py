import pandas as pd
import matplotlib.pyplot as plt
from dotenv import set_key
from estimate import estimate_price

# Load data
data = pd.read_csv("data.csv")
tmpdata = data.copy()

# Normalize the km values
data['km'] = (data['km'] - data['km'].mean()) / data['km'].std()

# Define learning rate and thetas
learning_rate = 0.1
theta0 = 0
theta1 = 0

def learn():
    global theta0, theta1
    
    m = len(data)
    gradient_theta0 = (1/m) * sum([estimate_price(data['km'][i], theta0, theta1) - data['price'][i] for i in range(m)])
    gradient_theta1 = (1/m) * sum([(estimate_price(data['km'][i], theta0, theta1) - data['price'][i]) * data['km'][i] for i in range(m)])

    print(f"theta0: {theta0} -> {theta0 - learning_rate * gradient_theta0}")
    print(f"theta1: {theta1} -> {theta1 - learning_rate * gradient_theta1}")

    theta0 -= learning_rate * gradient_theta0
    theta1 -= learning_rate * gradient_theta1

for i in range(100):
    learn()

set_key(".env", "THETA0", str(theta0))
set_key(".env", "THETA1", str(theta1))

# Plot data
plt.scatter(tmpdata['km'], data['price'])
plt.plot(tmpdata['km'], theta0 + theta1 * data['km'], color='red')
plt.xlabel('km')
plt.ylabel('price')
plt.title('Price of cars depending on their mileage')
plt.show()

