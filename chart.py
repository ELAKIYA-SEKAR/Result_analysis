import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r"D:\result_analysis\University Result Analysis III A 4TH SEM - 2022 - 2023(EVEN).csv")
while True:
    column_name = input("Enter the Subject code (or press Enter to exit): ")
    
    if not column_name:
        break  # Exit the loop if the user presses Enter without entering a column name
    
    if column_name not in data.columns:
        print("Invalid subject code. Please enter a valid subject code.")
    else:

        grade_count = data[column_name].value_counts()

        plt.figure(figsize=(6, 6))
        plt.pie(grade_count, labels=grade_count.index,
                autopct='%1.1f%%', startangle=140)
        plt.title(column_name)
        plt.axis('equal')
        plt.show()
