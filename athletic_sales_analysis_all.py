# Read the CSV files into DataFrames.

athletic_sales_2020_path = 'Resources/athletic_sales_2020.csv'
athletic_sales_2021_path = 'Resources/athletic_sales_2021.csv'

athletic_sales_2020_df = pd.read_csv(athletic_sales_2020_path)
athletic_sales_2021_df = pd.read_csv(athletic_sales_2021_path)

print(athletic_sales_2020_df.head())
print(athletic_sales_2021_df.head())
# Display the 2020 sales DataFrame
athletic_sales_2020_df
# Display the 2021 sales DataFrame
athletic_sales_2021_df
# Check the 2020 sales data types.
athletic_sales_2020_df.info()
athletic_sales_2020_df.columns
# Check the 2021 sales data types.
athletic_sales_2021_df.info()
athletic_sales_2021_df.columns
# Combine the 2020 and 2021 sales DataFrames on the rows and reset the index.
combined_athletic_sales_df = pd.concat([athletic_sales_2020_df, athletic_sales_2021_df], join='inner')
combined_athletic_sales_df.reset_index(drop=True, inplace=True)
combined_athletic_sales_df
# Check if any values are null.
null_values=combined_athletic_sales_df.isnull().sum()
null_values
# Check the data type of each column
combined_athletic_sales_df.info()
combined_athletic_sales_df.columns
# Convert the "invoice_date" to a datetime datatype
combined_athletic_sales_df['invoice_date'] = pd.to_datetime(combined_athletic_sales_df['invoice_date'], format='%y-%m-%d' )
combined_athletic_sales_df
# Confirm that the "invoice_date" data type has been changed.
combined_athletic_sales_df.info()
# Show the number products sold for region, state, and city.
# Rename the sum to "Total_Products_Sold".

combined_athletic_sales_groupby_df = combined_athletic_sales_df.groupby(['region', 'state', 'city'])['units_sold'].sum().reset_index(name='Total_Products_Sold')
comnined_athletic_sales_groupby_df_sorted = combined_athletic_sales_groupby_df.sort_values(by='Total_Products_Sold', ascending=False)
comnined_athletic_sales_groupby_df_sorted
# Show the top 5 results.
top_5_results = comnined_athletic_sales_groupby_df_sorted.head(5)
top_5_results
combined_athletic_sales_df.columns
# Show the number products sold for region, state, and city.
pivot_combined_sales_df = combined_athletic_sales_df.pivot_table(values='units_sold', index=['region', 'state', 'city'], aggfunc='sum')
pivot_combined_sales_df_sorted = pivot_combined_sales_df.sort_values(by='units_sold', ascending=False)
#pivot_combined_sales_df_sorted
# Rename the "units_sold" column to "Total_Products_Sold"
pivot_combined_sales_df_sorted = pivot_combined_sales_df_sorted.rename(columns={'units_sold': 'Total_Products_Sold'})
pivot_combined_sales_df_sorted

