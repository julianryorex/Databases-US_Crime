import sys
sys.path.insert(0, "/Users/myfatduck/OneDrive/Programs/Databases/Databases-US_Crime/Python_Crime_Generation")
import util
import json
import random


def generate_victim_offender():
    victims = []
    offenders = []
    final = []
    file_path = util.find_all("people.json")
    count = 0
    with open(file_path, "r") as people_json:
        people = json.load(people_json)
        for person in people:
            if person['Victim']:
                victims.append(person['SSN'])
            else:
                offenders.append(person['SSN'])
            count += 1
    util.process(count)

    # now lets make the connection between the two arrays.
    print(f"length of victims: {len(victims)}")
    print(f"length of offenders: {len(offenders)}")
    # length of victims is always larger than offenders (percentages)
    # therefore, we have a temp_offenders array that stores all deleted offenders
    # in case we run out of offenders to pair with victimes, hence the if stmt

    temp_offenders = []
    for victim in victims:
        length = len(offenders)-1

        if length < 0:
            l = len(temp_offenders)-1
            num = random.randint(0, l)
            offender = temp_offenders[num]
            temp_offenders.remove(temp_offenders[num])
            temp = [victim, offender]
            final.append(temp)

        else:
            num = random.randint(0, length)
            offender = offenders[num]
            temp_offenders.append(offenders[num])
            offenders.remove(offenders[num])
            temp = [victim, offender]
            final.append(temp)


    util.output_SQL("VICTIM_OFFENDER", final, "/mysql/insertVictimOffender.sql")
    util.output_json(final, "victim_offender.json")



def main():
    generate_victim_offender()

main()
