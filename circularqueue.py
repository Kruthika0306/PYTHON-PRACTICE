class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = self.rear = -1

    def enqueue(self, data):
        if (self.rear + 1) % self.size == self.front:
            print("Queue Full")
            return

        if self.front == -1:
            self.front = 0

        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data

    def display(self):
        print(self.queue)


cq = CircularQueue(5)

cq.enqueue(10)
cq.enqueue(20)

cq.display()
