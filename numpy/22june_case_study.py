"""
Q1. Write NumPy code to create a random integer array of shape (30, 5) with values between 50 and 500. Name it sales_data.
hint  : np.random.randint(50,500,size=(30,5))


Q2. What function would you use to check the shape, data type, and number of dimensions of
sales_data?
Hint: Use .shape, .dtype, .ndim

Q3. How many total sales values are stored in this array? Write the NumPy expression to find this.
hint  : np.size()

Q4. Extract the sales data for just the first product (column 0). What is the resulting shape?
hint : slicing  

Q5. Slice the data to get sales for days 10 to 20 (inclusive) for all products.
hint  :slicing 

Q6. Calculate the total sales for each product across all 30 days.
Hint: Sum along axis=0    np.sum(axis=0)

Q7. Find the average daily sales across all products combined. hint  : np.mean()

Q8. Which product had the highest total sales? Write the NumPy code to find its index.
Hint: np.argmax()

[[1,2,3],
[5,8,5]]   np.argmax(arr,axis =0)

Q9. Find the standard deviation of sales for each product. What does a high std dev indicate?  np.std(axis=0)

Q10. Calculate the median daily sales for the entire dataset. np.median(axis=0)

Q11. Find the minimum and maximum sales values recorded in the entire dataset. np.min() , np.max()

Q12. Write code to find all days where sales of Product 3 exceeded 300 units.
Q13. How many days had total sales (across all products) greater than 1500?
Hint: Use np.sum() on a boolean mask
Q14. Replace all sales values below 60 with 60 (treat these as the minimum threshold). Write the
NumPy code.
Q15. Find the indices (day numbers) where Product 1 had its top 5 highest sales days.
"""
import numpy as np

sales_data = np.loadtxt(
    "numpy//retailcorp_sales_data.csv",
    delimiter=",",
    skiprows=1,
    usecols=(1, 2, 3, 4,5)
)

print(sales_data)
"""
product_1 =sales_data[:,0:1]  # [:,0:1]   # row ,col 
print(product_1)
print(product_1.shape)

"""

print([sales_data[:,2:3]>300]) 

# my soultion  : 
"""result = np.where(sales_data[:,2:3]>300)[0]+1
print(result)"""

sales_data[-5:]   # arr = np.array([1,2,3,4,5])