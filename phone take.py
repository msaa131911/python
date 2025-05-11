import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

number=input("Enter the number:")                              #Bangladesh
                                                               #Grameenphone
                                                             #('Asia/Dhaka',)


country_name=phonenumbers.parse(number,"ch")
print(geocoder.country_name_for_number(country_name,"en"))

sim_name=phonenumbers.parse(number,"ro")
print(carrier.name_for_number(sim_name,"en"))

timezone_name=phonenumbers.parse(number,"gb")
print(timezone.time_zones_for_number(timezone_name))
