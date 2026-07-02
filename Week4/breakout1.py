#1
"""
You're curating a large collection of NFTs for a digital art gallery, and your first task is to extract the names of these NFTs from a given list of dictionaries. Each dictionary in the list represents an NFT, and contains information such as the name, creator, and current value.

Write the extract_nft_names() function, which takes in this list and returns a list of all NFT names.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

Example Usage:

def extract_nft_names(nft_collection):
    pass

# Example usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))
Example Output:

['Abstract Horizon', 'Pixel Dreams', 'Future City']
['Crypto Kitty', 'Galactic Voyage']
['Golden Hour']



Understanding:
input: 
output: 

Planning:


Implementation:
"""
# def extract_nft_names(nft_collection):
#     for nft in nft_collection:
#         nft.names_append
        

# # Example usage:
# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
# ]

# nft_collection_2 = [
#     {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
#     {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
# ]

# nft_collection_3 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))

#2
"""
You're responsible for ensuring the quality of the NFT collection before it is displayed in the virtual gallery. One of your tasks is to review and debug the code that extracts the names of NFTs from the collection. A junior developer wrote the initial version of this function, but it contains some bugs that prevent it from working correctly.

Task:

Review the provided code and identify the bug(s).

Explain what the bug is and how it affects the output.

Refactor the code to fix the bug(s) and provide the correct implementation.

def extract_nft_names(nft_collection):
    nft_names = []
    for nft in nft_collection:
        nft_names += nft["name"]
    return nft_names
Example Usage:

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
]

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

nft_collection_3 = []

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))
Example Output:

['Abstract Horizon', 'Pixel Dreams']
['Golden Hour']
[]

Understanding:
input: List of dictionarys 
output: nft Names
edge-cases: 

Planning:
1.Review the provided code and identify the bug(s).
2.Explain what the bug is and how it affects the output.
3. Refactor the code to fix the bug(s) and provide the correct implementation.

Implementation:
"""
# def extract_nft_names(nft_collection):
#     nft_names = []
#     for nft in nft_collection:
#         nft_names.append(nft["name"])
#     return nft_names

# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2}
# ]

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
# ]

# nft_collection_3 = []

# print(extract_nft_names(nft_collection))
# print(extract_nft_names(nft_collection_2))
# print(extract_nft_names(nft_collection_3))

#3
"""
You have been tasked with identifying the most popular NFT creators in your collection. A creator is considered "popular" if they have created more than one NFT in the collection.

Write the identify_popular_creators() function, which takes a list of NFTs and returns a list of the names of popular creators.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def identify_popular_creators(nft_collection):
    pass
Example Usage:

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))
Example Output:

['ArtByAlex']
['SpaceArt']
[]

Understanding:
input: dictionary of nft collections
output: the list of popular creators
edge-case:
- no popular creator

Planning
1. Create a frequency map
2. iterate throught the nft collection
3. If the creater not in feq 


Implementation:
"""
def identify_popular_creators(nft_collection):
    creators = set()
    popular = []
    for nft in nft_collection:
        if nft["creator"] in creators:
            popular.append(nft["creator"])
        else:
            creators.add(nft["creator"])
    return popular

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

# print(identify_popular_creators(nft_collection)) 
# print(identify_popular_creators(nft_collection_2))
# print(identify_popular_creators(nft_collection_3))

#4
"""
You want to provide an overview of the NFT collection to potential buyers. One key statistic is the average value of the NFTs in the collection. However, if the collection is empty, the average value should be reported as 0.

Write the average_nft_value function, which calculates and returns the average value of the NFTs in the collection.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def average_nft_value(nft_collection):
    pass

Example Usage:
nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]
print(average_nft_value(nft_collection))

nft_collection_2 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
    {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
]
print(average_nft_value(nft_collection_2))

nft_collection_3 = []
print(average_nft_value(nft_collection_3))

Example Output:
5.7
9.15
0

Understanding:
input: list of dictionaries
output: average of values from each dictionary in the list

Planning:
1. iterate through the nft collection, add each value entry to a total sum
2. return total / list length

Implementation:
"""
def average_nft_value(nft_collection):
    if not nft_collection:
        return 0
    total = 0
    for nft in nft_collection:
        total += nft["value"]
    return total / len(nft_collection)
    
# nft_collection = [
#     {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
#     {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
#     {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
# ]
# print(average_nft_value(nft_collection))

