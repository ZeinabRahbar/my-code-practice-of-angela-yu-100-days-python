#dictionary creation
programming_dict = {
    "Bug": "error",
    "Function": "add modularity",
    }

print(f"whole programming_dict: {programming_dict}")

#retrieving an item of a dictionary
print(programming_dict["Bug"])

#Adding new items to dictionary

programming_dict["Bug"] = "doing something over and over"
print(f"whole programming_dict: {programming_dict}")

#Edit an item in dictionary
programming_dict["Loop"] = "A moth in your computer"
print(f"whole programming_dict: {programming_dict}")

#Loop through a dictionary

for key in programming_dict:
    print(key)
    print(programming_dict[key])

#Wipe an axisting dictionart
empty_dict = {}
programming_dict = {}
print(f"whole programming_dict: {programming_dict}")

###############################################################
#Day 9.1

student_scores = {
     "Harry": 81,
     "Ron": 78,
     "Hemione": 99,
     "Draco": 74,
     "Neville": 62
     }

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score>90:
        student_grades[student] = "Outstanding"
    elif score>80:
        student_grades[student] = "Exceeds Expectations"
    elif score>70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
print(student_grades)

#############################################################
#Day 9.2
#Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
    }

#Nesting a list in dictionary

travel_log = {
    "France": {"cities_visited":["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Berlin", "Hamburg", "Stuttgart"] , "total_visits": 5}   
    }

#Nesting a dict in a list

travel_log = [
    { "country": "France",
      "cities_visited":["Paris", "Lille", "Dijon"],
      "total_visits": 12
      
        },
    { "country": "Germany",
      "cities_visited":["Berlin", "Hamburg", "Stuttgart"],
      "total_visits": 5
      
        }
    ]


#add to the dict func
print(travel_log)

def add_new_country(country_visited, times_visited, cities_visited):
        new_country = {}
        new_country["country"] = country_visited
        new_country["cities_visited"] = cities_visited
        new_country["total_visits"] = times_visited
        travel_log.append(new_country)

add_new_country("Russia", ["Moscow", "Saint Petersburg"],2)
print(travel_log)
