import random
import time
import pandas as pd

def bubbleSort(arr):
  now = time.time()

  for x in range(len(arr) - 1):
    for y in range(len(arr) - 1):
      if arr[y] > arr[y + 1]:
        arr[y], arr[y + 1] = arr[y + 1], arr[y]
  elapsed_time = time.time() - now
  return arr, elapsed_time, "Bubble Sort"

# MergeSortMethods
def mergeSort(arr, k):
  if k == 2:
    now = time.time()
    x = mergeSortTwo(arr)
    elapsed_time = time.time() - now
    return x, elapsed_time, "Merge 2 Way"

  elif k == 3:
    now = time.time()
    x = mergeSortThree(arr)
    elapsed_time = time.time() - now
    return x, elapsed_time, "Merge 3 Way"

def mergeSortTwo(arr):
  if len(arr) <=1:
    return arr
  mid = len(arr) // 2
  sortedLeft = mergeSortTwo(arr[:mid])
  sortedRight = mergeSortTwo(arr[mid:])
  return mergeTwo(sortedLeft, sortedRight)

def mergeTwo(left, right):
  sorted = []
  i=j=0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      sorted.append(left[i])
      i += 1
    else:
      sorted.append(right[j])
      j += 1

  sorted.extend(left[i:])
  sorted.extend(right[j:])

  return sorted

def mergeSortThree(arr):
  if len(arr) <= 1:
    return arr

  mid1 = len(arr) // 3
  mid2 = (2*len(arr)) // 3
  sortedLeft = mergeSortThree(arr[:mid1])
  sortedMiddle = mergeSortThree(arr[mid1:mid2])
  sortedRight = mergeSortThree(arr[mid2:])
  return mergeThree(sortedLeft, sortedMiddle, sortedRight)

def mergeThree(left, middle, right):
  sorted = []
  i=j=k=0

  while i<len(left) and j < len(middle) and k < len(right):
    if left[i] <= middle[j] and left[i] <= right[k]:
      sorted.append(left[i])
      i += 1

    elif middle[j] <= left[i] and middle[j] <= right[k]:
      sorted.append(middle[j])
      j += 1

    elif right[k] <= left[i] and right[k] <= middle[j]:
      sorted.append(right[k])
      k += 1

  while i < len(left) and j< len(middle):
    if left[i] <= middle[j]:
      sorted.append(left[i])
      i += 1
    else:
      sorted.append(middle[j])
      j +=1
  while i < len(left) and k < len(right):
    if left[i] <= right[k]:
      sorted.append(left[i])
      i +=1
    else:
      sorted.append(right[k])
      k += 1
  while j < len(middle) and k < len(right):
    if middle[j] <= right[k]:
      sorted.append(middle[j])
      j +=1
    else:
      sorted.append(right[k])
      k +=1
  sorted.extend(left[i:])
  sorted.extend(middle[j:])
  sorted.extend(right[k:])
  return sorted

# QuickSortMethods
def quickSort(arr, k):
  if k == 0:
    now = time.time()
    x = quickSortFirst(arr)
    elapsed_time = time.time() - now
    return x, elapsed_time, "Quick Sort F"
  if k == 1:
    now = time.time()
    x = quickSortMiddle(arr)
    elapsed_time = time.time() - now
    return x, elapsed_time, "Quick Sort M"

def quickSortFirst(arr, pivot=0):
  if len(arr) <= 1:
    return arr

  left = []
  middle = []
  right = []
  pivotVal = arr[pivot]

  for _ in arr:
    if _ < pivotVal:
      left.append(_)
    elif _ == pivotVal:
      middle.append(_)
    else:
      right.append(_)

  return quickSortFirst(left) + middle + quickSortFirst(right)

def quickSortMiddle(arr, pivot=0):
  if len(arr) <= 1:
    return arr
  pivot = len(arr) // 2

  left = []
  middle = []
  right = []
  pivotVal = arr[pivot]

  for _ in arr:
    if _ < pivotVal:
      left.append(_)
    elif _ == pivotVal:
      middle.append(_)
    else:
      right.append(_)

  return quickSortMiddle(left) + middle + quickSortMiddle(right)

def main():
    select = 0

    while select == 0:

        nums = [random.randint(0, 100) for _ in range(0, 50)]

        nums1 = nums.copy()
        nums2 = nums.copy()
        nums3 = nums.copy()
        nums4 = nums.copy()

        print("Select which sorting algorithm to run:")
        print("1: Bubble Sort")
        print("2: Merge Sort by 2")
        print("3: Merge Sort by 3")
        print("4: Quick Sort 1st pivot")
        print("5: Quick Sort middle pivot")
        print("6: Compare sorting times for All")

        run_Algorithm = int(input())

        if run_Algorithm == 1:
            print("Bubble Sort")
            print(nums)
            x = bubbleSort(nums)
            print(f'{x[0]}, \n elapsed time: {x[1]} seconds')

        elif run_Algorithm == 2:
            print("Merge Sort 2 way")
            print(nums)
            x = mergeSort(nums, 2)
            print(f'{x[0]}, \n elapsed time: {x[1]} seconds')

        elif run_Algorithm == 3:
            print("Merge Sort 3 way")
            print(nums)
            x = mergeSort(nums, 3)
            print(f'{x[0]}, \n elapsed time: {x[1]} seconds')

        elif run_Algorithm == 4:
            print("Quick Sort first pivot")
            print(nums)
            x = quickSort(nums, 0)
            print(f'{x[0]}, \n elapsed time: {x[1]} seconds')

        elif run_Algorithm == 5:
            print("Quick Sort middle pivot")
            print(nums)
            x = quickSort(nums, 1)
            print(f'{x[0]}, \n elapsed time: {x[1]} seconds')

        elif run_Algorithm == 6:

            print(nums)

            x = bubbleSort(nums)
            x1 = mergeSort(nums1, 2)
            x2 = mergeSort(nums2, 3)
            y1 = quickSort(nums3, 0)
            y2 = quickSort(nums4, 1)

            assert x[0] == x1[0], "Lists are not Equal"
            assert x[0] == x2[0], "Lists are not Equal"
            assert x[0] == y1[0], "Lists are not Equal"
            assert x[0] == y2[0], "Lists are not Equal"

            results = [
                (x[2], x[1], x[0]),
                (x1[2], x1[1], x1[0]),
                (x2[2], x2[1], x2[0]),
                (y1[2], y1[1], y1[0]),
                (y2[2], y2[1], y2[0]),
            ]

            results_sorted = sorted(results, key=lambda r: r[1])

            fast_label, fast_time, _ = results_sorted[0]

            print("\nSorting Algorithm Comparison")
            print(f"Fastest: {fast_label} — {fast_time:.6f}s\n")

            print("Algorithm       | Time (s)   | Δ from fastest (s)")
            print("---------------------------------------------------")

            for label, t, _ in results_sorted:
                delta = t - fast_time
                print(f"{label:14} | {t:9.6f} | {delta:16.6f}")

        else:
            print("Goodbye!")
            exit()

        print("Do you want to go again?")
        replay = input()

        if replay == 'y':
            select = 0
        else:
            select = 1
            print("Goodbye!")


if __name__ == "__main__":
    main()