from estimate import estimate_price
from dotenv import load_dotenv
import os

mileage = input("Enter mileage: ")
mileage = float(mileage)
price = input("Enter price: ")
price = float(price)
theta0 = float(os.getenv("THETA0"))
theta1 = float(os.getenv("THETA1"))

estimated_price = estimate_price(mileage, theta0, theta1)

print(f"Estimated price: {estimated_price}")
print(f"Actual price: {price}")
print(f"Error: {estimated_price - price}")
print(f"Error percentage: {abs(estimated_price - price) / price * 100}%")

