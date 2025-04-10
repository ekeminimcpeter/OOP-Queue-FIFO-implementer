#Code is with protected (with the use of _) properties.
#Use protected (_protected_var) when you want subclasses to access it but warn external users.


class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self._queue = []
        
    def put(self,elem):
        self._queue.append(elem)
        
    def get(self):
        if self._queue:
            val = self._queue[0]
            del self._queue[0]
            return val
        else:
            raise QueueError
        
class SuperQueue(Queue):
    def __init__(self):
        super().__init__() # Use super() instead of calling Queue.__init__(self)

    def isempty(self):
        if not self._queue: 
            return True
        else:
            return False

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

    
