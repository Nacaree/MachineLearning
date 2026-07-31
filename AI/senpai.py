import numpy as np


class Car:
    def __init__(self, brand, model, year):
        # *  Initialize attributes (constructor)
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}")


# * Instantiate object from class
car1 = Car("Astin Martin", "Vantage", "2025")
car1.display_info()

# * Create numpy array
data = np.array([17, 20-23, 24, 5, 67])
# * Calculations
mean_val = data.mean()
std_val = data.std()
min_val = data.min()
max_val = data.max()

print(f"Mean: {mean_val}")
print(f"std: {std_val:.2f}")
print(f"Min: {min_val}")
print(f"Max: {max_val}")
