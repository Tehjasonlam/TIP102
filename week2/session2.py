#create a set
empty_dict = {}
empyt_set = set()

nums = {1, 2, 3, 4, 5}
#print(nums)

# for num in numns:
#     print(num)

my_nums = {2, 3, 4}
#my_nums.remove(5)

my_nums.discard(5)
print(my_nums)

s1 = set({"A"})
s2 = set({"a", "A", "A" "b", "b"})
union = s1 & s2
print(union)


students_a = {"Alice", "Bob", "Charlie"}
students_b = {"Charlie", "Bob", "Eve"}

union = students_a | students_b
intersection = students_a & students_b
print(intersection)
diffa = students_a - students_b
diffb = students_b - students_a

sym = students_a ^ students_b
print(sym)