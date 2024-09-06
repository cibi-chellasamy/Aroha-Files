# creating Employee Csv with 10k random entries using Faker library.
# Creating names with some pre-defined name list with initials (to have Indian Names)
# Date of Birth I have chosen dates from the year 1964 to 2005
# Skills I have a predefined list to randomly chosen by machine
# If DOJ is present I can calculate Experience by subtracting DOJ by DoB. Here we dont have DOJ columns.
# So I have asked machine to randomly choose number (1-20)

import csv
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Sample words to construct meaningful names
names = ['Reshma', 'Anu', 'Graha', 'Ishwarya', 'Selva', 'Brindha', 'Dakshinesh','Jeyam','Prabavathi','Sakthivelu']
initials = ['Anbu','Balu','Cathi','Dina','Ezhil','Fabin','Garuda','Huma','Ishan','Jana']

# Function to generate a meaningful name
def naming():
    name = random.choice(names)
    initial = random.choice(initials)
    return f"{name} {initial}"


# Generating a random date of birth
start_date = datetime(1964, 1, 1)
end_date = datetime(2005, 12, 31)
def date_of_birth():
    dob = (start_date +timedelta(days=random.randint(0, (end_date - start_date).days)))
    return dob.strftime("%d/%m/%Y")


# Generating random skills
def skill_list():
    skills_list = [" Information and cybersecurity","Python", "AWS", "Data Science","Java", "SQL", "JavaScript", "DevOps",
                   "Machine Learning","Data Analytics","Data engineering","Business application development"]
    return ",".join(random.sample(skills_list, random.randint(1, len(skills_list))))


# Create and write to the CSV file
with open('Employee_data.csv', mode='w', newline='') as file:
    employee = csv.writer(file)

    # Write header (to have a column)
    employee.writerow(["Name", "Age", "DOB", "Experience", "Salary_CT", "Skills"])

    # Generating 10,000 entries
    for i in range(10000):
        name = naming()
        age = random.randint(22, 60)
        dob = date_of_birth()
        experience = random.randint(1, 20)
        salary_ct = round(random.uniform(50000, 150000), 2)
        skills = skill_list()

        # Writing in to the CSV file
        employee.writerow([name, age, dob, experience, salary_ct, skills])

print("CSV file 'Employee_data.csv' generated successfully.")
