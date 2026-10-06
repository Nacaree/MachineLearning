import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# ============================================================
# 1. Load Dataset
# ============================================================

columns = [
    "mpg",
    "cylinders",
    "displacement",
    "horsepower",
    "weight",
    "acceleration",
    "model_year",
    "origin",
    "car_name"
]

df = pd.read_csv(
    "auto-mpg.data",
    sep=r"\s+",
    names=columns,
    na_values="?",
    quotechar='"'
)

print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nSummary Statistics:")
print(df.describe())


# ============================================================
# 2. Data Preprocessing
# ============================================================

# 2.1 Remove missing horsepower values
df = df.dropna(subset=["horsepower"]).copy()

print("\nDataset shape after removing missing values:")
print(df.shape)

print("\nMissing values after cleaning:")
print(df.isnull().sum())


# 2.2 Check for outliers using the IQR method

columns_to_check = [
    "mpg",
    "displacement",
    "horsepower",
    "weight",
    "acceleration"
]

print("\nOutlier Check:")

for column in columns_to_check:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(f"{column}: {len(outliers)} outliers")


# Inspect flagged outliers

def show_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_bound) |
        (df[column] > upper_bound)
    ]

    print(f"\n{column} outliers:")
    print(outliers[[column, "car_name"]])


show_outliers("horsepower")
show_outliers("acceleration")


# ============================================================
# 3. Feature Engineering
# ============================================================

# Remove car name because it is not used for prediction
df = df.drop(columns=["car_name"])

# Convert origin into categorical dummy variables
df = pd.get_dummies(
    df,
    columns=["origin"],
    prefix="origin",
    drop_first=True,
    dtype=int
)

print("\nDataset after feature engineering:")
print(df.head())


# ============================================================
# 4. Data Exploration
# ============================================================

# 4.1 MPG Distribution

plt.hist(
    df["mpg"],
    bins=15,
    edgecolor="black"
)

plt.title("Distribution of Fuel Efficiency (MPG)")
plt.xlabel("Miles Per Gallon (MPG)")
plt.ylabel("Number of Cars")
plt.show()


# 4.2 Correlation Analysis

correlation_matrix = df.corr()

print("\nCorrelation with MPG:")
print(
    correlation_matrix["mpg"]
    .sort_values(ascending=False)
)


# 4.3 Feature Relationships - Vehicle Weight vs MPG

plt.scatter(
    df["weight"],
    df["mpg"]
)

plt.title("Vehicle Weight vs Fuel Efficiency")
plt.xlabel("Weight")
plt.ylabel("Miles Per Gallon (MPG)")
plt.show()


# 4.3 Feature Relationships - Horsepower vs MPG

plt.scatter(
    df["horsepower"],
    df["mpg"]
)

plt.title("Horsepower vs Fuel Efficiency")
plt.xlabel("Horsepower")
plt.ylabel("Miles Per Gallon (MPG)")
plt.show()


# ============================================================
# 5. Model Selection and Building
# ============================================================

# 5.1 Define features and target

X = df.drop(columns=["mpg"])
y = df["mpg"]


# 5.2 Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining features:", X_train.shape)
print("Testing features:", X_test.shape)

print("Training target:", y_train.shape)
print("Testing target:", y_test.shape)


# 5.3 Model Training

model = LinearRegression()

model.fit(
    X_train,
    y_train
)

print("\nModel training completed.")


# 5.4 Fuel Efficiency Prediction

y_pred = model.predict(X_test)

print("\nFirst 10 predicted MPG values:")
print(y_pred[:10])


# Compare actual and predicted MPG

results = pd.DataFrame({
    "Actual MPG": y_test.values,
    "Predicted MPG": y_pred
})

print("\nFirst 10 Actual vs Predicted MPG values:")
print(results.head(10))


# ============================================================
# 6. Model Evaluation
# ============================================================

# 6.1 Calculate MSE, RMSE and R²

mse = mean_squared_error(
    y_test,
    y_pred
)

rmse = np.sqrt(mse)

r2 = r2_score(
    y_test,
    y_pred
)

print("\nModel Evaluation:")
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)


# 6.2 Actual vs Predicted MPG

plt.scatter(
    y_test,
    y_pred
)

plt.xlabel("Actual MPG")
plt.ylabel("Predicted MPG")
plt.title("Actual vs Predicted Fuel Efficiency")

# Perfect prediction reference line
min_value = min(
    y_test.min(),
    y_pred.min()
)

max_value = max(
    y_test.max(),
    y_pred.max()
)

plt.plot(
    [min_value, max_value],
    [min_value, max_value],
    linestyle="--"
)

plt.show()
