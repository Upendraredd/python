class queue(object):
    def __init__(self):
        self.queue=[]
    def isempty(self):
        return self.queue==[]
    def enqueue(self,data):
        self.queue.insert(0,data)
        return '{} added to queue'.format(data)
    def dequeue(self):
        return self.queue.pop()
    def sizequeue(self):
        return '{} size of queue'.format(len(self.queue))
    
if __name__=='__main__':
    q=queue()
    print(q.enqueue(1))
    print(q.enqueue(2))
    print(q.enqueue(3))
    print(q.enqueue(1))
    print(q.dequeue())
    print(q.dequeue())
    print(q.sizequeue())
    print(q.isempty())