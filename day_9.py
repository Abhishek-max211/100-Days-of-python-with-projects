# Day 9
# Dictionaries in Python
dictionary={"name": "Abhishek"
            ,"Age":16,
            "Skill":"Python"
}
print(dictionary)
print(dictionary["name"])
print(dictionary["Age"])
print(dictionary["Skill"])

# How to add dictionary
dictionary["name"]="Abhi"
print(dictionary["name"])

# Nesting lists and dictionary
travel_log={
    "France":{
        "city_visited":["Paris","Lille","Dijon"],
        "total_visits":12,
    },
    "Germany":{
        "city_visited":["Berlin","Hamburg"],
        "total_visits":5,
    },
}
print(travel_log["Germany"]["city_visited"][0])
print("Thank you for visiting")