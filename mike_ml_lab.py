
# coding: utf-8

# # Setup

# In[1]:


# initial setup
import pandas as pd
orders_df = pd.read_csv("data/Orders.csv")
orders_df.head()
len(orders_df)


# In[2]:


# fix rownames
orders_df.columns = orders_df.columns.str.lower().str.replace(".", "_")
orders_df.columns


# # Problem 1

# In[3]:


# problem 1, look at profit and sales 
print(orders_df.sales.head(5))
print(orders_df.profit.head(5))
# need to remove $ and convert from obj (very generic) to numeric


# In[4]:


# fixed sales
orders_df.sales = pd.to_numeric(orders_df.sales.str.replace("$", "").str.replace(",",""))


# In[5]:


# checking against NAs
orders_df.sales.head(5)
orders_df.sales.plot(kind='hist')
print(len(orders_df.sales))
print(orders_df.sales.head(10))


# In[6]:


#fix profit
orders_df.profit = pd.to_numeric(orders_df.profit.str.replace("$", "").str.replace(",",""))


# In[7]:


orders_df.profit.head(5)


# # Problem 2

# In[8]:


orders_df.order_date.head(5)


# In[9]:


#have to convert object to datetime 
orders_df.order_date = pd.to_datetime(orders_df.order_date)
orders_df.ship_date = pd.to_datetime(orders_df.ship_date)


# In[10]:


print(orders_df.order_date.head(2))
print(orders_df.ship_date.head(2))


# In[11]:


#mutate a new column for grouping by quarter
orders_df_2 = orders_df.order_date.dt.quarter
orders_df['order_quarter'] = orders_df_2


# In[12]:


orders_df.quantity.head(2)


# In[13]:


# investigating category, order_quarte
quarterly_orders = orders_df.groupby(['category', 'order_quarter'])[['quantity']].agg('sum')
quarterly_orders
quarterly_orders.unstack().plot(kind = 'bar')


# Grouped by category and the fiscal quarter, you can see that there are significant increases in item purchases as the year progresses. Are there specific types of products that drive this growth?

# In[14]:


quarterly_sub_orders = orders_df.groupby(['category', 'sub_category', 'order_quarter'])[['quantity']].agg('sum')
quarterly_sub_orders
quarterly_sub_orders.unstack().plot(kind = 'barh', figsize=[6,16])


# Office supplies are a BIG seller as Q1 to Q4.
# Furniture, tables do not increase dramatically over time. 
# Subcategories and categories differ in their sales changes by quarter, but in most cases, trend is upwards as time progresses from Q1 to Q4.

# # Problem 3

# In[15]:


returns_df = pd.read_csv("data/Returns.csv")
returns_df.columns = returns_df.columns.str.lower().str.replace(" ", "_")
returns_df.head()


# In[16]:


#join on order_id
combined_df = pd.merge(orders_df, returns_df, how = 'left', on = 'order_id')


# In[18]:


len(combined_df)

