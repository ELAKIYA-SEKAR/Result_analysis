import pandas as pd
import matplotlib.pyplot as plt

subject_data = pd.read_csv(
    r"D:\result_analysis\University Result Analysis III A 4TH SEM - 2022 - 2023(EVEN).csv")

# Create an empty DataFrame to store the results
result_df = pd.DataFrame(
    columns=['Subject Code', 'Pass Percentage', 'Fail Percentage', 'Total Students'])

# Create lists to store pass percentages, fail percentages, subject labels, and total students
pass_percentages = []
fail_percentages = []
subject_labels = []
total_students = len(subject_data)

while True:
    column_name = input("Enter the Subject code (or press Enter to exit): ")

    if not column_name:
        break  # Exit the loop if the user presses Enter without entering a column name

    if column_name not in subject_data.columns:
        print("Invalid subject code. Please enter a valid subject code.")
    else:
        # Append the subject code to the list
        subject_labels.append(column_name)
        grade_counts = subject_data[column_name].value_counts()
        pass_percentage = 0
        fail_percentage = 0

        # Check if the grades are present in the data and calculate pass/fail percentages accordingly
        if 'O' in grade_counts:
            pass_percentage += (grade_counts['O'] / total_students) * 100
        if 'A' in grade_counts:
            pass_percentage += (grade_counts['A'] / total_students) * 100
        if 'A+' in grade_counts:
            pass_percentage += (grade_counts['A+'] / total_students) * 100
        if 'B' in grade_counts:
            pass_percentage += (grade_counts['B'] / total_students) * 100
        if 'B+' in grade_counts:
            pass_percentage += (grade_counts['B+'] / total_students) * 100
        if 'C' in grade_counts:
            pass_percentage += (grade_counts['C'] / total_students) * 100

        # Calculate fail percentage for grade 'U'
        if 'U' in grade_counts:
            fail_percentage = (grade_counts['U'] / total_students) * 100

        # Append the results to a temporary DataFrame
        temp_df = pd.DataFrame({'Subject Code': [column_name],
                                'Pass Percentage': [pass_percentage],
                                'Fail Percentage': [fail_percentage],
                                'Total Students': [total_students]})

        # Concatenate the temporary DataFrame to the result DataFrame
        result_df = pd.concat([result_df, temp_df], ignore_index=True)

        # Store pass and fail percentages
        pass_percentages.append(pass_percentage)
        fail_percentages.append(fail_percentage)

pass_data = subject_data[subject_data.apply(lambda row: 'U' not in row.values, axis=1)]

# Calculate the percentage of students who passed
pass_percentage = (len(pass_data) / len(subject_data)) * 100

print(f"Percentage of students who passed: {pass_percentage:.2f}%")

# Create a bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(subject_labels, pass_percentages,
               label='Pass Percentage', color='green', alpha=0.7)
plt.bar(subject_labels, fail_percentages, bottom=pass_percentages,
        label='Fail Percentage', color='red', alpha=0.7)
plt.xlabel('Subject Code')
plt.ylabel('Percentage')
plt.title('Pass and Fail Percentages by Subject')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Add labels for pass and fail percentages inside the bars
for bar, pass_percentage, fail_percentage in zip(bars, pass_percentages, fail_percentages):
    plt.text(bar.get_x() + bar.get_width() / 2, pass_percentage / 2,
             f'Pass: {pass_percentage:.2f}%', ha='center', color='white')
    plt.text(bar.get_x() + bar.get_width() / 2, pass_percentage + fail_percentage / 2,
             f'Fail: {fail_percentage:.2f}%', ha='center', color='white')

# Save the chart as an image
plt.savefig('pass_fail_percentages.png')

# Reset the index starting from 1
result_df.reset_index(drop=True, inplace=True)
result_df.index += 1

# Display the chart
plt.show()

# Display the results DataFrame
print(result_df)
