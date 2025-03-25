# Zomato Sales & User Performance Dashboard

### Dashboard Link: [Zomato Power BI Dashboard](https://app.powerbi.com/reportEmbed?reportId=8ceb7b5d-aed9-4970-a416-37b6762cdc47&autoAuth=true&ctid=0d8f96a4-62c2-4e68-9449-66de88e46f86)

## Problem Statement

This dashboard provides an in-depth analysis of Zomato's sales and user performance based on various metrics. The key objectives include:
- Identifying top-performing cities based on sales revenue.
- Analyzing user behavior across different age groups and genders.
- Understanding customer retention and churn rates.
- Comparing current year vs. previous year sales trends.

The dashboard consists of three main slides: **Overview, User Performance, and Performance by City**, each offering interactive insights for better decision-making.

---
## Steps Followed

### **Overview Slide**
- **Clustered Bar Chart:** Displays the **top N cities** based on sales.
  - Uses **DAX measure**:
    ```DAX
    TopN_Sale = 
    VAR RankValue = RANKX(
        ALL(orders[city]),
        [sales_value],
        ,
        DESC
    )
    VAR SelectedRank = SELECTEDVALUE(RankTable[No], 0)
    RETURN
        IF(
            SelectedRank = 0, 
            [sales_value],
            IF(
                RankValue <= SelectedRank, 
                [sales_value],
                BLANK()
            )
        )
    ```
- **Line Chart:** Shows sales trends over time.
  - **X-axis:** Order Date (Year-wise)
  - **Y-axis:** Sales Value (`sales_value = SUM(orders[Value])`)
- **6 Cards for Ratings & Sales Analysis:**
  - **Filters:** Sales values for categories (Veg, Non-Veg, Others)
  - **Ratings Measure:**
    ```DAX
    rating_counts = COUNT(restaurant[rating])
    ```
- **Slicer:** Allows selection of Amount or Quantity.
- **More Cards (Top Right Corner):** Shows **Quantity, Amount, Rating Counts, and Order Counts**.

---
### **User Performance Slide**
- **Clustered Column Chart:** Displays **user distribution by age**.
  - **X-axis:** Age
  - **Y-axis:** User Count (`UserCount = DISTINCTCOUNT(users[user_id])`)
- **Loss Customers by Gender (Donut Chart):**
  - **Legend:** Gender
  - **Values:** Loss Customers (`losscustomer`)
  - **DAX Calculation:**
    ```DAX
    losscustomer = VAR FilterUsers = 
    FILTER(SUMMARIZE(users,users[user_id]),AND([curryrsale]<=0,[prevyrsale]>0))
    RETURN CALCULATE([UserCount],FilterUsers)
    ```
- **Gain Customers by Gender (Donut Chart):**
  - **Legend:** Gender
  - **Values:** Gain Customers (`gaincustomer`)
  - **DAX Calculation:**
    ```DAX
    gaincustomer = VAR FilterUsers = 
    FILTER(SUMMARIZE(users,users[user_id]),AND([prevyrsale]<=0,[curryrsale]>0))
    RETURN CALCULATE([UserCount],FilterUsers)
    ```
- **Cards (Below Donut Charts):** Displays Loss and Gain Customers.

---
### **Performance by City Slide**
- **Table (City-Wise Performance):**
  - **Columns:** City, Sales Value, Order Count, Current Year Sales, Previous Year Sales.
  - **DAX Measures:**
    ```DAX
    curryrsale = VAR Yr=[CurrYear]
    RETURN CALCULATE([sales_value],orders[Year]=yr)
    
    prevyrsale = VAR Yr=[PrevYear]
    RETURN CALCULATE([sales_value],orders[Year]=yr)
    
    order_count = COUNT(orders[order_date])
    
    sales_value = SUM(orders[Value])
    ```
- **Three Clustered Bar Charts:**
  - **Sales by City:** `sales_value = SUM(orders[Value])`
  - **Ratings by City:** `rating_counts = COUNT(restaurant[rating])`
  - **Active Users by City:** `Activeusers = DISTINCTCOUNT(orders[user_id])`

---
## Key Insights

- **Top Performing Cities:** Cities contributing the most to sales revenue.
- **User Behavior:** Age and gender-wise analysis of active, lost, and gained customers.
- **Sales Trends:** Year-over-year comparison of sales data.
- **Customer Ratings:** Evaluation of customer preferences and feedback trends.
- **Performance by City:** Data-driven insights for regional performance optimization.

---
## Filters & Interactive Elements
- **Slicers for filtering Amount & Quantity**
- **City-wise filters for performance analysis**
- **Role-based and category-based filtering options**
- **Tooltips for additional insights on hover**

---
## Screenshots

![Image](https://github.com/user-attachments/assets/9d4ff840-cc0e-49c0-8b7c-3321ec41662d)
![Image](https://github.com/user-attachments/assets/c6268a5e-f14a-4405-8037-3fad8d4efff0)
![Image](https://github.com/user-attachments/assets/86ede6ff-c00e-45b9-835e-bbe03419ab9b)

---
## Publishing & Final Report
- The **dashboard was published on Power BI Service**.
- Users can **interact with the report**, explore insights, and make data-driven decisions.

---
## Conclusion

This **Zomato Sales & User Performance Dashboard** provides a **comprehensive analysis of sales and user behavior** using interactive Power BI visualizations. By leveraging **DAX calculations, charts, and slicers**, users can explore insights in an engaging and data-driven manner.

---
### Author: **Akanksha Bisht**  
### Date: **August 25, 2024**  
### Institution: **Shivalik College of Engineering (SCE)**

