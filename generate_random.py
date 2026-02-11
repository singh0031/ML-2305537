import csv
import random

fields = ["ID", "Age", "Salary", "Score", "Rating"]
records = []

for i in range(10):
    data = {
        "ID": random.randint(1, 100),
        "Age": random.randint(18, 60),
        "Salary": random.randint(20000, 80000),
        "Score": random.randint(1, 100),
        "Rating": float(f"{random.uniform(0, 1):.2f}")
    }
    records.append(data)

with open("random_output.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(records)

print("random_output.csv generated successfully!")
