import numpy as np

raw_data = [
    ["101", "Controllers", "1200"],
    ["102", "Mixers", "2500"],
    ["103", "Speakers", "800"],
    ["104", "Controllers", "1500"],
    ["105", "Mixers", "900"],
    ["106", "Speakers", "3000"],
    ["107", "Controllers", "950"],
    ["108", "Mixers", "1100"]
]
sales_np = np.array(raw_data)
prices = sales_np[:, 2].astype(float)
avg_price = np.mean(prices)
count_expensive = np.sum(prices > 1000)
unique_categors = np.unique(sales_np[:, 1])
total_revenue = np.sum(prices)
for cat in unique_categors:
    mask = sales_np[:, 1] == cat
    cat_prices = np.sum(prices[mask])
    percentage = (cat_prices / total_revenue) * 100

    print(f"Category: {cat}")
    print(f"Total Revenue: {cat_prices} NIS")
    print(f"Percentage from total revenue : {percentage:.2f}%")
    print("-" * 20)

import matplotlib.pyplot as plt
#emashelchasharmota
sums = [np.sum(prices[sales_np[:, 1] == c]) for c in unique_categors]
plt.figure(figsize=(8, 6))
plt.pie(sums, labels=unique_categors, autopct='%1.1f%%', startangle=140)
plt.title("Revenue Distribution by Category")
plt.show()