# nft_collection_2 = [
#     {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9},
#     {"name": "Sunset Serenade", "creator": "SunsetArtist", "value": 9.4}
# ]
# print(average_nft_value(nft_collection_2))

# nft_collection_3 = []
# print(average_nft_value(nft_collection_3))

#5
"""
Some NFTs are grouped into collections, and each collection might contain multiple NFTs. Additionally, each NFT can have a list of tags describing its style or theme (e.g., "abstract", "landscape", "modern"). You need to search through these nested collections to find all NFTs that contain a specific tag.

Write the search_nft_by_tag() function, which takes in a nested list of NFT collections and a tag to search for. The function should return a list of NFT names that have the specified tag.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def search_nft_by_tag(nft_collections, tag):
    pass
    
Example Usage:
nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))


Example Output:
['Urban Jungle', 'City Lights']
['Golden Hour', 'Sunset Serenade']
[]

Understanding:
inptut: A list of List dictionary
output: list of names that has a specifiied tag

Planning:
1. Ceate a list of names
2. Iterate through the dictionary of lists
3. find the  speficic tag
4. reutrn the name of specific tag

Implementation:
"""
def search_nft_by_tag(nft_collections, tag):
    ans = []
    for collection in nft_collections:
        for nft in collection:
            if tag in nft["tags"]:
                ans.append(nft["name"])
                
    return ans
    
nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

#print(search_nft_by_tag(nft_collections, "landscape"))
#print(search_nft_by_tag(nft_collections_2, "sunset"))
#print(search_nft_by_tag(nft_collections_3, "modern"))

#6
"""
NFTs are processed in a queue that follows First-In, First-Out (FIFO). Given a list of NFT names in their initial queue order, return the order in which they are processed.

Write the process_nft_queue() function, which takes a list of NFTs. The function should return a list of NFT names in the order they were processed.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def process_nft_queue(nft_queue):
    pass
    
Example Usage:
nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))
Example Output:

['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']
['Golden Hour', 'Sunset Serenade', 'Ocean Waves']
['Crypto Kitty', 'Galactic Voyage']

Understanding:
input: queue of dictionaries
ouput: list of the names in order

Planning
1. popleft until the queue is empty
2/ append to list
3. return the list

Implementation:
"""

from collections import deque
def process_nft_queue(nft_queue):
    queue = deque(nft_queue)
    result = []
    while queue:
        result.append(queue.popleft()["name"])
    return result

nft_queue = [
    {"name": "Abstract Horizon", "processing_time": 2},
    {"name": "Pixel Dreams", "processing_time": 3},
    {"name": "Urban Jungle", "processing_time": 1}
]
print(process_nft_queue(nft_queue))

nft_queue_2 = [
    {"name": "Golden Hour", "processing_time": 4},
    {"name": "Sunset Serenade", "processing_time": 2},
    {"name": "Ocean Waves", "processing_time": 3}
]
print(process_nft_queue(nft_queue_2))

nft_queue_3 = [
    {"name": "Crypto Kitty", "processing_time": 5},
    {"name": "Galactic Voyage", "processing_time": 6}
]
print(process_nft_queue(nft_queue_3))


['Abstract Horizon', 'Pixel Dreams', 'Urban Jungle']
['Golden Hour', 'Sunset Serenade', 'Ocean Waves']
['Crypto Kitty', 'Galactic Voyage']

#7
"""
You want to ensure that NFTs are added in a balanced way. For example, every "add" action must be properly closed by a corresponding "remove" action.

Write the validate_nft_actions() function, which takes a list of actions (either "add" or "remove") and returns True if the actions are balanced, and False otherwise.

A sequence of actions is considered balanced if every "add" has a corresponding "remove" and no "remove" occurs before an "add".

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def validate_nft_actions(actions):
    pass

Example Usage:
actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))

Example Output:
True
True
False

Understanding:
input: list of add or remove actions
output: boolean representing validity

Planning
dictionary mapping "remove" to "add"
add element to stack if it is "add"
pop from the stack if it is "remove"
if the stack is empty return true

Implementation:
"""

def validate_nft_actions(actions):
    stack = []
    
    for act in actions:
        if act == 'add':
            stack.append(act)
        elif act == 'remove':
            if not stack:
                return False 
            stack.pop() 
            
    return len(stack) == 0

actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))
