-- Total Sales by Category
SELECT Category, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category;

-- Profit by Region
SELECT Region, SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Region;

-- Top 10 Sub-Categories by Sales
SELECT [Sub-Category], SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY [Sub-Category]
ORDER BY Total_Sales DESC
LIMIT 10;

-- Total Sales and Profit
SELECT 
    SUM(Sales) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM superstore;