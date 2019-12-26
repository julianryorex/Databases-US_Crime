import sys
sys.path.insert(0, "/Users/myfatduck/OneDrive/Programs/Databases/Databases-US_Crime/Python_Crime_Generation")
import util
import csv


def generate_weapons():

    file_name = util.find_all("weapons.csv")
    with open(file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        weapons = []

        for row in csv_reader:
            if line_count == 0: # some glitch (weird UTF-8 symbol)
                weapon = row[0][1:]
            else:
                weapon = row[0]
            fatalities = row[1]
            temp = { weapon : fatalities}
            weapons.append(temp)
            line_count += 1

        util.process(line_count)
        return weapons



def main():

    weapon_data = generate_weapons()
    util.output_SQL("WEAPON", weapon_data, "/mysql/insertWeapons.sql")

main()
