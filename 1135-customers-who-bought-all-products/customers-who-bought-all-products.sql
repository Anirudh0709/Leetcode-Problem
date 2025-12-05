# Write your MySQL query statement below
Select customer_id
From Customer
Group by customer_id
Having Count(Distinct product_key)=(Select Count(*)from Product)
