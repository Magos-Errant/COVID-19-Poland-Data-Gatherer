from unidecode import unidecode
import csv

file_location = "Y:\Fukuoka Research\Covid-19 polska\\24_11_20_wojewodztwa.csv"
file_output = "Y:\Fukuoka Research\Covid-19 polska\\24_11_20_wojewodztwa_normalized.csv"

data_bucket = open(file_location, 'r')
current_file = data_bucket.readlines()
data_bucket.close()

current_file = [line.strip() for line in current_file]

save = open(file_output, 'w')


d = {'œ': 's', '³': 'l', '¹': 'a'}
for line in current_file:
    for key in d.keys():
        line = line.replace(key, d[key])
    normalized_line = unidecode(line) + '\n'
    save.write(normalized_line)

save.close()




