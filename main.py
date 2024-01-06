from recursion import print_nums

print_nums(10)


from binary_search import *

my_list_nums = [3,14,22,24,41,65,78,99]
my_list_words = ['apple', 'blueberry', 'chicken', 'egg', 'meat', 'pasta', 'pork', 'watermelon']

print(search_number(my_list_nums, 65))
print(search_number(my_list_nums, 45))

print(search_word(my_list_words, 'blueberry'))
print(search_word(my_list_words, 'fish'))


from sort import *

my_list_unsorted_nums = [1,5,3,24,21,54,32,11,12]

print(bubble_sort(my_list_unsorted_nums))
print(insertion_sort(my_list_unsorted_nums))