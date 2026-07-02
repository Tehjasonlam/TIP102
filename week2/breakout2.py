#1
"""
Imagine you are working on a wildlife conservation database. Write a function named most_endangered() that returns the species with the highest conservation priority based on its population.

The function should take in a list of dictionaries named species_list as a parameter. Each dictionary represents data associated with a species, including its name, habitat, and wild population. The function should return the name of the species with the lowest population.

If there are multiple species with the lowest population, return the species with the lowest index.

def most_endangered(species_list):
    pass
Example Usage:

species_list = [
    {"name": "Amur Leopard",
     "habitat": "Temperate forests",
     "population": 84
    },
    {"name": "Javan Rhino",
     "habitat": "Tropical forests",
     "population": 72
    },
    {"name": "Vaquita",
     "habitat": "Marine",
     "population": 10
    }
]

Understanding:
input: A list of the dictionarys with the name, habitat, and population of the species
output: Lowest Population species Name

Plan:
Edge cases:
1. List is empty => return "" 
2. Two items with the same min population => return item with lowest index
3. Create min population variable and name variable
4. Create a loop to iterate over the list and store the min and name
5. Return the name


Implementation:
"""
# import math
# def most_endangered(species_list):
#     if not species_list:
#         return ""

#     min_population = math.inf
#     min_name = ""
    
#     for species in species_list:
#         if species["population"] < min_population:
#             min_population = species["population"]
#             min_name = species["name"]

    
#     return min_name
        

# species_list = [
#     {"name": "Amur Leopard",
#      "habitat": "Temperate forests",
#      "population": 84
#     },
#     {"name": "Javan Rhino",
#      "habitat": "Tropical forests",
#      "population": 73
#     },
#     {"name": "Vaquita",
#      "habitat": "Marine",
#      "population": 10
#     }
# ]

# print(most_endangered(species_list))

#2
"""
As part of conservation efforts, certain species are considered endangered and are represented by the string endangered_species. Each character in this string denotes a different endangered species. You also have a record of all observed species in a particular region, represented by the string observed_species. Each character in observed_species denotes a species observed in the region.

Your task is to determine how many instances of the observed species are also considered endangered.

Note: Species are case-sensitive, so "a" is considered a different species from "A".

Write a function to count the number of endangered species observed.

def count_endangered_species(endangered_species, observed_species):
    pass
Example Usage:

endangered_species1 = "aA"
observed_species1 = "aAAbbbb" {"aAb"}

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  
Example Output:

3 # `a` and `A` are endangered species. `a` appears once, and `A` twice.
0

Understanding:
input: The endagered species and the observeed species
output: The number of endangered species observed

Plan:
1. endangered species => set
2. count
3. Create a for loop going through each species in the obsered species
4. If the species in the endangered set, then add count += 1
5. Return count
Implementation:
"""
def count_endangered_species(endangered_species, observed_species):
    endangered_set = set(endangered_species)
    count = 0
    
    for species in observed_species:
        if species  in endangered_set:
            count += 1
            
    return count

endangered_species1 = "aA"
observed_species1 = "aAAbbbb"

endangered_species2 = "z"
observed_species2 = "ZZ"

print(count_endangered_species(endangered_species1, observed_species1)) 
print(count_endangered_species(endangered_species2, observed_species2))  


