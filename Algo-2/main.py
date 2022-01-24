# Sorting algorithms
# Overlaps with C++ basic-6

import func

def main():
    givenList = [5,6,2,4,1,3]
    func.QuickSort(givenList)
    print(givenList)

    givenList = [5,6,2,4,1,3]
    func.MergeSort(givenList)
    print(givenList)

    givenList = [5,6,2,4,1,3]
    func.HeapSort(givenList)
    print(givenList)

if __name__ == "__main__":
    main()