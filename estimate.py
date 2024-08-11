from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# grab thetas from environment variables
theta0 = float(os.getenv("THETA0"))
theta1 = float(os.getenv("THETA1"))

def estimate_price(mileage, theta0, theta1):
    return theta0 + theta1 * mileage

def main(): 
    # take user input for mileage
    mileage = input("Enter mileage: ")
    mileage = float(mileage)

    # estimate price
    price = estimate_price(mileage, theta0, theta1)
    print(f"Estimated price: {price}")

if __name__ == "__main__":
    main()