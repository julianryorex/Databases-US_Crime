import csv
import os
import json


'''
Gets absolute path from json file
'''
def import_path():
    with open("pass.json") as json_file:
        path = json.load(json_file)
        path = path['path']
        print(type(path))
        return path


'''
Extracts data from FBI crime csv files in Extracted Data.
:params int year: due to how the folders are structured, pass a year
'''
def extract_locations(year, abs_path):

    # os.chdir(f"{abs_path}/{year}")
    # current_directory = os.getcwd()

    print(f"{abs_path}/{year}/{year}.csv")
    with open(f"{abs_path}/{year}/{year}.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        state_stats = {}
        current_state = ""
        prev_state = ""
        city_stats_array = []

        for row in csv_reader:

            # skip header lines
            if(line_count < 4):
                line_count += 1
                continue

            state = row[0]
            city_stats = {}
            city = row[1]

            crime_header = ("Population", "Violent", "Murder", "Rape", "Robbery", "Aggravated", "Property", "Burglary", "Larceny", "Motor")
            rape = row[5] if row[4] == "" and year == 2016 else row[4]
            #rape = check_rape(row[5], row[6])
            crimes = [row[2], row[3], rape, row[6], row[7], row[8], row[9], row[10], row[11], row[12]]
            city_stats = { city : crimes }

            if state != "" and current_state == "" and prev_state == "": # initial
                current_state = state
                prev_state = state
            elif state != "": # new state
                state_stats[prev_state] = city_stats_array
                city_stats_array = []
                prev_state = state
                current_state = state
                # break if reaches footer
                if row[0] != "" and row[0][0].isdigit():
                    break
            else: # same state as prev
                state = current_state

            city_stats_array.append(city_stats)

            # print(f"Loop {line_count-4}")
            # print(f"Current state: {current_state}")
            # print(f"Previous state: {prev_state}")
            # print(f"State: {state}")
            # print(f"City: {city}\n")

            # limit
            # if(line_count > 400):
            #     break
            line_count += 1

        print(f"Processed {line_count} lines.")
        # print_dict(state_stats)
        return state_stats


'''
Pretty prints the final dictionary with all the necessary data.
:params dictionary dict: pass in a dictionary
'''
def print_dict(dict):
    for state, states in dict.items():
        print(f"State: {state}")
        for city in states:
            print(f"\tCity: {city}")


def print_all(list):
    for item in list:
        print_dict(item)


def main():
    abs_path = import_path()
    data = []
    year2016 = extract_locations(2016, abs_path)
    #year2017 = extract_locations(2017, abs_path)
    print_dict(year2016)


main()
