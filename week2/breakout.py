
"""
Understand:




Plan:




Implement:



"""
"""""
Given two lists of strings artists and set_times of length n, write a function lineup() that maps each artist to their set time.

An artist artists[i] has set time set_times[i]. Assume i <= 0 < n and len(artists) == len(set_times).

def lineup(artists, set_times):
    pass

Example Usage:

artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

artists2 = []
set_times2 = []

print(lineup(artists1, set_times1))
print(lineup(artists2, set_times2))

Example Output:

{"Kendrick Lamar": "9:30 PM", "Chappell Roan": "5:00 PM", "Mitski": "2:00 PM", "Rosalía": "7:30 PM"}
{}

Understand: 
Inputs: artists1 and set_times1 array
Outputs: Dictionary, artists as keys, settimes as values
Edge cases: If both arrays empty, return empty dictionary

Plan:
Create a Dictionary 
Then, go through each list artist and set times and add it to the dictionary 
for loop



"""

# def lineup(artists, set_times):
#     dict = {}

#     if (len(artists) == 0 and len(set_times) == 0):
#         return dict
#     for i in range(0, len(artists), 1):
#         ##dict[artists[i]] = set_times[i]
#         dict.update({artists[i]: set_times[i]})
#     return dict

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))



""""
You are designing an app for your festival to help attendees have the best experience possible! As part of the application, 
users will be able to easily search their favorite artist and find out the day, time, and stage the artist is playing at. 
Write a function get_artist_info() that accepts a string artist and a dictionary festival_schedule mapping artist's names to 
dictionaries containing the day, time, and stage they are playing on. Return the dictionary containing the information about the given artist.

If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

def get_artist_info(artist, festival_schedule):
    pass

Example Usage:

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

print(get_artist_info("Blood Orange", festival_schedule)) 
print(get_artist_info("Taylor Swift", festival_schedule))  

Example Output:

{'day': 'Friday', 'time': '9:00 PM', 'stage': 'Main Stage'}
{'message': 'Artist not found'}

Understand: 
Inputs: Artist and whole festival schedule
Outputs: The specific artist's information that's found in the festival schedule
Edge Case: If the artist searched for does not exist in festival_schedule, return the dictionary {"message": "Artist not found"}.

Plan:
def get_artist_info(String artist, Dictionary festival schedule):

    if (artist not in festival schedule) {
        "message": "Artist not found"
    }

    print statement of artist info
        

"""

# def get_artist_info(artist, festival_schedule):
#     if artist in festival_schedule:
#         return festival_schedule[artist]
#     else:
#         return {'message': 'Artist not found'}
        

# festival_schedule = {
#     "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
#     "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
#     "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
#     "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
# }

# print(get_artist_info("Kali Uchis", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  

"""""
A dictionary ticket_sales is used to map ticket type to number of tickets sold. Return the total number of tickets of all types sold.

def total_sales(ticket_sales):
    pass

Example Usage:

ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}

print(total_sales(ticket_sales))

Example Output:

4500

Understand - Tri
Input: Dictionary of ticket_sales
Output: Return the total number of tickets sold
Edgecase: if ticket sales are negative return error.

Plan - Ishaan
def function:
    total = 0
    my_dict.values()
    for loop that iterates through my_dict:
        if (values[i] < 0):
            return "error negative number"
        else: 
            add to total
    
        
Implement - Meghashree


"""
# def total_sales(ticket_sales):
#     total = 0
#     ticket_sales.values()
#     for value in ticket_sales.values():
#         if value < 0:
#             return -1
#         else:
#             total += value
#     return total


# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 1, "3-Day Pass": 2500}

# print(total_sales(ticket_sales))

"""""

You're given strings vip_passes representing the types of guests that have VIP passes, 
and guests representing the guests you have at the music festival. 
Each character in guests is a type of guest you have. You want to know how many of the guests you have are also VIP pass holders.

Letters are case sensitive, so "a" is considered a different type of guest from "A".

Here is the pseudocode for the problem. Implement this in Python and explain your implementation step-by-step.

1. Create an empty set called vip_set.
2. For each character in vip_passes, add it to vip_set.
3. Initialize a counter variable to 0.
4. For each character in guests:
   * If the character is in vip_set, increment the count by 1.
5. Return the count.

def num_VIP_guests(vip_passes, guests):
    pass

Example Usage:

vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))

Example Output:

3
0

Understand - Meghashree

Plan - Hayley:

1. Create an empty set called vip_set.
2. For each character in vip_passes, add it to vip_set.
3. Initialize a counter variable to 0.
4. For each character in guests:
   * If the character is in vip_set, increment the count by 1.
5. Return the count.

Implement - Ishaan


"""

def num_VIP_guests(vip_passes, guests):
    vip_set = set()
    for char in vip_passes:
        vip_set.add(char)
    count = 0
    for char in guests:
       if char in vip_set:
        count = count + 1
    return count


vip_passes1 = "aA"
guests1 = "aAAbbbb"

vip_passes2 = "z"
guests2 = "ZZ"

print(num_VIP_guests(vip_passes1, guests1))
print(num_VIP_guests(vip_passes2, guests2))