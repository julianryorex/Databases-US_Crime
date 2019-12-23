import csv
import os
import pprint


current_directory = os.getcwd()
# print(f"Original: {current_directory}")

def extract_locations(year):

    os.chdir(f"../Extracted Data/{year}")
    current_directory = os.getcwd()


    with open(f"{current_directory}/{year}.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        crime_by_state = {}
        current_state = ""
        city_info_array = []
        for row in csv_reader:

            # skip header lines
            if(line_count < 4):
                line_count += 1
                continue

            # print(f"Current Row: {row}")

            state_stats = {}
            state = row[0]
            city = row[1]
            crime_header = ("Population", "Violent", "Murder", "Rape", "Robbery", "Aggravated", "Property", "Burglary", "Larceny", "Motor")
            rape = check_rape(row[5], row[6])
            crimes = [row[2], row[3], row[4], rape, row[7], row[8], row[9], row[10], row[11], row[12]]

            if(state != ""):
                current_state = state
                crime_by_state.update({ current_state : city_info_array})
                city_info_array = []

            state_stats.update({ city : crimes})
            city_info_array.append(state_stats)
            # print(city_info_array)


            line_count += 1
            # limit

        pprint(crime_by_state)

def check_rape(r1, r2):

    if(r1 == ""):
        return r2
    else:
        return r1


year = 2016
extract_locations(year)
