def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if sorted(s1) == sorted(s2):
        return True
    else:
        return False
    

def is_palindrome(s1):
    if s1.lower() == s1[::-1].lower():
        return True
    return False
