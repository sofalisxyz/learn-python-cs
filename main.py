from recursion import print_nums

print_nums(10)


from binary_search import search_number, search_word

my_list_nums = [3,14,22,24,41,65,78,99]
my_list_words = ['apple', 'blueberry', 'chicken', 'egg', 'meat', 'pasta', 'pork', 'watermelon']

print(search_number(my_list_nums, 65))
print(search_number([3,14,22,24,41,65,78,99], 45))

print(search_word(my_list_words, 'blueberry'))
print(search_word(my_list_words, 'fish'))