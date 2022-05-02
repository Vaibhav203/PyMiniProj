# Vaibhav Bhaliya   68   SeitB-B3
def add(queue):
    print("\nAdding 'Sun' to the left: ")
    queue.appendleft("Sun")
    print(queue)

def popfront(queue):
    print("\nRemoving front-most from the right: ")
    queue.pop()
    print(queue)

def rotate(queue):
    print("\nRotating: ")
    queue.rotate()
    print(queue)

def extend(queue):
    print("\nExtendiing: ")
    queue.extend('Sun')
    print(queue)
