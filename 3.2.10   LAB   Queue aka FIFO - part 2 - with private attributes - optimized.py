#Code is with name-mangled - private (with the use of __) properties.

#Manage Error
class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.__queue = []
        
    def put(self,elem):
        self.__queue.append(elem)
        
    def get(self):
        if self.__queue:
            val = self.__queue[0]
            del self.__queue[0]
            return val
        else:
            raise QueueError
        
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        return len (self._Queue__queue) == 0 #to manually access a private attribute of the parent class
                                              #Optimized to return True or False directly

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

    
