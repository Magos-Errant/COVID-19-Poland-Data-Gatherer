from unidecode import unidecode
import re

target_day = 30
target_month = 11
target_year = 20





def DataFormatter(target_day, target_month, target_year):
    file_location = f"Y:\Fukuoka Research\Covid-19 polska\\{target_day}_{target_month}_{target_year}_wojewodztwa.csv"
    file_output = f"Y:\Fukuoka Research\Covid-19 polska\\All_wojewodztwa_normalized.csv"

    data_bucket = open(file_location, 'r')
    current_file = data_bucket.readlines()
    data_bucket.close()

    current_file = [line.strip() for line in current_file]
    current_file = current_file[1:]
    save = open(file_output, 'a+')



    d = {'œ': 's', '³': 'l', '¹': 'a', ',': '.', ';': ','}
    for line in current_file:

        for key in d.keys():
            line = line.replace(key, d[key])

        test = re.search('(t[0-9]+)', line)
        if test:
            line = line[:-3] + date
        normalized_line = unidecode(line) + '\n'
        save.write(normalized_line)

    save.close()



for i in range(24,target_day+1):
    date = str(f"{i}/{target_month}/20{target_year}")
    print(i)
    DataFormatter(i, target_month, target_year)


