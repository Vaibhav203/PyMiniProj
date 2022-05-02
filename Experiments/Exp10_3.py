import collections

queue = collections.deque(["A","B","C"])
print(queue)

print("\nAdding 'D' to the left: ")
queue.appendleft("D")
print(queue)

print("\nRemoving front-most from the right: ")
queue.pop()
print(queue)

print("\nRotating: ")
queue.rotate()
print(queue)

print("\nExtendiing: ")
queue.extend('EFG')
print(queue)
