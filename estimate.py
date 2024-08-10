theta0 = 0
theta1 = 0

def estimate_price(mileage):
    return theta0 + theta1 * mileage

# take user input for mileage
mileage = input("Enter mileage: ")
mileage = float(mileage)

# estimate price
price = estimate_price(mileage)
print(f"Estimated price: {price}")