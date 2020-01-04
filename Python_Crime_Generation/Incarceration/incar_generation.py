import sys
sys.path.insert(0, "/Users/myfatduck/OneDrive/Programs/Databases/Databases-US_Crime/Python_Crime_Generation")
import util
import json
import random

TOTAL_INCAR_NUM = 100

def import_prisons():
    file = util.find_all("prison_list.txt")
    prisons = []
    with open(file, "r") as prison_list:
        for row in prison_list:
            row = row.split("\t")
            name = row[0]
            state = row[1].strip("\n")
            temp = [name, state]
            prisons.append(temp)

    return prisons


def generate_time():
    num = random.random()
    if num < 0.6: # month
        months = random.randint(1, 11)
        return f"{months} months"

    else:
        if num < 0.7:
            years = random.randint(1, 25)
        elif num < 0.9:
            years = random.randint(25, 50)
        else:
            return "Life"

        return f"{years} years"


def generate_incar():
    final = []
    prisons = import_prisons()
    for i in range(TOTAL_INCAR_NUM):
        length = len(prisons) - 1
        index = random.randint(0, length)
        temp = [generate_time(), prisons[index][0], prisons[index][1]]
        final.append(temp)
    util.output_json(final, "incarceration.json")

    for prison in final:
        del(prison[-1])

    util.output_SQL("INCARCERATION", final, "/mysql/insertIncar.sql", True)






def main():
    generate_incar()

main()
