#1
"""
You are managing a social media platform and need to ensure that posts are properly formatted. Each post must have balanced and correctly nested tags, such as () for mentions, [] for hashtags, and {} for links. You are given a string representing a post's content, and your task is to determine if the tags in the post are correctly formatted.

A post is considered valid if:

Every opening tag has a corresponding closing tag of the same type.
Tags are closed in the correct order.
def is_valid_post_format(posts):
  pass

Example Usage:
print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

Example Output:
True
True
False

Understanding:
input: is a string of 
output: Booleon True or false

Planning:


Implementation:
"""
# def is_valid_post_format(posts):
#   pairs = {')': '(', ']': '[', '}': '{'}
#   stack = []
    
#   for char in posts:
#     if char in pairs:
#       stack.append(char)
#     elif char in pairs.values():
#       stack.pop(char)
            
#     # If the stack is empty, all tags were properly closed and nested
#     return not stack
    
# print(is_valid_post_format("()"))
# print(is_valid_post_format("()[]{}"))
# print(is_valid_post_format("(]"))

#2
"""
On your platform, comments on posts are displayed in the order they are received. However, 
for a special feature, you need to reverse the order of comments before displaying them. 
Given a queue of comments represented as a list of strings, reverse the order using a stack.

def reverse_comments_queue(comments):
  pass
Example Usage:

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))
Example Output:

['Thanks for sharing.', 'Love it!', 'Great post!']
['Well written.', 'Interesting read.', 'First!']

Understanding:
input: list of strings
output: list of strings (reversed)
edge-cases: empty list

Planning:
1. initalized the stack
2. while loop thru the list
3. poop the value from the list into the stack
4. return the list

Implementation:
"""
# def reverse_comments_queue(comments):
#   result = []
  
#   while len(comments) != 0:
#       result.append(comments.pop())
#   return result
    
  

# print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

# print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

#3
"""
As part of a new feature on your social media platform, 
you want to highlight post titles that are symmetrical, 
meaning they read the same forwards and backwards when ignoring spaces, punctuation, 
and case. Given a post title as a string, use a new algorithmic technique 
the two-pointer method to determine if the title is symmetrical.

def is_symmetrical_title(title):
  pass
Example Usage:

print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 
Example Output:

True
False

Understanding:
input: string
output: bool true if symestrical
edge-case: white space, punctioation, capital letters

Planning



Implementation:


"""

# def is_symmetrical_title(title):
#   title = title.replace(" ","").lower()
#   left = 0
#   right = len(title) - 1
#   while left < right:
#     if title[left] != title[right]:
#       return False
#     left += 1
#     right -= 1
#   return True

# print(is_symmetrical_title("A Santa at NASA"))
# print(is_symmetrical_title("Social Media")) 

#4
"""
You track your daily engagement rates as a list of integers, sorted in non-decreasing order. To analyze the impact of certain strategies, you decide to square each engagement rate and then sort the results in non-decreasing order.

Given an integer array engagements sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Your Task:

Read through the existing solution and add comments so that everyone in your pod understands how it works.
Modify the solution below to use the two-pointer technique.
def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result

Example Usage:

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
Example Output:

[0, 1, 9, 16, 100]
[4, 9, 9, 49, 121]

Understanding:
Planning
Implementation:
"""
# def engagement_boost(engagements):
#   squared_engagements = []
    
#   for i in range(len(engagements)):
#     squared_engagement = engagements[i] * engagements[i]
#     squared_engagements.append((squared_engagement, i))
    
#     squared_engagements.sort(reverse=True)
    
#     result = [0] * len(engagements)
#     position = len(engagements) - 1
    
#     for square, original_index in squared_engagements:
#         result[position] = square
#         position -= 1
    
#     return result

def engagement_boost(engagements):
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result
print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11])) 
  
#5
"""
You want to make sure your posts are clean and professional. Given a string post of lowercase and uppercase English letters, you want to remove any pairs of adjacent characters where one is the lowercase version of a letter and the other is the uppercase version of the same letter. Keep removing such pairs until the post is clean.

A clean post does not have two adjacent characters post[i] and post[i + 1] where:

post[i] is a lowercase letter and post[i + 1] is the same letter in uppercase or vice-versa.
Return the clean post.

Note that an empty string is also considered clean.

def clean_post(post):
  pass

Example Usage:
print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 

Example Output:
post

s
Understanding:
inptut: string
output: a string of a clean post

Planning:
1:iterate through to look for lower-upper pairs
2.remove if pair found
3.return clean string

Implementation:
"""
def clean_post(post):
    stack = []
    for char in post:
        if stack:
            if stack[-1] != char:
                if stack[-1].lower() == char.lower():
                    stack.pop()
                    continue  # Skip to the next character in the loop
                    
        stack.append(char)
        
    return "".join(stack)
        
        
print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s"))    

#6
"""
Understanding:
Planning
Implementation:
"""

#7
"""
Understanding:
Planning
Implementation:
"""