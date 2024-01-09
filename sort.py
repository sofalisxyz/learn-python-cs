def bubble_sort(a_list):
    list_length = len(a_list) - 1
    
    for i in range(list_length):
        no_swaps = True

        for j in range(list_length - i):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]
                no_swaps = False

        if no_swaps:
            return a_list
        
    return a_list

def insertion_sort(a_list):
    for i in range(1, len(a_list)):
        value = a_list[i]

        while i > 0 and a_list[i - 1] > value:
            a_list[i] = a_list[i - 1]
            i = i - 1

        a_list[i] = value

    return a_list

def merge_sort(a_list):
    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_half = a_list[:mid]
        right_half = a_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        left_index = 0
        right_index = 0
        alist_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                a_list[alist_index] = left_half[left_index]
                left_index += 1
            else:
                a_list[alist_index] = right_half[right_index]
                right_index += 1

            alist_index += 1

        while left_index < len(left_half):
            a_list[alist_index] = left_half[left_index]
            left_index += 1
            alist_index += 1

        while right_index < len(right_half):
            a_list[alist_index] = right_half[right_index]
            right_index += 1
            alist_index += 1

    return a_list