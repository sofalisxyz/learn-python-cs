# given a list of sorted numbers, write a function that does binary search of target number and returns if it's in the list
def search_number(nums_list, n):
    first = 0
    last = len(nums_list) - 1

    while last >= first:
        mid = (first + last) // 2

        if nums_list[mid] == n:
            return True
        else:
            if n < nums_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

# given a list of sorted words, write a function that does binary search of target word and returns if it's in the list
def search_word(words_list, word):
    first = 0
    last = len(words_list) - 1

    while last >= first:
        mid = (first + last) // 2

        if words_list[mid] == word:
            return True
        else:
            if ord(word[0]) < ord(words_list[mid][0]):
                last = mid - 1
            else:
                first = mid + 1
    return False
