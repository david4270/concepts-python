# Sorting algorithms
# Overlaps with C++ basic-6

import func

def main():
    givenList = [23,45,12,53,125,62]
    func.QuickSort(givenList)
    print("Result of quicksort is",givenList)

    givenList = [23,45,12,53,125,62]
    func.MergeSort(givenList)
    print("Result of mergesort is",givenList)

    givenList = [23,45,12,53,125,62]
    func.HeapSort(givenList)
    print("Result of heapsort is", givenList)

    givenList = [23,45,12,53,125,62]
    func.RadixSort(givenList)
    print("Result of radixsort is", givenList)

    givenList = [23,45,12,53,125,62]
    func.SelectionSort(givenList,len(givenList))
    print("Result of selction srot is",givenList)

    givenList = [23,45,12,53,125,62]
    func.BubbleSort(givenList,len(givenList))
    print("Result of bubblesort is",givenList)

    givenList = [23,45,12,53,125,62]
    func.InsertionSort(givenList,len(givenList))
    print("Result of insertion sort is",givenList)

    givenList = [23,45,12,53,125,62]
    func.CountingSort(givenList,len(givenList))
    print("Result of counting sort is",givenList)

if __name__ == "__main__":
    main()