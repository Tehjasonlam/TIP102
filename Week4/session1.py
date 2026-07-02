# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None
        
# x = Node(2)
# y = Node(3)
# x.next = y
# print(x.value)

class Node:
    def __init__(self,name):
        self.name = name
        self.next = None
            
student1 = Node("alice")
student2 = Node("bob")
student3 = Node("carol")

student1.next = student2
student2.next = student3
