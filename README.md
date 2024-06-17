# Athletic Sales Analysis

## Overview
This project analyzes athletic sales data from 2020 and 2021. The data includes details such as region, state, city, retailer, product, units sold, and total sales. The analysis includes combining data from both years, checking for null values, converting date formats, grouping and pivoting data, and resampling data for weekly and daily sales trends.

## Data Files
The data files are located in the `Resources` directory:
- `athletic_sales_2020.csv`
- `athletic_sales_2021.csv`

## Analysis Steps
1. **Load Data**: Read CSV files into Pandas DataFrames.
2. **Data Inspection**: Display first few rows, check data types, and check for null values.
3. **Combine Data**: Concatenate DataFrames for 2020 and 2021, reset index, and convert date formats.
4. **Grouping and Aggregation**:
   - Group by region, state, and city to sum units sold and total sales.
   - Create pivot tables for units sold and total sales.
5. **Top Results**:
   - Display top 5 regions, states, and cities by products sold and total sales.
   - Display top 5 retailers by total sales.
   - Filter data for women's athletic footwear sales and display top 5 results.
6. **Resampling**:
   - Resample data into weekly and daily bins to get total sales for each period.

## Code
The code is implemented in Python using Pandas library. Below are the key code sections:

### Load Data
```python
import pandas as pd

athletic_sales_2020_path = 'Resources/athletic_sales_2020.csv'
athletic_sales_2021_path = 'Resources/athletic_sales_2021.csv'

athletic_sales_2020_df = pd.read_csv(athletic_sales_2020_path)
athletic_sales_2021_df = pd.read_csv(athletic_sales_2021_path)
##Combine Data and Convert Date Formats
combined_athletic_sales_df = pd.concat([athletic_sales_2020_df, athletic_sales_2021_df], join='inner')
combined_athletic_sales_df.reset_index(drop=True, inplace=True)
combined_athletic_sales_df['invoice_date'] = pd.to_datetime(combined_athletic_sales_df['invoice_date'], format='%y-%m-%d')
##Grouping and Aggregation
combined_athletic_sales_groupby_df = combined_athletic_sales_df.groupby(['region', 'state', 'city'])['units_sold'].sum().reset_index(name='Total_Products_Sold')
pivot_combined_sales_df = combined_athletic_sales_df.pivot_table(values='units_sold', index=['region', 'state', 'city'], aggfunc='sum')
pivot_combined_sales_df_sorted = pivot_combined_sales_df.sort_values(by='units_sold', ascending=False)
pivot_combined_sales_df_sorted.rename(columns={'units_sold': 'Total_Products_Sold'}, inplace=True)
##Resmapling
pivot_most_women_day_df = womens_athletic_sales_df.pivot_table(values='total_sales', index='invoice_date', aggfunc='sum')
pivot_most_women_day_df_sorted = pivot_most_women_day_df.sort_values(by='total_sales', ascending=False)
pivot_most_women_day_df_sorted.rename(columns={'total_sales': 'Total Sales'}, inplace=True)
##Resample into daily bins
daily_sales = pivot_most_women_day_df_sorted.resample('D').sum()
print(daily_sales)
##Results
The analysis includes visualizations and summary statistics for various groupings and time periods. The top regions, states, cities, and retailers by sales are identified, and sales trends over time are examined through weekly and daily resampling.

##Requirements
Python 3.x
Pandas library
Usage
Clone the repository.
Ensure the Resources directory contains the CSV files.
Run the provided Python script to perform the analysis.
##License
This project is licensed under the MIT License. See the LICENSE file for details.

##Acknowledgements
Special thanks to the data providers and the open-source community for their invaluable resources and tools.

This `README.md` provides a comprehensive overview of the project, including data files, analysis steps, key code sections, results, requirements, usage instructions, license information, and acknowledgements. Adjust the `git clone` URL and other details as needed for your specific project.
