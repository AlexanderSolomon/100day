# nesting is like having a folder system, a folder within a folder

# ACCESS dictionaries by keys (names)
# ACCESS list by index (positions)



#nesting
capitals = {
    "france": "paris",
    "Denmark": "copenhagen"
}

#nesting a list in a dictionary 
travel_log ={
    "Denmark" : ["copenhagen","aarhus","hillerød", "hvidovre"],
    "france": ["paris","lyon"]
}
# make it so the list has a discription 

#nesting a dictionary in a dictionary , 
# nested dictionary cities_visited
travel_log ={
    "Denmark" : ["copenhagen","aarhus","hillerød", "hvidovre"],
    "france": {"cities_visited" : ["paris","lyon"], "total_visits": 12}
}
    
#nesting a dictionary in a list , 
travel_log= [
    {
    "country": "france",
     "cities_visited" : ["paris","lyon"],
     "total_visits": 12
    },
    {
        "country": "Denmark",
        "cities_visited" : ["copenhagen","aarhus","hillerød", "hvidovre"], 
        "total_visits": 6
    }
]

