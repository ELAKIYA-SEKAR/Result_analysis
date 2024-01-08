import pandas as pd

# Read the CSV file
subject_data = pd.read_csv(
    r"D:\result_analysis\University Result Analysis III A 4TH SEM - 2022 - 2023(EVEN).csv")

# Filter rows containing the grade 'U'
pass_data = subject_data[subject_data.apply(lambda row: 'U' not in row.values, axis=1)]

# Calculate the percentage of students who passed
pass_percentage = (len(pass_data) / len(subject_data)) * 100

print(f"Percentage of students who passed: {pass_percentage:.2f}%")