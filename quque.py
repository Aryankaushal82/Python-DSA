queue = []
def enqueue(queue, num):

    queue.append(num)



def dequeue(queue):

    return queue.pop(0)

    

def size(queue):

    return len(queue)

    

def top(queue):

    return queue[0]