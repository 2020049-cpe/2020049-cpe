# Camille S. Munoz
# Student ID: 2020049
# Section: CPE2A

try:
    print("Welcome to UBLC Canteen")
    Name_049 = str(input('Student Name: '))
    Idno_049 = str(input('Student ID: '))
    Year_049 = str(input('Year: '))
    Course_049 = str(input('Course: '))
    Section_049 = str(input('Section: '))

except Exception as error:
    print(error)
info = {
    'Name': Name_049,
    'ID': Idno_049,
    'year': Year_049,
    'course': Course_049,
    'section': Section_049,
    'money': 150
    }