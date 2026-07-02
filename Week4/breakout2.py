"""
Your day consists of various tasks, each requiring a certain amount of time. To optimize your workday, you want to find a pair of tasks that fits exactly into a specific time slot you have available. 
You need to identify if there is a pair of tasks whose combined time matches the available slot.

Given a list of integers representing the time required for each task and an integer representing the available time slot, 
write a function that returns True if there exists a pair of tasks that exactly matches the available time slot, and False otherwise.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def find_task_pair(task_times, available_time):
  pass

Example Usage:
task_times = [30, 45, 60, 90, 120]
available_time = 105
print(find_task_pair(task_times, available_time))

task_times_2 = [15, 25, 35, 45, 55]
available_time = 100
print(find_task_pair(task_times_2, available_time))

task_times_3 = [20, 30, 50, 70]
available_time = 60
print(find_task_pair(task_times_3, available_time))

Example Output:
True
True
False

Understanding:
Input: Task times is a list of integers. Available time is an integer.
Output: True or False


Planning
1. Iterate through the task times
2. Subtract it from our available time 
3. See if the remaining time is in the rest of the list 
4. If we find a pair, return True
5. If not, return False


Implementation:
"""
# def find_task_pair(task_times, available_time):
#   seen = set()
#   for task in task_times:
#     remaining_time = available_time - task
#     if remaining_time in seen:
#       return True
#     else:
#       seen.add(task)
#   return False 
  



# task_times = [30, 45, 60, 90, 120]
# available_time = 105
# print(find_task_pair(task_times, available_time))

# task_times_2 = [15, 25, 35, 45, 55]
# available_time = 100
# print(find_task_pair(task_times_2, available_time))

# task_times_3 = [20, 30, 50, 70]
# available_time = 60
# print(find_task_pair(task_times_3, available_time))


#2
"""
You work with clients across different time zones and often have gaps between your work sessions. 
You want to minimize these gaps to make your workday more efficient. You have a list of work sessions, 
each with a start time and an end time. Your task is to find the smallest gap between any two consecutive work sessions.

Given a list of tuples where each tuple represents a work session with a start and end time 
(both in 24-hour format as integers, e.g., 1300 for 1:00 PM), 
write a function to find the smallest gap between any two consecutive work sessions. The gap is measured in minutes.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for 
why you believe your solution has the stated time and space complexity.

def find_smallest_gap(work_sessions):
  pass
Example Usage:

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))
Example Output:

60
30
15

Understanding:
Input: A list of sessions 
Output:The Smallest Gap in mins 
Edge cases: 0 size = 3
Planning
1. if the work seesion empty return None
2. Iterate through the sessions
3. Change the time to mins to get the min output
4. get min gap
5.return min gap

Implementation:
"""


def find_smallest_gap(work_sessions):

    min_gap = float('inf')
    
    for i in range(len(work_sessions)-1):
        prev_end = work_sessions[i][1]
        curr_start = work_sessions[i+1][0]
        
        prev_end_min = (prev_end // 100) * 60 + (prev_end % 100)
        curr_start_min = (curr_start // 100) * 60 + (curr_start % 100)
        # (time // 100) * 60 + (time % 100)
        
        gap = curr_start_min - prev_end_min
        min_gap = min(min_gap, gap)

    return min_gap

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))
    
  # for i in range(len(work_sessions)-1) :
  #   start_time = [i+1][0]
  #   end_time = [i][1]
  
"""
def find_smallest_gap(work_sessions):
    minDiff = float('inf')

    for i in range(len(work_sessions)-1):
        nextTime = (work_sessions[i+1][0]//100) * 60 + work_sessions[i+1][0] %100
        currTime = (work_sessions[i][1]//100) * 60 + work_sessions[i][1] %100
        minDiff = min(minDiff, nextTime-currTime)

    return minDiff

work_sessions = [(900, 1100), (1300, 1500), (1600, 1800)]
print(find_smallest_gap(work_sessions))

work_sessions_2 = [(1000, 1130), (1200, 1300), (1400, 1500)]
print(find_smallest_gap(work_sessions_2))

work_sessions_3 = [(900, 1100), (1115, 1300), (1315, 1500)]
print(find_smallest_gap(work_sessions_3))
"""

        



"""
You travel frequently and need to keep track of your expenses. You categorize your expenses into different categories such as "Food," "Transport," "Accommodation," etc. At the end of each month, you want to calculate the total expenses for each category to better understand where your money is going.

Given a list of tuples where each tuple contains an expense category (string) and an expense amount (float), write a function that returns the expense categories and the total expenses for each category. Additionally, the function should return the category with the highest total expense.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

def calculate_expenses(expenses):
  pass
Example Usage:

expenses = [("Food", 12.5), ("Transport", 15.0), ("Accommodation", 50.0),
            ("Food", 7.5), ("Transport", 10.0), ("Food", 10.0)]
print(calculate_expenses(expenses))

expenses_2 = [("Entertainment", 20.0), ("Food", 15.0), ("Transport", 10.0),
              ("Entertainment", 5.0), ("Food", 25.0), ("Accommodation", 40.0)]
print(calculate_expenses(expenses_2))

expenses_3 = [("Utilities", 100.0), ("Food", 50.0), ("Transport", 75.0),
              ("Utilities", 50.0), ("Food", 25.0)]
print(calculate_expenses(expenses_3))
Example Output:

({'Food': 30.0, 'Transport': 25.0, 'Accommodation': 50.0}, 'Accommodation')
({'Entertainment': 25.0, 'Food': 40.0, 'Transport': 10.0, 'Accommodation': 40.0}, 'Food')
({'Utilities': 150.0, 'Food': 75.0, 'Transport': 75.0}, 'Utilities')

Understanding:
Find the total expense for each catogory and return catogory with highest expense
Input: tuple
Output:  dictionary with catagory and total expense, then catogory with max expense
Planning
make dic if not already in dic add into , if there , we add the expense


Implementation:
"""

"""


Understanding:


Planning


Implementation:
"""
"""


Understanding:


Planning


Implementation:
"""

"""


Understanding:


Planning


Implementation:
"""

"""


Understanding:


Planning


Implementation:
"""

"""


Understanding:


Planning


Implementation:
"""