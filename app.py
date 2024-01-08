import os
from flask import Flask, request, render_template, send_file
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Check if a file was uploaded
        if "file" not in request.files:
            return "No file part"

        file = request.files["file"]

        # Check if the file has a valid extension
        if file.filename == "":
            return "No selected file"
        if not file.filename.endswith(".csv"):
            return "Invalid file format. Please upload a CSV file."

        # Save the uploaded file to a temporary location
        upload_dir = "uploads"
        os.makedirs(upload_dir, exist_ok=True)
        upload_path = os.path.join(upload_dir, file.filename)
        file.save(upload_path)

        # Read the uploaded CSV file
        subject_data = pd.read_csv(upload_path)
        total_students = len(subject_data)

        # Filter rows containing the grade 'U'
        filtered_data = subject_data[subject_data.apply(lambda row: 'U' in row.values, axis=1)]

        # Reset the index with ordered index numbers starting from 1 and drop the old index
        filtered_data.reset_index(drop=True, inplace=True)

        # Generate a unique filename for the filtered data
        output_excel_filename = "filtered_data.xlsx"

        # Save the filtered data to the specified Excel file without the serial number column
        output_excel_path = os.path.join(upload_dir, output_excel_filename)
        filtered_data.to_excel(output_excel_path, index=False)

        return send_file(output_excel_path, as_attachment=True, download_name=output_excel_filename)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)