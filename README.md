This Jupyter Notebook is designed for exploratory data analysis (EDA) and data preprocessing on the dataset "Gunnels.csv." 
It begins by loading the dataset using pandas, displaying column names, dataset dimensions, summary statistics, and data types, 
followed by checking for missing values and removing duplicates. The notebook then performs data cleaning, such as stripping whitespace 
from column names and handling missing values—filling numerical columns with the mean and categorical columns with the mode. 
To ensure consistency, it converts numerical columns like Time, Fromlow, Slope, and Rw to numeric types and categorical columns such as 
Amphiso, Subst, Pool, Water, and Cobble to categorical types. For data visualization, it utilizes Matplotlib and Seaborn to generate 
insightful plots and explore relationships between variables. To run the notebook, users must install pandas, numpy, matplotlib, and 
seaborn using pip install. The dataset should be placed in the same directory as the notebook, and users can execute the cells sequentially 
to analyze and preprocess the data. The notebook can be extended to include advanced machine learning models or feature engineering, depending
on the analysis requirements.







