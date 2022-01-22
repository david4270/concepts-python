# Quicksort

class QuickSort:
    def __init__(self,list):
        self.list = list
        self.quickSort(0,len(list)-1)
    
    def quickSort(self,left,right):
        pivot = self.SelectAndShuffle(left,right)
        #print(left,pivot,right)
        if(pivot > left):
            self.quickSort(left,pivot-1)
        if(pivot < right):
            self.quickSort(pivot+1,right)
    
    def SelectAndShuffle(self,left,right):
        ls = left
        for i in range(left+1,right+1):
            if(self.list[i] <= self.list[left]):
                ls = ls+1
                tmp = self.list[i]
                self.list[i] = self.list[ls]
                self.list[ls] = tmp
        tmp = self.list[left]
        self.list[left] = self.list[ls]
        self.list[ls] = tmp
        return ls


# Mergesort

# Heapsort

# Radix sort

# Selection sort

# Bubble sort

# Insertion sort

# Counting sort

