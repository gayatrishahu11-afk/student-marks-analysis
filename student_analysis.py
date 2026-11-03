import pandas as pd
import numpy as np

# Step 1: Load the dataset
df = pd.read_csv("StudentsPerformance.csv")

print("====================================")
print("     STUDENT MARKS ANALYSIS")
print("====================================")

# Step 2: Display first five records
print("\nFirst Five Student Records:")
print(df.head())

# Step 3: Check dataset information
print("\nDataset Information:")
print("Total Rows and Columns:", df.shape)

# Step 4: Check missing values
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# Step 5: Clean missing data
df = df.dropna().copy()

# Step 6: Select subject columns
subjects = ["math score", "reading score", "writing score"]

# Convert marks into numeric values
for subject in subjects:
    df[subject] = pd.to_numeric(df[subject], errors="coerce")

# Remove invalid or missing marks
df = df.dropna(subset=subjects).copy()

# Step 7: Calculate average marks
print("\nAverage Marks:")
average = df[subjects].mean()
print(average.round(2))

# Step 8: Calculate maximum marks
print("\nMaximum Marks:")
maximum = df[subjects].max()
print(maximum)

# Step 9: Calculate minimum marks
print("\nMinimum Marks:")
minimum = df[subjects].min()
print(minimum)

# Step 10: Use NumPy for numerical analysis
marks = df[subjects].to_numpy()

print("\nNumPy Analysis:")
print("Overall Average:", round(np.mean(marks), 2))
print("Overall Maximum:", np.max(marks))
print("Overall Minimum:", np.min(marks))

# Step 11: Display final summary using Pandas
summary = pd.DataFrame({
    "Subject": subjects,
    "Average Marks": average.values.round(2),
    "Maximum Marks": maximum.values,
    "Minimum Marks": minimum.values
})

print("\n====================================")
print("          FINAL SUMMARY")
print("====================================")

print(summary.to_string(index=False))

# Step 12: Display final dataset information
print("\nMissing Values After Cleaning:")
print(df[subjects].isnull().sum())

print("\nTotal Students Analyzed:", len(df))

print("\n====================================")
print(" PROJECT COMPLETED SUCCESSFULLY!")
print("====================================")