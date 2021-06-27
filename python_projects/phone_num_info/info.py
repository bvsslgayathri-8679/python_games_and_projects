import phonenumbers 
from test import *
from phonenumbers import geocoder,carrier

number="+918247879324"

ch_num=phonenumbers.parse(number,'CH')
print(geocoder.description_for_number(ch_num,"en"))

ser_num=phonenumbers.parse(number,"RO")

print(carrier.name_for_number(ser_num,"en"))




