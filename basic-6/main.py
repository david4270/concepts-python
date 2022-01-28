from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import ChainMap
from collections import namedtuple
from collections import deque
import heapq

from numpy import get_array_wrap

def main():
    #Counter example
    #https://www.geeksforgeeks.org/counters-in-python-set-1/
    print("Counter example")
    arr = [3,6,1,2,2,4,2,3,3,6,4,6,2,5,4,8,6,8,5,8,3,8,3,7,9,7,9,5,6,4,4,6,3,4,3,2,1,6,4,3,3,2,4,6,7,3,3]
    print(Counter(arr))

    ctr = Counter()
    ctr.update(arr)
    print(ctr)

    ctr.update([4,7,3,4,2,7,4,7,4,3,5,6,1,7,2,3,6,7,4,5,7,4,7,5,4,5,8,5])
    print(ctr)

    #OrderedDict
    #https://www.geeksforgeeks.org/ordereddict-in-python/?ref=lbp
    print("OrderedDict example")
    od = OrderedDict()
    od['a'] = 5    
    od['b'] = 3    
    od['c'] = 2    
    od['d'] = 4
    print(od)

    od.pop('c')
    print(od)

    od['c'] = 1
    print(od)

    #DefaultDict
    #https://www.geeksforgeeks.org/defaultdict-in-python/?ref=lbp
    print("DefaultDict example")
    dd = defaultdict(lambda: "NA")
    dd["a"] = 5
    dd["b"] = 3
    dd["c"] = 2
    print(dd)
    print(dd["a"])
    print(dd["d"])

    #ChainMap
    #https://www.geeksforgeeks.org/chainmap-in-python/?ref=lbp
    print("Chainmap example")
    d1 = {'a': 1, 'b': 2}
    d2 = {'c': 6, 'd': 5}
    d3 = {'e': 3, 'f': 7}
    d4 = {'a': 4, 'e': 2}
    cm = ChainMap(d1,d2,d3,d4)
    print(cm.maps)
    print(list(cm.keys()))
    print(list(cm.values()))
    
    d5 = {'g':4, 'f':3}
    c1 = cm.new_child(d5)
    print(c1.maps)
    print(list(c1.keys()))
    print(list(c1.values()))
    print(c1['a'])

    c1.maps = reversed(c1.maps)
    print(c1['a'])

    #Namedtuple
    #https://www.geeksforgeeks.org/namedtuple-in-python/?ref=lbp
    print("NamedTuple example")
    FootyPlayer = namedtuple('FootyPlayer',['name','age','position','league','team','kitnum'])
    StevieB = FootyPlayer('Steven Bergwijn',24,'LW','EPL','Tottenham Hotspur',23)
    Sonny = FootyPlayer('Heung-Min Son',29,'LF','EPL','Tottenham Hotspur',7)
    Harry = FootyPlayer('Harry Kane',28,'ST','EPL','Tottenham Hotspur',10)
    Bryan = FootyPlayer('Brian Gil',20,'LW','EPL','Tottenham Hotspur',11)
    Lucas = FootyPlayer('Lucas Moura',29,'RW','EPL','Tottenham Hotspur',27)
    Hojbjerg = FootyPlayer('Pierre-Emile Hojbjerg',26,'CDM','EPL','Tottenham Hotspur',5)
    Skippy = FootyPlayer('Oliver Skipp',21,'CDM','EPL','Tottenham Hotspur',29)
    Hugo = FootyPlayer('Hugo Lloris',35,'GK','EPL','Tottenham Hotspur',1)
    Royal = FootyPlayer('Emerson Royal',23,'RB','EPL','Tottenham Hotspur',12)
    Reggie = FootyPlayer('Sergio Reguilon',25,'LB','EPL','Tottenham Hotspur',3)
    Dier = FootyPlayer('Eric Dier',28,'CB','EPL','Tottenham Hotspur',15)
    Romero = FootyPlayer('Christian Romero',23,'CB','EPL','Tottenham Hotspur',4)
    Davinson = FootyPlayer('Davinson Sanchez',25,'CB','EPL','Tottenham Hotspur',6)
    Japhet = FootyPlayer('Japhet Tanganga',22,'CB','EPL','Tottenham Hotspur',25)
    Davies = FootyPlayer('Ben Davies',28,'LCB','EPL','Tottenham Hotspur',33)
    Doherty = FootyPlayer('Matt Doherty',30,'RWB','EPL','Tottenham Hotspur',2)
    Winky = FootyPlayer('Harry Winks',25,'CM','EPL','Tottenham Hotspur',8)
    sess = ['Ryan Sessegnon',21,'LWB','EPL','Tottenham Hotspur',19]
    Sess = FootyPlayer._make(sess)
    gollini = {'name':'Pierluigi Gollini','age':26,'position':'GK','league':'EPL','team':'Tottenham Hotspur','kitnum':22}

    print("What is Sonny's kit number?:",Sonny.kitnum)
    print("What is Skippy's name?:",Skippy[0])
    print("What is Stevie B's position?:",getattr(StevieB,'position'))
    print("How old is Sess?:",Sess.age)
    print(Lucas._asdict())
    print(FootyPlayer(**gollini)) #Return namedtuple from dictionary
    print(Bryan._fields)
    print(Romero._replace(name='Cuti Romero'))

    #Deque
    #https://www.geeksforgeeks.org/deque-in-python/
    print("Deque example")
    queue = deque([1,3,2,5])
    print(queue)
    queue.append(4)
    print(queue)
    queue.appendleft(6)
    print(queue)
    queue.pop()
    print(queue)
    queue.popleft()
    print(queue)
    queue.insert(2,4) #put 4 in index 2
    print(queue)
    queue.remove(5)
    print(queue)
    del queue

    queue = deque([1,6,4,6,4,4,3,3,2,4,6,4,1,2,3])
    print(queue)
    print("Count of 4 in deque is",queue.count(4))
    queue.insert(1,4) #put 4 in index 1
    print(queue)
    print("Count of 4 in deque is",queue.count(4))
    print("Between index 3 and 10, 6 occurs first at",queue.index(6,3,10))

    queue.extend([4,2,5,3]) #extend at right
    queue.extendleft([1,4,6,2,4]) #extend at left
    print(queue)
    print("Count of 4 in deque is",queue.count(4))
    queue.rotate(-3) #rotate left by 3
    print(queue)
    queue.reverse() #reverse
    print(queue)

    #Heap Queue
    #https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/
    print("Heap queue example")

    #UserDict


    #UserList


    #UserString


     



if __name__ == "__main__":
    main()