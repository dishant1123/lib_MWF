"""
loc  :
iloc  : 
"""
import pandas as pd 

# df = pd.read_csv("pandas\mckinsey.csv")
# print(df)

# print(df['country'])
# print(df[['country','life_exp']])

# loc : label 

"""print(df.loc[2])
print(df.loc[2 :5])   # 2 index start   5 index end  last  value  include 
print(df.loc[2:5,['country','life_exp']])
print(df.loc[2:5,['country:life_exp']])  # task  
"""
# iloc : index number 
"""print(df.iloc[2])
print(df.iloc[2 :5])   # last value  excluded 
print(df.iloc[2 :5 ,1:3])   # last value  excluded 
"""
# year ==2002 life_exp >30 
# print(df[(df['year']==2002) & (df['life_exp']>50)])

"""
result =df.loc[(df['year']==2002) & (df['life_exp']>50)][['country','life_exp']]
print(result)
"""

"""
result = df.query("year==2002 & life_exp>50")
print(result)
"""

# join  : inner  join  , outer ,left ,right : 

"""customer = pd.DataFrame({
    "id" :[1,2,3,4,5], 
    "name" :["ram","sita","ravan","laxman","surekha"],
    "city" :["ahm","ahmedabad","bombay","mumbai","delhi"]
})

products = pd.DataFrame({
    "id" :[1,2,3,4,5,6,7,8],
    "product_name" :["mobile","laptop","desktop","tablet","smartphone","printer","scanner","camera"],
    "price" :[1000,2000,3000,4000,5000,9000,10000,11000]
})

print(customer)
print(products)
"""
# merge : 
"""
result = pd.merge(
    customer,
    products,
    on="id",
    how="inner"
)
print(result)
"""
"""
result = pd.merge(
    customer,
    products,
    on="id",
    how="right"
)
print(result)
"""

"""result = pd.merge(
    customer,
    products,
    on="id",
    how="outer"
)
print(result)
"""

# sort , groupby : 

"""df = pd.DataFrame({
    "id" :[1,2,3,4,5,6,7,8,9,10], 
    "department" :["HR","IT","HR","Finance","HR","Finance","IT","HR","Finance","IT"],
    "salary" :[10000,23000,3000,4000,5000,6000,7000,8000,9000,21000]
})

print(df)
"""
# department  wise print salary  :

"""depart_wise_salary =df.groupby("department")['salary'].sum() 
print(depart_wise_salary)
"""
# sort by salary  : 

"""sort_by_salary  = df['salary'].sort_values(ascending=False)
print(sort_by_salary)
"""

# drop_duplicates() :
"""
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Alice", "Bob", "David"],
    "Age": [25, 30, 35, 25, 30, 40],
    "City": ["NY", "LA", "SF", "NY", "DC", "TX"]
})


print(df)

# df =df.drop_duplicates(subset=["Name", "City"],keep="last")
df =df.drop_duplicates().sum()
print(df)
"""

# pivot_table :
"""sales_data = pd.DataFrame({
    "Date": [
        "2026-01-01", "2026-01-01", "2026-01-02",
        "2026-01-02", "2026-01-03", "2026-01-03",
        "2026-01-04", "2026-01-04"
    ],
    "Region": [
        "North", "South", "North", "South",
        "East", "West", "East", "West"
    ],
    "Product": [
        "Laptop", "Laptop", "Mouse", "Mouse",
        "Keyboard", "Keyboard", "Laptop", "Mouse"
    ],
    "Sales": [
        50000, 45000, 5000, 6000,
        8000, 7000, 55000, 6500
    ]
})

print(sales_data)

pivort_table = sales_data.pivot_table(
    columns ="Region",
    values="Sales",
    aggfunc="sum"
)
print(pivort_table)
"""

# concat : 
jan_sales = pd.DataFrame({
    "product_id":[101,102,103,104,105],
    "product_name":["monitor","keyboard","mouse","CPU","printer"],
    "sales":[100,200,300,400,500]
})

feb_sales = pd.DataFrame({
    "product_id":[106,107,108,109,110],
    "product_name":["monitor","keyboard","mouse","CPU","printer"],
    "sales":[10000,20000,30000,40000,50000]
})


# all_sales = pd.concat([jan_sales,feb_sales])
# all_sales = pd.concat([jan_sales,feb_sales],axis=1)
all_sales = pd.concat([jan_sales,feb_sales],axis=0)


print(all_sales)
