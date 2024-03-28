# DummyData.py
import random

# Generate dates YYYY-MM-DD
def generateDate():
    year = random.randrange(2020, 2023)
    month = random.randrange(1, 12)
    day = random.randrange(1, 18)
    date = str(year) + '-'
    if (month < 10):
        date += '0' + str(month)
    else:
        date += str(month)

    if (day < 10):
        date += '-' + '0' + str(day)
    else:
        date += '-' + str(day)
    return date

# Ask for how many DummyData entries there should be
f = open("dummy.sql", "w")

num = int(input("Enter number of records to be created: "))
f.write("INSERT INTO HOSPITALIZATION(StartDate, EndDate, HospitalID)\nVALUES ")
for i in range(num):
    # Hospital Insertion
    startDate = generateDate()
    modDate = startDate.split('-')
    modDate[2] = str(int(modDate[2]) + random.randrange(1, 10))
    if (int(modDate[2]) < 10):
        endDate = modDate[0] + '-' + modDate[1] + '-' + '0' + modDate[2]
    else:
        endDate = modDate[0] + '-' + modDate[1] + '-' + modDate[2]

    hospitalID = str(random.randrange(100, 5454))
    f.write("('" + startDate + "', " + "'" + endDate + "', " + hospitalID + ")")
    if(i < num - 1):
        f.write(",\n")


f.write(";\n\nINSERT INTO Patient(FName, LName, Gender, AgeCategoryID, VaccineID, TestID, HospitalizationID, PositiveID)\nVALUES ")
for i in range(num):
    # Patient Insertion
    firstNames = ["Bob", "Laurie", "Andy", "Billy", "Jaycie", "Quinn", "Niko", "Bill", "William", "Ahmad", "Miranda", "Kitty", "Peter", "Clark", "Diana", "Bruce"]
    lastNames = ["Chow", "Guy", "Banner", "Wayne", "Gunn", "Johnson", "Jones", "Munim", "Dude", "Chowder", "Le Clair", "White", "Pryde", "Parker", "Kent", "Prince", "Arthur"]
    genders = ['M', 'F', 'NB']

    vaccine = ["3", "4", "5", "6", "10", "11", "12", "13", "26", "27", "40", "41", "45", "46", "52", "60", "67", "69", "97", "101", "102", "104", "108", "111", "115", "118"]



    pid = str(random.randrange(1, 4900))
    hid = str(random.randrange(1, num))
    ageCategory = str(random.randrange(1, 15))
    test = str(random.randrange(1, 34545))
    f.write("('" + random.choice(firstNames) + "', " + "'" + random.choice(lastNames) + "', " + "'" + random.choice(genders) + "', " + ageCategory + ", " + random.choice(vaccine) + ", " + test + ", " + hid + ", " + pid + ")")
    if(i < num - 1):
        f.write(",\n")

f.write(";")
f.close()
