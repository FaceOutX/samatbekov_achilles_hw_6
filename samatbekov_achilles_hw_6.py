def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

unsorted_list = [23,45,78,98,65,45,67,43,4,5,89,0,1]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)


def binary_search(item,array):
    array.sort()
    low = 0
    high = len(array)-1
    found = False

    while low <= high and not found:
        mid = (low + high)//2

        if array[mid] == item:
            print(f'Элемент {item} найден на позиции {mid}')
            found = True
        elif array[mid] < item:
            low = mid + 1
        else:
            high = mid - 1

    if not found:
        print(f'Элемент {item} не найден в списке')

element_to_find = 5
list = [5,23,45,67,89,77,544,3,687,97,51]
binary_search(element_to_find,list)