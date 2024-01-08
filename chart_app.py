import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the CSV data when the Flask app starts
data = pd.read_csv("D:\result_analysis\University Result Analysis III A 4TH SEM - 2022 - 2023(EVEN).csv")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        column_name = request.form.get("subject_code")

        if not column_name:
            return render_template("index.html", error="Please enter a subject code.")

        if column_name not in data.columns:
            return render_template("index.html", error="Invalid subject code. Please enter a valid subject code.")

        grade_count = data[column_name].value_counts()

        plt.figure(figsize=(6, 6))
        plt.pie(grade_count, labels=grade_count.index,
                autopct='%1.1f%%', startangle=140)
        plt.title(column_name)
        plt.axis('equal')

        # Save the pie chart as an image
        chart_filename = f"{column_name}_pie_chart.png"
        chart_path = f"static/{chart_filename}"
        plt.savefig(chart_path)

        return render_template("result.html", chart_path=chart_filename)

    return render_template("index1.html")

if __name__ == "__main__":
    app.run(debug=True)
