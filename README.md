# Week 1 - Strategic Planning and Data Exploration in Logistics

## Project Overview
This project covers the strategic planning phase of a logistics data science project. The objective is to define a realistic logistics problem, identify measurable KPIs, research public logistics data, and design an end-to-end Python analytics roadmap.

The project focuses on **e-commerce delivery performance, delay prediction, and logistics resource optimization** using the **Brazilian E-Commerce Public Dataset by Olist**.

## Business Problem
An e-commerce logistics network needs to improve delivery reliability while controlling transportation cost. The analysis is designed to identify delivery-delay patterns, understand operational drivers, predict delivery risk, segment operational zones/orders, and support route and resource allocation decisions.

## Key KPIs
- **On-Time Delivery Rate** = On-time delivered orders / delivered orders × 100
- **Average Delivery Delay** = Average(actual delivery date − estimated delivery date)
- **Freight Cost per Order** = Total freight value / delivered orders
- **Average Order-to-Delivery Time**
- **Customer Review Score / Low-Score Rate**

## Dataset
Reference dataset: **Brazilian E-Commerce Public Dataset by Olist**

Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

The dataset contains approximately 100,000 orders from 2016–2018 and includes order lifecycle, order items, seller/customer information, products, freight, reviews, payments, and geolocation data.

## Data Science Methods
### Exploratory Data Analysis
Used to identify:
- Delivery trends
- Regional performance differences
- Seller patterns
- Freight and product effects
- Distance-related patterns
- Customer experience relationships

### Predictive Modeling
Candidate methods:
- Linear Regression
- Logistic Regression
- Random Forest
- Gradient Boosting

Potential targets:
- Delivery duration
- Late vs. on-time delivery

### Clustering
K-Means can be used to segment delivery zones, sellers, or order profiles based on operational characteristics.

### Optimization
A Vehicle Routing Problem can be modeled using Google OR-Tools with constraints such as:
- Vehicle capacity
- Delivery time windows
- Route duration
- Depot start/end
- Late-delivery penalties

## Strategic Roadmap
1. Define business problem and KPIs
2. Collect public logistics data
3. Validate and understand data structure
4. Clean and integrate datasets
5. Engineer logistics features
6. Perform exploratory analysis
7. Establish KPI baseline
8. Build predictive models
9. Perform clustering/segmentation
10. Prototype route/resource optimization
11. Validate against baseline
12. Communicate findings and recommendations

## Project Files
```text
Week-1-logistics-data-intern/
├── Week_1_Logistics_Strategic_Planning_Report.docx
├── logistics_strategy.py
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Use
Install dependencies:
```bash
pip install -r requirements.txt
```

Run the strategy/demo script:
```bash
python logistics_strategy.py
```

## Important Note
This repository contains the **strategic Week 1 plan**, not claimed final model results. Actual numerical findings should only be reported after the Olist dataset is downloaded, cleaned, analyzed, and validated.

## References
- Olist Dataset: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
- World Bank Logistics Performance Index: https://www.worldbank.org/en/news/press-release/2023/04/21/world-bank-releases-logistics-performance-index-2023
- Scikit-learn Metrics: https://scikit-learn.org/stable/api/sklearn.metrics.html
- Google OR-Tools: https://developers.google.com/optimization
- Vehicle Routing: https://developers.google.com/optimization/routing
