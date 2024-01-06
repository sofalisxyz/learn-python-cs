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
