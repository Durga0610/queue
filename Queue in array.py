max_size=int(input("Enter the size:"))
front=-1
rear=-1
queue=[0]*max_size
def enqueue():
    global front,rear
    if rear==max_size-1:
        print("\n queue is full")
    elif front==-1 and rear==-1:
        front=rear=0
        num=int(input("Enter the element:"))
        queue[rear]=num
    else:
        rear+=1
        num=int(input("Enter the element to insert:"))
        queue[rear]=num
def dequeue():
    global front,rear
    if front==-1 and rear==-1:
        print("queue is empty")
    elif front==rear:
        print(queue[front],"is deleted")
        front=rear=-1
    else:
        print("The deleted element from the queuq is ",queue[front])
        front+=1
def display():
     if front==-1 and rear==-1:
        print("queue is empty! Nothing to display")
     else:
        print("Element in the queue's are:")
        for i in range(front,rear+1):
            print(queue[i],end='\t')
        print()
def peek():
    if front==-1 and rear==-1:
        print("queue is empty! Nothing to display")
    else:
        print(f"Element in the element in the queue is {queue[front]}")
while True:
    choice=int(input("Enter the choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        peek()
    elif choice==5:
        exit()
    else:
        print("Invalid choice")
    
    
