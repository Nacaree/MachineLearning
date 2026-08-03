import numpy as np
import matplotlib.pyplot as plt


class BankAccount:
    def __init__(self, holder_name: str, balance: float):
        self.holder_name = str(holder_name)
        self.balance = float(balance)
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdrew: {amount}")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        print(f"--- Your transaction history ---")
        for transaction in self.transaction_history:
            print(f"{transaction}")


my_account = BankAccount("Alice", 1000.0)
my_account.deposit(500.0)
my_account.deposit(500.0)
my_account.deposit(500.0)
my_account.withdraw(200.0)
my_account.withdraw(200.0)
my_account.withdraw(2000.0)
print(f"Your Balance: {my_account.get_balance()}")
my_account.get_transaction_history()


data = np.array([55, 68, 72, 90, 85, 77, 60, 95, 88, 70])
# * Calculations
mean_val = data.mean()
median_val = np.median(data)
std_val = data.std()
min_val = data.min()
max_val = data.max()

print("")

print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"std: {std_val:.2f}")
print(f"Min: {min_val}")
print(f"Max: {max_val}\n")

# above average student scores
above_average = data[data > mean_val]
print(f"Marks above the average: {above_average}")

# histogram
plt.hist(data, bins=5, color="skyblue", edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

# Mean: Represents the average value of the dataset
# Standard Deviation: Measures the spread or dispersion of the data points around the mean
# A low standard deviation means the values are close to the mean, while a high one indicates the data is spread out over a wider range