#3
"""
In a wildlife research station, each letter of the alphabet represents a different observation point laid out in a single row. Given a string station_layout of length 26 indicating the layout of these observation points (indexed from 0 to 25), you start your journey at the first observation point (index 0). To make observations in a specific order represented by a string observations, you need to move from one point to another.

The time taken to move from one observation point to another is the absolute difference between their indices, |i - j|.

Write a function that returns the total time it takes to visit all the required observation points in the given order with one movement.

def navigate_research_station(station_layout, observations):
  pass
Example Usage:

station_layout1 = "pqrstuvwxyzabcdefghijklmno"
observations1 = "wildlife"

station_layout2 = "abcdefghijklmnopqrstuvwxyz"
observations2 = "cba"

print(navigate_research_station(station_layout1, observations1))  
print(navigate_research_station(station_layout2, observations2))

Understanding:
input:
output:

Plan:

Implementation:
"""
#4
"""
In your work with a wildlife conservation database, you have two lists: observed_species and priority_species. The elements of priority_species are distinct, and all elements in priority_species are also in observed_species.

Write a function prioritize_observations() that sorts the elements of observed_species such that the relative ordering of items in observed_species matches that of priority_species. Species that do not appear in priority_species should be placed at the end of observed_species in ascending order.

def prioritize_observations(observed_species, priority_species):
  pass
Example Usage:

observed_species1 = ["🐯", "🦁", "🦌", "🦁", "🐯", "🐘", "🐍", "🦑", "🐻", "🐯", "🐼"]
priority_species1 = ["🐯", "🦌", "🐘", "🦁"]  

observed_species2 = ["bluejay", "sparrow", "cardinal", "robin", "crow"]
priority_species2 = ["cardinal", "sparrow", "bluejay"]

print(prioritize_observations(observed_species1, priority_species1))
print(prioritize_observations(observed_species2, priority_species2)) 

Expected Output:

["🐯", "🐯", "🐯", "🦌", "🐘", "🦁", "🦁", "🐍", "🐻", "🐼", "🦑"]
["cardinal", "sparrow", "bluejay", "crow", "robin"]

Understanding:
input:
output:

Plan:

Implementation:
"""
#5
"""
You are given a 0-indexed integer array species_populations of even length, where each element represents the population of a particular species in a wildlife reserve.

As long as species_populations is not empty, you must repetitively:

Find the species with the minimum population and remove it.
Find the species with the maximum population and remove it.
Calculate the average population of the two removed species.
The average of two numbers a and b is (a+b)/2.

For example, the average of 200 and 300 is (200+300)/2=250.

Return the number of distinct averages calculated using the above process.

Note that when there is a tie for a minimum or maximum population, any can be removed.

def distinct_averages(species_populations):
  pass
Example Usage:

species_populations1 = [4,1,4,0,3,5]
species_populations2 = [1,100]

print(distinct_averages(species_populations1))
print(distinct_averages(species_populations2)) 
Example Output:

2
Example 1 Explanation:
1. Remove 0 and 5, and the average is (0 + 5) / 2 = 2.5. Now, nums = [4,1,4,3].
2. Remove 1 and 4. The average is (1 + 4) / 2 = 2.5, and nums = [4,3].
3. Remove 3 and 4, and the average is (3 + 4) / 2 = 3.5.
Since there are 2 distinct numbers among 2.5, 2.5, and 3.5, we return 2.

1
Example 2 Explanation:
There is only one average to be calculated after removing 1 and 100, 
so we return 1.

Understanding:
input:
output:

Plan:

Implementation:
"""
#6
"""
You are given a string ecosystem_data that consists of digits and lowercase English letters. The digits represent the observed counts of various species in a protected ecosystem.

You will replace every non-digit character with a space. For example, "f123de34g8hi34" will become " 123 34 8 34". Notice that you are left with some species counts that are separated by at least one space: "123", "34", "8", and "34".

Return the number of unique species counts after performing the replacement operations on ecosystem_data.

Two species counts are considered different if their decimal representations without any leading zeros are different.

def count_unique_species(ecosystem_data):
  pass
Example Usage:

ecosystem_data1 = "f123de34g8hi34"
ecosystem_data2 = "species1234forest234"
ecosystem_data3 = "x1y01z001"

print(count_unique_species(ecosystem_data1))
print(count_unique_species(ecosystem_data2))
print(count_unique_species(ecosystem_data3))


Understanding:
input:
output:

Plan:

Implementation:
"""
#7
"""
Understanding:
input:
output:

Plan:

Implementation:
"""
#8
"""
Understanding:
input:
output:

Plan:

Implementation:
"""