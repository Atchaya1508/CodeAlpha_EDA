                                       Exploratory Data Analysis
# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('/content/drive/MyDrive/Ship_Performance_Dataset.csv') 
                                   
# Show first few rows
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Summary statistics
print("\nSummary statistics:")
print(df.describe())

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Data types and unique values
print("\nData types and unique values:")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values, Type: {df[col].dtype}")

# Histograms
df.hist(bins=30, figsize=(12, 8))
plt.suptitle("Feature Distributions")
plt.tight_layout()
plt.show()

# Boxplots to detect outliers
for col in df.select_dtypes(include=np.number).columns:
    plt.figure(figsize=(8, 4))
    sns.boxplot(data=df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()