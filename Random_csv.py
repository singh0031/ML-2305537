import csv
import random

# Define fields
fields = ["ID", "Age", "Salary", "Score", "Rating"]

# Generate 10 random employee records
records = []
for emp_id in range(1, 11):
    record = {
        "ID": emp_id,
        "Age": random.randint(18, 60),
        "Salary": random.randint(20000, 80000),
        "Score": random.randint(1, 100),
        "Rating": round(random.uniform(0, 5), 2)
    }
    records.append(record)

# Write records into a CSV file
filename = "employee_data.csv"
with open(filename, "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)

print(f"{filename} created successfully with 10 employee records!")

