# Crime Data Analysis

## Overview
This project focuses on analyzing crime cases across different years and cities using Python and Pandas. The analysis aims to uncover patterns and trends in crime rates, providing insights for better decision-making.

## Datasets
The project uses the following datasets:
- **rape2020-2022.csv** - Contains year-wise data on reported rape cases.
- **rapecasesamongcities.csv** - Contains city-wise crime details.

## Steps Followed
1. **Data Loading:**
   - Read CSV files using Pandas.
   - Display initial records and check column names.
   ```python
   import pandas as pd
   
   df1 = pd.read_csv("rape2020-2022.csv")
   df2 = pd.read_csv("rapecasesamongcities.csv")
   
   print(df1.head())
   print(df2.head())
   print(df1.columns)
   print(df2.columns)
   ```

2. **Data Cleaning:**
   - Handle missing values.
   - Convert data types if necessary.

3. **Exploratory Data Analysis (EDA):**
   - Visualize trends in crime rates.
   - Compare city-wise statistics.
   - Identify high-crime regions.
   
   ## Screenshots
   ![Image](https://github.com/user-attachments/assets/e5a0a221-ba3d-46c1-b5db-3676acaf5399)
   ![Image](https://github.com/user-attachments/assets/ca929e7c-a282-4c50-b85a-bd7f9926a947)
   ![Image](https://github.com/user-attachments/assets/438aa887-de36-404a-b7f3-200669684ab9)
   
4. **Insights & Findings:**
   - Identify which cities have the highest crime rates.
   - Observe trends over the years.
   - Provide recommendations based on analysis.

## Requirements
- Python
- Pandas
- Matplotlib / Seaborn (for visualization)

## How to Run
1. Install dependencies:
   ```bash
   pip install pandas matplotlib seaborn
   ```
2. Run the Jupyter Notebook or Python script to analyze the data.

### Author: **Akanksha Bisht**  
### Date: **July 18, 2024**  
### Institution: **Shivalik College of Engineering (SCE)**  

