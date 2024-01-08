import pandas as pd

# Read the CSV file
subject_data = pd.read_csv(
    r"D:\result_analysis\University Result Analysis III A 4TH SEM - 2022 - 2023(EVEN).csv")
total_students = len(subject_data)
# Filter rows containing the grade 'U'
filtered_data = subject_data[subject_data.apply(lambda row: 'U' in row.values, axis=1)]

# Reset the index with ordered index numbers starting from 1 and drop the old index
filtered_data.reset_index(drop=True, inplace=True)

# Ask the user for the file path and name to save the filtered data
output_excel_file = input("Enter the file path and name to save the filtered data (e.g., C:\\filtered_data.xlsx): ")

# Save the filtered data to the specified Excel file without the serial number column
filtered_data.to_excel(output_excel_file, index=False)

print("Filtered data with 'U' grades has been saved to", output_excel_file)