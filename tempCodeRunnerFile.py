while True:
    column_name = input("Enter the Subject code (or press Enter to exit): ")
    
    if not column_name:
        break  # Exit the loop if the user presses Enter without entering a column name
    
    if column_name not in data.columns:
        print("Invalid subject code. Please enter a valid subject code.")
    else: