stack = []
stack.append(1)
stack.append(2)
stack.append(3)

#print(stack)

popped = stack.pop()

print(popped)
print(stack)

stack.pop()
print(stack)

print(stack[-1])

from collections import deque

queue = deque()
queue.append("Messi")
queue.append("Ronaldo")
queue.append("Neymar")

print(queue)

messi = popped = queue.popleft()
print(messi)

print(queue)
print(queue.popleft())



def is_valid_parentheses(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in pairs.values():      # openers
            stack.append(c)
        elif c in pairs:             # closers
            if not stack or stack.pop() != pairs[c]:
                return False
    return not stack

print(is_valid_parentheses(")"))