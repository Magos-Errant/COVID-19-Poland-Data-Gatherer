import re

dupa = "dupa zachodniopomorskie,457,2.7,39,5,34,t32"
matches = re.search('(t[0-9]+)', dupa)

print(matches.group(1))