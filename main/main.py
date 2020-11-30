from unidecode import unidecode
import re

date = "30/11/2020"

target_day = date[:2]
target_month = date[3:5]
target_year = date[-2:]

def DataFormatter(target_day, target_month, target_year):
    file_location = f"Y:\Fukuoka Research\Covid-19 polska\\{target_day}_{target_month}_{target_year}_wojewodztwa.csv"
    file_output = f"Y:\Fukuoka Research\Covid-19 polska\\{target_day}_{target_month}_{target_year}_wojewodztwa_normalized.csv"


    data_bucket = open(file_location, 'r')
    current_file = data_bucket.readlines()
    data_bucket.close()

    current_file = [line.strip() for line in current_file]

    save = open(file_output, 'w')


    d = {'œ': 's', '³': 'l', '¹': 'a', ',': '.', ';': ','}
    for line in current_file:
        for key in d.keys():
            line = line.replace(key, d[key])
        change_id = re.search('id', line)
        if change_id:
            line = line[:-2] + "Date"

        test = re.search('(t[0-9]+)', line)
        if test:
            line = line[:-3] + date
        normalized_line = unidecode(line) + '\n'
        save.write(normalized_line)

    save.close()

DataFormatter(target_day, target_month, target_year)


