import math

#1

pi = 22 / 7
type(pi)

#for is a special word in python thus cannot be assigned a variable


principal_amount = int(input("Principal amount: "))
rate_of_interest = int(input("Rate of interest: "))
time = int(input("Time: "))


pa = principal_amount
roi = rate_of_interest
t = time

simple_interest = pa * roi * t / 100



#2


def represent(a, b):
    return f"{a} is represented by {b}"

represent(145, 'o')



def pond(r):
    pi = 3.14
    area = pi * (r ** 2)
    water = int(area / 1.4)

    return area, water

pond(84)


def speed(d, t):
    s = int(d / (t * 60))

    return s

speed(490, 7)


#3

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

no_of_members = len(justice_league)
new_members = ['Batman', 'Nightwing']
justice_league.extend(new_members)
justice_league.remove('Wonder Woman')
justice_league.insert(0, 'Wonder Woman')
justice_league.remove("Green Lantern")
justice_league.insert(4, 'Green Lantern')
justice_league = ['Cyborg', 'Shazam', 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']
justice_league.sort()


#4

def determine():
    height = float(input("Enter your height in metres: "))
    weight = int(input("Enter your weight in kilograms: "))

    BMI = weight / (height ** 2)

    if BMI >= 30:
        a = 'Obesity'

    elif 25 <= BMI <= 29:
        a = 'Overweight'

    elif 18.5 <=BMI < 25:
        a = 'Normal'

    elif BMI < 18.5:
        a = 'Underweight'

    return a

determine()          


def find(s):
    city = input("Enter the name of the city to find its country: ")

    a = ''
    for x in s:
        if city in s[x]:
            a = x


    return city + ' is in ' + a
    


countries = {
   'Australia' : ['Sydney', 'Melbourne', 'Brisbane', 'Perth'],
   'UAE' : ['Dubai', 'Abu Dhabi', 'Sharjah, Ajman'],
   'India' : ['Mumbai', 'Bangalore', 'Chennai', 'Delhi']
   
   }

find(countries)


countries = {
   'Australia' : ['Sydney', 'Melbourne', 'Brisbane', 'Perth'],
   'UAE' : ['Dubai', 'Abu Dhabi', 'Sharjah, Ajman'],
   'India' : ['Mumbai', 'Bangalore', 'Chennai', 'Delhi']
   
   }

def both(s):

    city1 = input("Enter the first city: ")
    city2 = input("Enter the 2nd city: ")

    a = 'Not Found'

    for x in s:
        if city1 in s[x] and city2 in s[x]:
            a = 'Both cities are in ' + x

        else:
            a = "They don't belong to the same country"
    return a 

both(countries)


#5

#roll_dice

import random

num_rolls = 20
six_count = 0
one_count = 0
two_sixes_in_a_row = 0
previous_roll = None

for i in range(num_rolls):
    roll = random.randint(1, 6)
    print("Roll", i + 1, ":", roll)
    if roll == 6:
        six_count += 1
        if previous_roll == 6:
            two_sixes_in_a_row += 1
    elif roll == 1:
        one_count += 1
    previous_roll = roll

print("\nStatistics:")
print("Number of times 6 was rolled:", six_count)
print("Number of times 1 was rolled:", one_count)
print("Number of times two 6s were rolled in a row:", two_sixes_in_a_row)


#jumping jacks

total_jumping_jacks = 100
completed_jacks = 0
set_size = 10

while completed_jacks < total_jumping_jacks:
    completed_jacks += set_size
    print("Completed", completed_jacks, "jumping jacks.")
    tired = input("Are you tired? (yes/no): ").lower()
    if tired in ("yes", "y"):
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip in ("yes", "y"):
            break
        else:
            print(total_jumping_jacks - completed_jacks, "jumping jacks remaining.")
    elif completed_jacks == total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break

print("You completed a total of", completed_jacks, "jumping jacks.")


#6

#friends

friends = ["John", "Samantha", "Michael", "Emily", "Robert"]
name_lengths = [(name, len(name)) for name in friends]
print(name_lengths)


#expenses


my_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}


my_total = sum(my_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your total expenses:", my_total)
print("Partner's total expenses:", partner_total)


if my_total > partner_total:
    print("You spent more.")
else:
    print("Your partner spent more.")


max_difference = 0
max_difference_category = ""

for category in my_expenses:
    difference = abs(my_expenses[category] - partner_expenses[category])
    if difference > max_difference:
        max_difference = difference
        max_difference_category = category

print("Category with the most difference:", max_difference_category, "Difference:", max_difference)


#7

import csv

with open('student_marks.csv', 'r') as file:
    reader = csv.DictReader(file)
    students = list(reader)

for student in students:
    marks = [int(student[subject]) for subject in student if subject not in ['Name']]
    student['Total_Marks'] = sum(marks)
    student['Average'] = student['Total_Marks'] / len(marks)

with open('student_marks_updated.csv', 'w', newline='') as file:
    fieldnames = students[0].keys()
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)



#8

class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
    
    def get_info(self):
        return f"{self.name}, Age: {self.age}, Gender: {self.gender}, Super Power: {self.super_power}, Weapon: {self.weapon}"
    
    def is_leader(self):
        return self.name == "Captain America"

super_heroes = [
    Avenger("Captain America", 100, "Male", "Super Strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 35, "Male", "Fighting Skills", "Bow and Arrows")
]

for hero in super_heroes:
    print(hero.get_info(), "- Leader:", hero.is_leader())


# Base Class: MobilePhone
class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def make_call(self, number):
        print("Calling " + str(number) + "...")

    def receive_call(self, caller):
        print("Receiving a call from " + str(caller) + "...")

    def take_picture(self):
        print("Taking a picture with the " + str(self.rear_camera) + " rear camera.")

# Child Class: Apple
class Apple(MobilePhone):
    def __init__(self, model, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

# Child Class: Samsung
class Samsung(MobilePhone):
    def __init__(self, model, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        super().__init__(screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage)
        self.model = model

# Creating Apple object
iphone_14 = Apple(
    "iPhone 14", 
    "Touch Screen", 
    "5G", 
    False, 
    "12MP", 
    "48MP", 
    "6GB", 
    "128GB"
)

# Creating Samsung object
galaxy_s23 = Samsung(
    "Galaxy S23", 
    "Touch Screen", 
    "5G", 
    True, 
    "16MP", 
    "64MP", 
    "8GB", 
    "256GB"
)

# Testing Apple object
iphone_14.make_call("123-456-7890")
iphone_14.take_picture()
print("Model: " + iphone_14.model + ", RAM: " + iphone_14.ram)

# Testing Samsung object
galaxy_s23.receive_call("987-654-3210")
galaxy_s23.take_picture()
print("Model: " + galaxy_s23.model + ", Dual Sim: " + str(galaxy_s23.dual_sim))


