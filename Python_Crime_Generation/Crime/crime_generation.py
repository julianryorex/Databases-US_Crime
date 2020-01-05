import sys
sys.path.insert(0, "/Users/myfatduck/OneDrive/Programs/Databases/Databases-US_Crime/Python_Crime_Generation")
import util
import json
import random

TOTAL_CRIME_NUM = 550
JSON_DATA = ""
WEAPON_JSON = ""
INCAR_JSON = ""
V_O_JSON = ""
vo_index = []




def lookup_crime_type(index):
    crime_header = ("Population", "Violent", "Murder", "Rape", "Robbery", "Aggravated", "Property", "Burglary", "Larceny", "Motor")
    return crime_header[index]


def lookup_weapon_type(index):
    weapons = ('Handgun', 'Rifles', 'Shotguns', 'Other guns', 'Firearms (type not stated)', 'Knives or cutting instruments', 'Blunt objects', 'Personal weapons', 'Poison', 'Explosives', 'Fire', 'Narcotics', 'Drowning', 'Strangulation', 'Asphyxiation')
    return weapons[index-1]


def capitalize_states(state):
    cap_state = []
    if " " in state: # two words
        state = state.split(" ")
        for token in state:
            cap_state.append(token.capitalize())

        cap_state = " ".join(cap_state)
        return cap_state
    else:
        return state.capitalize()


def load_location():
    states = []
    file = util.find_all("location.json")
    with open(file, 'r') as location_file:
        global JSON_DATA
        JSON_DATA = json.load(location_file)
        for state in JSON_DATA.keys():
            states.append(capitalize_states(state))
    return states


def remove_location_num(state):
    global JSON_DATA
    crime_index = ""
    city = ""
    while(True):
        crime_info = JSON_DATA[state.upper()]
        length = len(crime_info) - 1
        randnum = random.randint(0, length)
        city_info = crime_info[randnum]
        city = next(iter(city_info))

        length = len(list(city_info.values())[0]) - 1
        randnum2 = random.randint(1, length)
        crime_index = randnum2
        crime_type = list(city_info.values())[0][randnum2]

        # now check if 0 or
        if crime_type == '0' or crime_type == "":
            #print("CONTINUE")
            continue

        number = list(JSON_DATA[state.upper()][randnum].values())[0][randnum2]
        if "," in number:
            number = number.replace(',', '')

        number = int(number) - 1
        list(JSON_DATA[state.upper()][randnum].values())[0][randnum2] = str(number)
        break

    return city, lookup_crime_type(crime_index)


def load_weapons():
    weapon = []
    global WEAPON_JSON
    file = util.find_all("weapons.json")
    with open(file, 'r') as weapon_json:
        WEAPON_JSON = json.load(weapon_json)


def generate_weapon():
    global WEAPON_JSON
    weapons = []
    if random.random() < 0.4: # some crime dont have weapons
        # generate an array of weapons

        for item in WEAPON_JSON:
            for key in item:
                weapons.append(key)

        while(True):
            length = len(WEAPON_JSON) - 1
            randnum = random.randint(0, length)
            weapon_object = WEAPON_JSON[randnum]
            wep_count = list(weapon_object.values())[0]

            if wep_count == '0' or wep_count == "":
                #print("CONTINUE")
                continue

            if "," in wep_count:
                wep_count = wep_count.replace(',', '')

            wep_count = int(wep_count) - 1
            o = {next(iter((WEAPON_JSON[randnum]))): str(wep_count)}
            WEAPON_JSON[randnum].update(o)
            return randnum + 1

    else:
        return "NULL"


def load_incar():
    global INCAR_JSON
    file = util.find_all("incarceration.json")
    with open(file, 'r') as incar_file:
        INCAR_JSON = json.load(incar_file)


def incar_gen(weapon):
    global INCAR_JSON
    # no incarceration if no weapon
    if weapon == "NULL":
        return "NULL"

    length = len(INCAR_JSON) - 1
    randnum = random.randint(0, length)
    return randnum


def load_victim_offender():
    global V_O_JSON
    file = util.find_all("victim_offender.json")
    with open(file, 'r') as vo_file:
        V_O_JSON = json.load(vo_file)


def vo_gen():
    global V_O_JSON
    global vo_index
    while(True):
        randnum = random.randint(0, len(V_O_JSON) - 1)
        if randnum in vo_index:
            continue
        else:
            vo_index.append(randnum)
            return V_O_JSON[randnum][0], V_O_JSON[randnum][1]


def crime_gen(states):
    st_len = len(states) - 1
    randnum = random.randint(0, st_len)
    random_state = states[randnum]
    city, crime_type = remove_location_num(random_state) # random_state
    year = 2016 # hardcorded because did not add a year type
    weapon = generate_weapon()
    incarceration = incar_gen(weapon)
    victim, offender = vo_gen()
    crime = [year, random_state, city, weapon, incarceration, victim, offender]
    return crime


def generate_crimes():
    # extract most json files
    # states is used to randomly choose a state
    states = load_location()
    load_weapons()
    load_incar()
    load_victim_offender()

    crime = []
    for loop in range(TOTAL_CRIME_NUM):
        crime.append(crime_gen(states))

    util.output_SQL("CRIME", crime, "/mysql/insertCrime.sql", True)


def main():
    generate_crimes()


main()