# Show the top 5 results.
pivot_top_5 = pivot_combined_sales_df_sorted.head(5)
pivot_top_5
# Show the total sales for the products sold for each region, state, and city.
# Rename the "total_sales" column to "Total Sales"
most_regional_sales_groupby_df = combined_athletic_sales_df.groupby(['region', 'state', 'city'])['total_sales'].sum().reset_index(name='Total_Sales')
most_regional_sales_groupby_df_sorted = most_regional_sales_groupby_df.sort_values(by='Total_Sales', ascending=False)
most_regional_sales_groupby_df_sorted
# Show the top 5 results.
top_5_regions = most_regional_sales_groupby_df_sorted.head(5)
top_5_regions
# Show the total sales for the products sold for each region, state, and city.
pivot_most_region_sales_df = combined_athletic_sales_df.pivot_table(values='total_sales', index=['region','state','city'],aggfunc='sum')
pivot_most_region_sales_df_sorted = pivot_most_region_sales_df.sort_values(by='total_sales', ascending=False)
pivot_most_region_sales_df_sorted
# Optional: Rename the "total_sales" column to "Total Sales"
pivot_most_region_sales_df_sorted = pivot_most_region_sales_df_sorted.rename(columns={'total_sales':'Total Sales'})
pivot_most_region_sales_df_sorted
# Show the top 5 results.
mostregional_top_5 = pivot_most_region_sales_df_sorted.head(5)
mostregional_top_5
# Show the total sales for the products sold for each retailer, region, state, and city.
# Rename the "total_sales" column to "Total Sales"
most_retailer_sales_groupby_df = combined_athletic_sales_df.groupby(['retailer','region', 'state', 'city'])['total_sales'].sum().reset_index(name='Total_Sales')
most_retailer_sales_groupby_df_sorted = most_retailer_sales_groupby_df.sort_values(by='Total_Sales', ascending=False)
most_retailer_sales_groupby_df_sorted
# Show the top 5 results.
top_5_retailers = most_retailer_sales_groupby_df_sorted.head(5)
top_5_retailers
# Show the total sales for the products sold for each retailer, region, state, and city.
pivot_top_retailer_sales_df= combined_athletic_sales_df.pivot_table(values='total_sales', index=['retailer', 'region', 'state', 'city'], aggfunc='sum')
pivot_top_retailer_sales_df_sorted = pivot_top_retailer_sales_df.sort_values(by='total_sales', ascending=False)
pivot_top_retailer_sales_df_sorted
# Optional: Rename the "total_sales" column to "Total Sales"
pivot_top_retailer_sales_df_sorted = pivot_top_retailer_sales_df_sorted.rename(columns={'total_sales': 'Total Sales'})
pivot_top_retailer_sales_df_sorted 
# Show the top 5 results.
pivot_top_5_retailers = pivot_top_retailer_sales_df_sorted.head(5)
pivot_top_5_retailers
# Filter the sales data to get the women's athletic footwear sales data.
womens_atheletic_sales_df = combined_athletic_sales_df[combined_athletic_sales_df['product'].str.contains("Women's Athletic Footwear")]
womens_atheletic_sales_df
# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
womens_atheletic_sales_groupby_df = womens_atheletic_sales_df.groupby(['retailer','region', 'state', 'city'])['units_sold'].sum().reset_index(name='Womens_Footwear_Units_Sold')
womens_atheletic_sales_groupby_df_sorted = womens_atheletic_sales_groupby_df.sort_values(by='Womens_Footwear_Units_Sold', ascending=False)
womens_atheletic_sales_groupby_df_sorted 

# Show the top 5 results.
womens_atheletic_sales_top_5 = womens_atheletic_sales_groupby_df_sorted.head(5)
womens_atheletic_sales_top_5
# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.

pivot_womens_atheltics_sales_df = womens_atheletic_sales_df.pivot_table(values='units_sold', index=['retailer', 'region', 'state', 'city'], aggfunc='sum')
pivot_womens_atheltics_sales_df_sorted = pivot_womens_atheltics_sales_df.sort_values(by='units_sold', ascending=False)
pivot_womens_atheltics_sales_df_sorted
# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
pivot_womens_atheltics_sales_df_sorted = pivot_womens_atheltics_sales_df_sorted.rename(columns={'units_sold': 'Womens_Footwear_Units_Sold'})
pivot_womens_atheltics_sales_df_sorted
# Show the top 5 results.
top_5_womens_athletic = pivot_womens_atheltics_sales_df_sorted.head(5)
top_5_womens_athletic
womens_atheletic_sales_df.columns
# Create a pivot table with the 'invoice_date' column is the index, and the "total_sales" as the values.

pivot_most_women_day_df = womens_atheletic_sales_df.pivot_table(values='total_sales', index='invoice_date', aggfunc='sum')
pivot_most_women_day_df_sorted = pivot_most_women_day_df.sort_values(by='total_sales', ascending=False)
pivot_most_women_day_df_sorted
# Optional: Rename the "total_sales" column to "Total Sales"
pivot_most_women_day_df_sorted = pivot_most_women_day_df_sorted.rename(columns={'total_sales': 'Total Sales'})
pivot_most_women_day_df_sorted
# Show the table.
most_women_day_top = pivot_most_women_day_df_sorted.head(10)
most_women_day_top
# Resample the pivot table into daily bins, and get the total sales for each day.
women_day_sales = pivot_most_women_day_df_sorted.resample('D').sum()
women_day_sales
# Sort the resampled pivot table in descending order on "Total Sales".
women_day_sales_sorted = women_day_sales.sort_values(by='Total Sales', ascending=False).head(10)
women_day_sales_sorted
# Resample the pivot table into weekly bins, and get the total sales for each week.
women_weekly_sales = pivot_most_women_day_df_sorted.resample('W').sum()
women_weekly_sales

# Sort the resampled pivot table in descending order on "Total Sales".
women_weekly_sales_sorted = women_weekly_sales.sort_values(by='Total Sales', ascending=False).head(10)
women_weekly_sales_sorted