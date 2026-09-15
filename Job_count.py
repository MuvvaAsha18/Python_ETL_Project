import csv


with open("Employee 1000x.csv") as f:
    reader = csv.DictReader(f)
    employees = list(reader)


job_counts = {}
for emp in employees:
    role = emp["Job Title"]
    job_counts[role] = job_counts.get(role, 0) + 1


with open("job_roles.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Job Title", "Count"])
    for role, count in job_counts.items():
        writer.writerow([role, count])


for role, count in job_counts.items():
    print(f"{role}: {count}")

male_count = 0
female_count = 0

for emp in employees:
    gender = emp["Sex"].capitalize()
    if gender == "Male":
        male_count += 1
    elif gender == "Female":
        female_count += 1

print(f"Total Males: {male_count}")
print(f"Total Females: {female_count}")


