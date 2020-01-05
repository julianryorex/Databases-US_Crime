import sys
sys.path.insert(0, "/Users/myfatduck/OneDrive/Programs/Databases/Databases-US_Crime/Python_Crime_Generation")
import util
import random

# number of people to generate
TOTAL_PERSON_NUM = 10000



def import_first_names():
    male_first_names = []
    female_first_names = []
    file = util.find_all("people.txt")
    with open(file, "r") as person_file:
        for line in person_file:
            data = line.split("\t")
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


def output_json(first_names, last_names, people):
    util.output_json(first_names, "first_names.json")
    util.output_json(last_names, "last_names.json")
    util.output_json(people, "people.json")



def choose_race(races):
    ranks = []
    current = 0.00
    for race, percentage in races.items():
        temp = [race, current, (current + percentage)]
        ranks.append(temp)
        current = current + percentage + 0.01

    num = float('{0:.2f}'.format(random.uniform(0, 113)))
    for item in ranks:
        if item[1] <= num and num <= item[2]:
            return item[0] # race

    return "white"


# this will output to output_SQL in util.
# format must be a list of dictionaries.
# a dictionary will be a person with: gender, race, ssn, names,
def generate_person(genders, races, first_names, last_names):
    people = []
    ssn = 1 # initial SSN
    for i in range(TOTAL_PERSON_NUM):
        gender = genders[random.randint(0,1)]
        race = choose_race(races)
        fname = random.choice(first_names['Male']) if gender == 'M' else random.choice(first_names['Female'])
        lname = random.choice(last_names)
        num = random.random()
        victim = True if num < 0.6 else False
        offender = not victim
        person = {"SSN": str(ssn).zfill(9), "gender": gender, "race": race, "Firstname": fname, "Lastname": lname, "Victim": victim, "Offender": offender}
        people.append(person)
        ssn += 1

    return people


def generation_reqs():
    genders = ["M", "F"]
    races = {"American Indian": 0.5, "Alaskan Native": 0.4, "Asian": 4.8, "African American": 12.6, "Hispanic": 16.3, "Native Hawaiian": 0.1, "Other Pacific Islanders": 0.1, "White": 72.4, "Other":6.4}
    first_names = import_first_names()
    last_names = import_last_names()
    people = generate_person(genders, races, first_names, last_names)


    util.output_SQL("PERSON", people, "/mysql/insertPeople.sql")
    output_json(first_names, last_names, people)






def main():
    generation_reqs()

main()
