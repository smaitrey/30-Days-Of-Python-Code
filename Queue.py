from collections import deque

def main():
    # 1. Initialize a queue.
    q = deque()
    
    # 2. Push new elements.
    q.append(5)
    q.append(13)
    q.append(8)
    q.append(6)
    
    # 3. Check if the queue is empty.
    if not q:
        print("Queue is empty!")
        return

    # 4. Pop an element from the front.
    q.popleft()
    
    # 5. Get the first element.
    print(f"The first element is: {q[0]}")
    
    # 6. Get the last element.
    print(f"The last element is: {q[-1]}")
    
    # 7. Get the size of the queue.
    print(f"The size is: {len(q)}")

if __name__ == "__main__":
    main()


