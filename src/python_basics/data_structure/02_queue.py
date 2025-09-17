# Queue implementation using list

queue = []  # empty queue

def enqueue(item):
    queue.append(item)
    print(f"Enqueued {item} -> {queue}")

def dequeue():
    if not is_empty():
        item = queue.pop(0)   # remove first element
        print(f"Dequeued {item} -> {queue}")
        return item
    else:
        print("Queue is empty! Cannot dequeue.")
        return None

def peek():
    if not is_empty():
        print(f"Front element is {queue[0]}")
        return queue[0]
    else:
        print("Queue is empty! Nothing to peek.")
        return None

def is_empty():
    return len(queue) == 0


# Example usage
enqueue(10)
enqueue(20)
enqueue(30)
peek()
dequeue()
dequeue()
dequeue()
dequeue()   # trying to dequeue from empty queue
