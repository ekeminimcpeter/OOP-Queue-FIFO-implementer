#Code is with name-mangled - private (with the use of __) properties.
#Use private (__private_var) when you want strict encapsulation and prevent external modifications


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
        if not self._Queue__queue: #to manually access a private attribute of the parent class
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

    
