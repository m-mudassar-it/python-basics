# Stack implementation using list

stack = []  # empty stack

def push(item):
    stack.append(item)
    print(f"Pushed {item} -> {stack}")

def pop():
    if not is_empty():
        item = stack.pop()
        print(f"Popped {item} -> {stack}")
        return item
    else:
        print("Stack is empty! Cannot pop.")
        return None

def peek():
    if not is_empty():
        print(f"Top element is {stack[-1]}")
        return stack[-1]
    else:
        print("Stack is empty! Nothing to peek.")
        return None

def is_empty():
    return len(stack) == 0


# Example usage
push(10)
push(20)
push(30)
peek()
pop()
pop()
pop()
pop()   # trying to pop from empty stack
