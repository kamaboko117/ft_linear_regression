from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# grab thetas from environment variables
theta0 = float(os.getenv("THETA0"))
theta1 = float(os.getenv("THETA1"))

def estimate_price(mileage):
    return theta0 + theta1 * mileage

# take user input for mileage
mileage = input("Enter mileage: ")
mileage = float(mileage)

# estimate price
price = estimate_price(mileage)
print(f"Estimated price: {price}")