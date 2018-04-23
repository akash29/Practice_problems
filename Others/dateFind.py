import re

str_sample = "15/11/2012','15/11/12',15.11.2012','15-11-12' '15th March 1999','15th March 99, October 21, 2014"

vals = re.findall(r'\d+[/|-]\d+[/|-]?\d+',str_sample)
print(vals)
val2 = re.findall(r'[O|ok]ctober\s+\d+,\s+\d+',str_sample)
print(val2)