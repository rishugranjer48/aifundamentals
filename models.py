import csv

with open("students.csv", "w") as f:
    fieldnames = ["name", "age", "grade"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 20, "grade": "A"})
    writer.writerow({"name": "Bob", "age": 22, "grade": "B"})
    writer.writerow({"name": "Charlie", "age": 21, "grade": "C"})

    with open("students.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
