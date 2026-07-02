#Set 1

#P1
# def welcome():
# 	print("Welcome to The Hundred Acre Wood!")

# welcome()

#P2
# def greeting(name):
# 	print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

# greeting("Michael")
# greeting("Winnie the Pooh")

#P3
# def print_catchphrase(character):
#     if character == "Pooh":
#         print("Oh bother!")
#     elif character == "Tigger":
#         print("TTFN: Ta-ta for now!")
#     elif character == "Eeyore":
#         print("Thanks for noticing me.")
#     elif character == "Christopher Robin":
#         print("Silly old bear.")
#     else:
#         print(f"Sorry! I don't know {character}'s catchphrase!")
        

# character = "Pooh"
# print_catchphrase(character)

# character = "Piglet"
# print_catchphrase(character)

#P4
# def get_item(items, x):
#     if 0 <= x < len(items):
#         return items[x]
#     return None
    
# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# print(get_item(items, 2))

# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 5
# print(get_item(items, 5))

#P5
# def sum_honey(hunny_jars):
#     total = 0
#     for i in hunny_jars:
#         total += i
#     return total

# hunny_jars = [2, 3, 4, 5]
# print(sum_honey(hunny_jars))  # 14

# hunny_jars = []
# print(sum_honey(hunny_jars))  # 0

#P6
# def doubled(hunny_jars):
#     doubled_jars = []
#     for i in hunny_jars:
#         doubled_jars.append(i * 2)
 
#     return doubled_jars

# hunny_jars = [1, 2, 3]
# print(doubled(hunny_jars))

#P7
# def count_less_than(race_times, threshold):
#     races = 0
#     for i in race_times:
#         if i < threshold:
#             races += 1
    
#     return races

# race_times = [1, 2, 3, 4, 5, 6]
# threshold = 4
# print(count_less_than(race_times, threshold))

# race_times = []
# threshold = 4
# print(count_less_than(race_times, threshold))

#P8
# def print_todo_list(task):
#     print("Pooh's To Dos:")
#     for i in range(len(task)):
#         print(f"{i + 1}. {task[i]}")
     

# task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)

# task = []
# print_todo_list(task)

#P9
# def can_pair(item_quantities):
#     for i in item_quantities:
#         if i % 2 != 0:
#             return False
#     return True 

# item_quantities = [2, 4, 6, 8]
# print(can_pair(item_quantities))

# item_quantities = [1, 2, 3, 4]
# print(can_pair(item_quantities))

# item_quantities = []
# print(can_pair(item_quantities))

#P10
# def split_haycorns(quantity):
#     split_corn = []
#     for i in range(1, quantity + 1):
#         if quantity % i == 0:
#             split_corn.append(i)
#     return split_corn

# quantity = 6
# print(split_haycorns(quantity))

# quantity = 1
# print(split_haycorns(quantity))

#P11
# def tiggerfy(s):
#     tigger = ""
#     tiger = "tiger"
#     for char in s:
#         if char.lower() not in tiger:
#             tigger += char
#     return tigger

# s = "suspicerous"
# print(tiggerfy(s))

# s = "Trigger"
# print(tiggerfy(s))

# s = "Hunny"
# print(tiggerfy(s))

#P12
def locate_thistles(items):
    for i in range(0, len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j]:
                return [i, j]
    return []


items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
print(locate_thistles(items))

items = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items))