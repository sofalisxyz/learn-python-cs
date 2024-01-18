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
my_list_unsorted_words = ['blueberry', 'egg', 'pork', 'chicken', 'apple', 'watermelon', 'pasta', 'meat']

print(bubble_sort(my_list_unsorted_nums.copy()))
print(insertion_sort(my_list_unsorted_nums.copy()))
print(merge_sort(my_list_unsorted_nums.copy()))

print(sorted(my_list_unsorted_nums.copy()))
print(sorted(my_list_unsorted_nums.copy(), reverse=True))
print(sorted(my_list_unsorted_words.copy()))
print(sorted(my_list_unsorted_words.copy(), reverse=True))
print(sorted(my_list_unsorted_words.copy(), key=len))

from string_algs import *

print(is_anagram('Cats', 'acst'))
print(is_palindrome('eveveveve'))
print(is_palindrome('something'))

