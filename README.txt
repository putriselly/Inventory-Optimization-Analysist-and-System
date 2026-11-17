# Inventory Optimization System

A Python-based inventory management and optimization system designed to help retail businesses monitor stock levels, analyze sales performance, and make better restocking decisions.

## Project Overview

This project focuses on analyzing retail sales and product data to support inventory management decisions. It uses historical sales information to evaluate product performance, monitor stock availability, and identify products that require restocking.

The project also provides an interactive dashboard built with Streamlit to make the analysis easier to understand.

## Features

- **Sales Data Analysis** – Examine sales data and identify patterns and trends.
- **Product Performance Analysis** – Identify the best-selling and lowest-selling products.
- **Transaction Trend Analysis** – Analyze transaction activity by date and hour.
- **Inventory Monitoring** – Compare current stock levels with Reorder Points (ROP).
- **Restock Recommendations** – Identify products that need restocking.
- **Order Quantity Estimation** – Calculate the quantity of products that should be reordered.
- **Interactive Dashboard** – Visualize analysis results through Streamlit.

## Technologies Used

- Python
- Pandas
- Streamlit
- Matplotlib

---

# Data Analysis Results

## A. Sales Data Analysis

### 1. Data Quality Inspection

Several observations were identified during the data inspection and cleaning process:

1. The `Tanggal_Waktu` column needed to be converted into datetime format to support date and time analysis.
2. The `Harga_Satuan` column needed to be converted into float format for numerical calculations.
3. The `Total_Harga` column also needed to be converted into float format.
4. The `ID_Produk` column contained 40 duplicate values. However, these duplicates were not necessarily errors because the same product could appear in multiple transactions.
5. The `Jumlah_Terjual` column contained values of 5 and 6, each appearing only once, while the median was 2. These values were considered unusual but could still represent valid purchases.
6. The mean of `Harga_Satuan` was approximately Rp3,000 or 16% higher than its median. This could indicate the influence of relatively high-priced products.
7. The minimum and maximum values of `Harga_Satuan` were Rp18,000 and Rp55,000, respectively. This variation could be explained by differences in product prices.
8. The Coefficient of Variation (CV) of `Harga_Satuan` was approximately 62.1%, indicating considerable price variation.
9. The CV of `Total_Harga` was approximately 56.4%, potentially influenced by differences in unit prices and quantities purchased.

These findings were not sufficient to conclude that the data contained recording errors. Therefore, suspicious values were retained pending further verification.

### 2. Sales Trend Analysis

Sales trends were analyzed to identify transaction patterns based on date and time.

Key findings:

- **Busiest Transaction Date:** November 3, 2025, with 3 transactions.
- **Busiest Transaction Hour:** Around 18:00 (6 PM), with 5 transactions.

These findings suggest that early-month promotions and improved service availability during the evening could be considered as potential sales strategies.

### 3. Conclusion and Recommendations

The sales data inspection did not provide sufficient evidence to justify deleting or correcting the observed values.

Several values showed considerable variation, particularly in unit prices and total transaction amounts. However, these variations could be explained by differences in products and purchase quantities.

Recommendations:

- Consider running promotional campaigns during periods with higher transaction activity.
- Ensure sufficient staff availability during evening hours.
- Maintain product and transaction records to support future data verification.
- Continue monitoring sales trends to identify more consistent purchasing patterns.

## B. Product Data Analysis

### 1. Data Quality Inspection

Several observations were identified during the product data inspection:

1. The `Harga_Modal` column needed to be converted into float format for numerical calculations.
2. The CV of `Harga_Modal` was approximately 78%, indicating considerable variation in product costs.
3. The CV of `Stok_Minimum` was approximately 50%, indicating differences in minimum stock requirements across products.

These variations were considered potentially reasonable because products can have different costs and inventory requirements.

### 2. Product Sales Performance

Product sales were analyzed to identify the best-selling and lowest-selling products.

Key findings:

| Product | Total Units Sold |
|---|---:|
| Roti Cokelat | 24 |
| Kopi Bubuk 250g | 4 |

- **Best-Selling Product:** Roti Cokelat, with 24 units sold.
- **Lowest-Selling Product:** Kopi Bubuk 250g, with 4 units sold.

### 3. Conclusion and Recommendations

The analysis showed that product costs and minimum stock requirements varied across products. These differences were not necessarily errors, as each product could have different characteristics and inventory needs.

Roti Cokelat recorded the highest sales, while Kopi Bubuk 250g recorded the lowest sales.

Based on these findings, the following recommendations were identified:

1. **Increase Roti Cokelat Inventory:** Consider increasing its stock availability to support customer demand and reduce the risk of stockouts.
2. **Consider Similar Product Variations:** Introduce other bread variations, such as strawberry or cheese, to attract more customers.
3. **Evaluate Kopi Bubuk 250g Inventory:** Review its stock levels to avoid unnecessary inventory accumulation, without immediately discontinuing the product.
4. **Monitor Product Sales Regularly:** Track sales performance to ensure inventory decisions are based on consistent demand patterns.

---

## Project Objective

The main objective of this project is to help retail businesses identify products that need restocking before they run out of stock.

By combining historical sales analysis, inventory monitoring, and Reorder Point (ROP) calculations, the system provides information to support more effective inventory management decisions.
