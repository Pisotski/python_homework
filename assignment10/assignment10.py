# %% Line Plot
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [1000, 1200, 1500, 1700, 1600, 1800]
plt.plot(months, revenue, marker="o", linestyle="-", color="blue")
plt.title("Monthly Revenue")
plt.xlabel("Months")
plt.ylabel("Revenue ($)")
plt.show()

# %%
# Bar Plot
categories = ["Region A", "Region B"]
sales = [500, 700]
plt.bar(categories, sales, color=["green", "orange"])
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales ($)")
plt.show()

# %%
# Histogram
random_data = np.random.randn(1000)
plt.hist(random_data, bins=30, color="purple", alpha=0.7)
plt.title("Random Data Distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# %%
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [1000, 1200, 1500, 1700, 1600, 1800]

# Customized Line Plot
plt.plot(months, revenue, marker="o", linestyle="--", color="red", linewidth=2)
plt.title("Monthly Revenue", fontsize=14, fontweight="bold")
plt.xlabel("Months", fontsize=12)
plt.ylabel("Revenue ($)", fontsize=12)
plt.grid(color="gray", linestyle="--", linewidth=0.5)
plt.legend(["Revenue"], loc="upper left")
plt.show()

# Customized Bar Plot
plt.bar(categories, sales, color=["skyblue", "salmon"], width=0.5, edgecolor="black")
plt.title("Sales by Region", fontsize=14, fontweight="bold")
plt.xlabel("Region", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)
plt.grid(axis="y", color="gray", linestyle="--", linewidth=0.5)
plt.show()
# %%
# Load Titanic dataset: This dataset is
titanic = sns.load_dataset("titanic")

# Heat map of correlations
plt.figure(figsize=(10, 6))
correlation_matrix = titanic.corr(numeric_only=True)
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Pair Plot
sns.pairplot(
    titanic, vars=["age", "fare", "adult_male"], hue="survived", palette="Set2"
)
plt.title("Pair Plot of Age, Fare, and Survival")
plt.show()

# %%
categories = ["Region A", "Region B"]
sales = [500, 700]
random_data = np.random.randn(1000)

# Subplot Example
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Left plot: Bar Plot
axes[0].bar(categories, sales, color=["skyblue", "salmon"])
axes[0].set_title("Sales by Region")
axes[0].set_xlabel("Region")
axes[0].set_ylabel("Sales ($)")

# Right plot: Histogram
axes[1].hist(random_data, bins=30, color="purple")
axes[1].set_title("Random Data Distribution")
axes[1].set_xlabel("Value")
axes[1].set_ylabel("Frequency")

plt.tight_layout()  # Adjust layout for better spacing
plt.show()

# Using a Custom Color Palette in Seaborn
sns.set_palette("muted")
sns.barplot(x=categories, y=sales)
plt.title("Sales by Region with Custom Palette")
plt.show()


# %%
