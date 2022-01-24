"""
<<Big-OH, Big-Omega and Big-Theta>>
1) Big-OH - upper bound of complexity of algorithm
    f(n) = O(g(n)) if and only if
    O(g(n)) = {f(n) there exists a positive constants c and n_0 such that
                0 <= f(n) <= cg(n) for all n >= n_0}
2) Big-Omega - lower bound of complexity of algorithm
    f(n) = Ω(h(n)) if and only if
    Ω(h(n)) = {f(n) there exists a positive constants c_1 and n_1 such that
                0 <= c_1 h(n) <= f(n) for all n >= n_1}
3) Big-Theta
    f(n) = θ(g(n)) if and only if
    θ(g(n)) = {f(n) there exists a positive constants c_1, c_2 and n_0 such that
                0 <= c_1 g(n) <= f(n) <= c_2 g(n) for all n >= n_0}
"""

"""
<<Recurrence - Master Method>>
Let a >= 1, b > 1, f(n) is some function
Recurrence T(n) = aT(n/b) +f(n) has solution:
1) f(n) = O(n^(log_b(a) - ε)) for ε > 0
    then T(n) = θ(n^(log_b(a)))
2) f(n) = θ(n^(log_b(a)))
    then T(n) = θ( (n^(log_b(a))) * log(n) )
2-1) f(n) = θ( n^(log_b(a)) * log^k(n) )
    then T(n) = θ( (n^(log_b(a))) * log^(k+1)(n) )
3) f(n) = Ω(n^(log_b(a) + ε)) for ε > 0
    and af(n/b) <= cf(n) for 0 < c < 1
    then T(n) = θ(f(n))
"""

"""
<<Quicksort>>

<Worst-case scenario>
[               ] n
[] 1 [          ] n-1
[] [] [         ] n-2
      ...
[][][] ... [][][] 1

T(n) = T(n-1) + θ(n)
     = T(n-2) + θ(n-1) + θ(n)
     = T(n-3) + θ(n-2) + θ(n-1) + θ(n)
     ...
     = θ(1) + ... + θ(n-1) + θ(n)
     = θ(∑ k) =  θ(n^2)

<Best-case scenario>
[              ] n
[     ] [      ] n/2
[  ][  ][  ][  ] n/4
       ...
T(n) = 2T(n/2) + θ(n)
     = θ(n logn)

<Average-case scenario>
[              ] n
[          ][  ] 3n/4 & n/4
      ...
T(n) = T(3n/4) + T(n/4) + θ(n)
     = θ(n logn)
"""

from heapq import heapify
import sys
#sys.setrecursionlimit(10000)

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
        # For each i from left+1 to right, if arr[i] <= arr[left],
        # move ls (pivot) by 1, and swap arr[i] and arr[ls]
        for i in range(left+1,right+1):
            if(self.list[i] <= self.list[left]):
                ls = ls+1
                tmp = self.list[i]
                self.list[i] = self.list[ls]
                self.list[ls] = tmp
        
        # After traversal, swap arr[left] and arr[ls] 
        tmp = self.list[left]
        self.list[left] = self.list[ls]
        self.list[ls] = tmp
        return ls

""" 
<<Mergesort>>
[                ] n    -> T(n)
[       ][       ] ~n/2 -> T(n/2)
[  ] [  ][  ] [  ] ~n/4
        ...
[][][] ...  [][][] 1
[  ][  ]...[ ][  ] 2
        ...
[       ][       ] ~n/2
[                ] n  

Merge -> θ(n)
T(n) = 2T(n/2)+θ(n)
T(n) = θ(n logn)
"""

class MergeSort:
    def __init__(self,list):
        self.list = list
        self.mergeSort(0,len(list)-1)
    
    def mergeSort(self,left,right):
        middle = (int) (left + (right-left)/2)
        if(right <= left): return
        self.mergeSort(left,middle)
        self.mergeSort(middle+1,right)
        self.merge(left,middle,right)
        
    def merge(self,left,middle,right):
        lftarr = []
        rgtarr = []
        lftptr,rgtptr = 0,0
        arrptr = left

        # Left to middle - copy left array
        for i in range(0, middle-left+1):
            lftarr.append(self.list[left+i])
        
        #middle to right - copy right array
        for i in range(0, right-middle):
            rgtarr.append(self.list[middle+1+i])

        # while lftptr > middle-left+1 and rgtptr < right-middle        
        while((lftptr < (middle-left+1)) and (rgtptr < (right-middle))):
            
            # If lftarr[lftptr] <= rgtarr[rgtptr], fill arr[arrptr] from left array, and add 1 to lftptr
            if(lftarr[lftptr] <= rgtarr[rgtptr]):
                print(lftarr[lftptr])
                self.list[arrptr] = lftarr[lftptr]
                lftptr += 1
            # If lftarr[lftptr] > rgtarr[rgtptr], fill arr[arrptr] from right array, and add 1 to rgtptr
            else:
                print(rgtarr[rgtptr])
                self.list[arrptr] = rgtarr[rgtptr]
                rgtptr += 1
            # Add 1 in arrptr
            arrptr += 1
        
        # When lftarr remains, add lftarr elements to array
        while(lftptr < middle-left+1):
            print(lftarr[lftptr])
            self.list[arrptr] = lftarr[lftptr]
            lftptr += 1
            arrptr += 1

        # When rgtarr remains, add rgtarr elements to array
        while(rgtptr < right-middle):
            print(rgtarr[rgtptr])
            self.list[arrptr] = rgtarr[rgtptr]
            rgtptr += 1
            arrptr += 1
        
        #Since merge is performed from one-element arrays, array is being automatically sorted in merging process

"""
Heapsort
O(nlogn). See comments below
"""
class HeapSort:
    def __init__(self,list):
        self.list = list
        self.heapsort(len(self.list)) 
    
    def heapsort(self,size):
        #Building heap
        for i in range((int)((size/2)-1),-1,-1): #O(n)
            self.heapify(size,i) #O(logn)
        
        #'Delete' maximum element from heap - will not be moved in later part of heapsort
        for i in range(size-1,0,-1): #O(n)
            temp = self.list[i]
            self.list[i] = self.list[0]
            self.list[0] = temp
            self.heapify(i,0) #O(logn)

    def heapify(self,size,idx):
        maxi = idx
        #Figure out what is maximum
        if(idx*2+1 < size and self.list[idx*2+1] > self.list[maxi]):
            maxi = idx*2+1
        if(idx*2+2 < size and self.list[idx*2+2] > self.list[maxi]):
            maxi = idx*2+2
        if(maxi != idx):
            #Swap
            temp = self.list[idx]
            self.list[idx] = self.list[maxi]
            self.list[maxi] = temp 
            #heapify to next level (maximum) - not going through all memboers -> O(logn)
            self.heapify(size,maxi)

"""
Radix sort
"""


"""
Selection sort
"""


"""
Bubble sort
"""


"""
Insertion sort
"""


"""
Counting sort
"""

