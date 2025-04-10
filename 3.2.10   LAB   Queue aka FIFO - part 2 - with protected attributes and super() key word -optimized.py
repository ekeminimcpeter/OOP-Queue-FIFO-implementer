#Code is with protected (with the use of _) properties.


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
        return len(self._queue) == 0 #optimized to return True or False directly
         

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

    
