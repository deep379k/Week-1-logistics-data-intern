# Week 1 Strategic Planning - Logistics Analysis
# This script illustrates the proposed analytical strategy.
# It is intentionally a planning/demo script rather than a finished model.

import pandas as pd
import numpy as np

# 1. Load reference data
orders = pd.read_csv("data/olist_orders_dataset.csv")
items = pd.read_csv("data/olist_order_items_dataset.csv")

print("Orders:", orders.shape)
print("Items:", items.shape)

# 2. Convert timestamps
date_cols = [
    "order_purchase_timestamp",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_cols:
    orders[col] = pd.to_datetime(orders[col], errors="coerce")

# 3. Create logistics target/features
delivered = orders[
    orders["order_delivered_customer_date"].notna()
].copy()

delivered["delivery_days"] = (
    delivered["order_delivered_customer_date"]
    - delivered["order_purchase_timestamp"]
).dt.total_seconds() / 86400

delivered["delay_days"] = (
    delivered["order_delivered_customer_date"]
    - delivered["order_estimated_delivery_date"]
).dt.total_seconds() / 86400

delivered["is_late"] = (delivered["delay_days"] > 0).astype(int)

# 4. KPI baseline
on_time_rate = (1 - delivered["is_late"].mean()) * 100
avg_delivery_days = delivered["delivery_days"].mean()
avg_delay_late = delivered.loc[
    delivered["is_late"] == 1, "delay_days"
].mean()

print(f"On-time delivery rate: {on_time_rate:.2f}%")
print(f"Average delivery time: {avg_delivery_days:.2f} days")
print(f"Average delay among late orders: {avg_delay_late:.2f} days")

# 5. Planned EDA
monthly_orders = (
    delivered.set_index("order_purchase_timestamp")
    .resample("ME")
    .size()
)

print("\nMonthly delivered orders:")
print(monthly_orders)

# 6. Planned ML workflow
# Candidate models:
# - LogisticRegression -> late/on-time classification
# - RandomForest -> non-linear classification/regression
# - GradientBoosting -> structured/tabular prediction
#
# Suggested evaluation:
# Classification -> precision, recall, F1, ROC-AUC
# Regression -> MAE, RMSE, R^2
#
# Important: Do not use post-delivery information such as actual delivery
# timestamp or final review score as features when predicting delivery risk.

# 7. Planned clustering workflow
# Suggested segmentation features:
# - average delivery days
# - late rate
# - average freight
# - order volume
# Standardize features before K-Means.

# 8. Planned optimization workflow
# Prototype a Vehicle Routing Problem with Google OR-Tools.
# Constraints may include vehicle capacity, time windows,
# route duration, depot start/end, and late-delivery penalty.

print("\nWeek 1 strategy demo complete.")
