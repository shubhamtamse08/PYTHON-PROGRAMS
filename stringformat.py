headers = ["Name", "Age", "Department"]

data = [
    ["raj", 25, "HR"],
    ["anjali", 34, "finance"],
    ["aman", 23, "sales"],
    ["hem", 29, "finance"]
]

print(f"{headers[0]:<12}{headers[1]:<5}{headers[2]:<15}")
print("*" * 30)

for row in data:
    print(f"{row[0]:<12}{row[1]:<5}{row[2]:<15}")
