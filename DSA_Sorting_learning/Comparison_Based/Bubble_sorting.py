# def bubble_sort(arr):

#     n = len(arr)

#     for i in range(n - 1):

#         for j in range(n - i - 1):

#             if arr[j] > arr[j + 1]:

#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]

#     return arr


# num=int(input("Enterr the Size of the list: "))

# numbers = []

# for _ in range(num):
#     element = int(input("Enter an element: "))
#     numbers.append(element)

# bubble_sort(numbers)

# print(numbers)

def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

num = int(input("Enter the size of the list: "))
numbers = []
for _ in range(num):
    element = int(input("Enter an element: "))
    numbers.append(element)

bubble_sort(numbers)
print("Sorted list:", numbers)