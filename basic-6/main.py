from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import ChainMap

def main():
    #Counter example
    #https://www.geeksforgeeks.org/counters-in-python-set-1/
    arr = [3,6,1,2,2,4,2,3,3,6,4,6,2,5,4,8,6,8,5,8,3,8,3,7,9,7,9,5,6,4,4,6,3,4,3,2,1,6,4,3,3,2,4,6,7,3,3]
    print(Counter(arr))

    ctr = Counter()
    ctr.update(arr)
    print(ctr)

    ctr.update([4,7,3,4,2,7,4,7,4,3,5,6,1,7,2,3,6,7,4,5,7,4,7,5,4,5,8,5])
    print(ctr)

    #OrderedDict
    #https://www.geeksforgeeks.org/ordereddict-in-python/?ref=lbp
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
    dd = defaultdict(lambda: "NA")
    dd["a"] = 5
    dd["b"] = 3
    dd["c"] = 2
    print(dd)
    print(dd["a"])
    print(dd["d"])

    #ChainMap
    #https://www.geeksforgeeks.org/chainmap-in-python/?ref=lbp
    


if __name__ == "__main__":
    main()