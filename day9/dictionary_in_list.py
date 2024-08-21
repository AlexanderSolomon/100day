# You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries. 
# Your job is to create a function that can add new countries to this list.

# Write a function that will work with the following line of code on line 21 to add the entry for Brazil to the travel_log.

# add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
# DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

# Example Input
# Brazil
# 5
# ["Sao Paulo", "Rio de Janeiro"]
# Example Output
# I've been to Brazil 5 times.
# My favourite city was Sao Paulo.
new_country = "Brazil"
new_visits = 2
new_lists_of_cities = ["Sao Paulo", "Rio de Janeiro"] 

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

#print(travel_log)
print(travel_log[1].get("visits"))

# def add_new_country(country,visits,list_of_cities):
#     new_entry = {"country": country,
#                   "visits": visits,
#                   "cities": list_of_cities}
#     travel_log.append(new_entry)
#     print(travel_log)

# add_new_country(country=new_country,list_of_cities=new_lists_of_cities,visits=new_visits)