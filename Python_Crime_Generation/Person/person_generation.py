import sys
sys.path.insert(0, "/Users/myfatduck/OneDrive/Programs/Databases/Databases-US_Crime/Python_Crime_Generation")
import util
import csv


def import_first_names():
    male_first_names = []
    female_first_names = []
    file = util.find_all("people.txt")
    with open(file, "r") as person_file:
        for line in person_file:
            data = line.split("\t")
            print(data)
            for index, token in enumerate(data):
                if token.isalpha():
                    if index == 1:
                        female_first_names.append(token)
                    else:
                        male_first_names.append(token)

    first_names = {"Male": male_first_names, "Female": female_first_names}
    return first_names

def import_last_names():
    last_names_array = []
    file = util.find_all("last_names.txt")
    with open(file, "r") as last_names:
        for line in last_names:
            data = line.split("\t")
            last_names_array.append(data[0].capitalize())

    return last_names_array


def output_names(first_names):
    util.output_json(first_names, "first_names.json")

def output_last_names(last_names):
    util.output_json(last_names, "last_names.json")



def generate_person():
    genders = ["M", "F"]
    races = {"American Indian": 0.5, "Alaskan Native": 0.4, "Asian": 4.8, "African American": 12.6, "Hispanic": 16.3, "Native Hawaiian": 0.1, "Other Pacific Islanders": 0.1, "White": 72.4, "Other":6.4}
    first_names = import_first_names()
    output_names(first_names)
    last_names = import_last_names()
    output_last_names(last_names)







def main():
    generate_person()

main()
