import random
import timeit

from sorting_techniques import pysort


def main():
    arr = range(1, 1_000_000)
    arr1 = random.sample(arr, 1_000)
    arr2 = random.sample(arr, 10_000)
    arr3 = random.sample(arr, 100_000)

    sortObj = pysort.Sorting()

    print(timeit.timeit(lambda: sortObj.mergeSort(arr1), number=10))
    print(timeit.timeit(lambda: sortObj.mergeSort(arr2), number=10))
    print(timeit.timeit(lambda: sortObj.mergeSort(arr3), number=10))

    print("\n")

    print(timeit.timeit(lambda: sortObj.insertionSort(arr1), number=10))
    print(timeit.timeit(lambda: sortObj.insertionSort(arr2), number=10))
    print(timeit.timeit(lambda: sortObj.insertionSort(arr3), number=10))

    print("\n")

    print(timeit.timeit(lambda: arr1.sort(), number=10))
    print(timeit.timeit(lambda: arr2.sort(), number=10))
    print(timeit.timeit(lambda: arr3.sort(), number=10))



if __name__ == '__main__':
    main()