from unidecode import unidecode
import re

file_location = "Y:\Fukuoka Research\Covid-19 polska\\24_11_20_wojewodztwa.csv"
file_output = "Y:\Fukuoka Research\Covid-19 polska\\24_11_20_wojewodztwa_normalized.csv"
time = "24.11.2020"

data_bucket = open(file_location, 'r')
current_file = data_bucket.readlines()
data_bucket.close()

current_file = [line.strip() for line in current_file]

save = open(file_output, 'w')


d = {'œ': 's', '³': 'l', '¹': 'a', ',': '.', ';': ','}
for line in current_file:
    for key in d.keys():
        line = line.replace(key, d[key])
    test = re.search('(t[0-9]+)', line)
    if test:
        line = line[:-3] + time
    normalized_line = unidecode(line) + '\n'
    save.write(normalized_line)

save.close()




