from curses.ascii import isalpha


def isUnique(s):
    sorted_s = sorted(s)
    str_len = len(s)

    for index, char in enumerate(sorted_s):
        if (str_len == index + 1):
            break
        if (sorted_s[index] == sorted_s[index+1]):
            return False

    return True

def checkPermutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    str1_sorted = sorted(str1)
    str2_sorted = sorted(str2)

    for i in range(len(str1)):
        if str1_sorted[i] != str2_sorted[i]:
            return False

    return True

def URLify(str, str_len):
    def helper(str, index, len_str):
        for ind in range(len_str, index-1, -1):
            if (ind + 2 <= len_str):
                str[ind+2] = str[ind]
                str[ind] = " "

    str_array = [i for i in str]
    for ind, char in enumerate(str_array):
        if char == " ":
            helper(str_array, ind+1, str_len-1)
            str_array[ind] = "%"
            str_array[ind+1] = "2"
            str_array[ind+2] = "0"
    
    return "".join(str_array)

def isPalindromePerm(str):
    a_set = set(str)
    odd = 0
    for c in a_set:
        if isalpha(c) and str.count(c) % 2 != 0:
            odd += 1
    
    return True if odd <= 1 else False

def oneAway(string1, string2):
    
    len1 = len(string1)
    len2 = len(string2)

    if len2 > len1:
        string1, string2 = string2, string1
    if abs(len1-len2) >= 2:
        return False

    ptr1, ptr2 = 0, 0
    counter = 0
    while ptr1 < len1 and ptr2 < len2:
        if counter > 1:
            return False
        if string1[ptr1] != string2[ptr2] and string1[ptr1+1] == string2[ptr2]:
            ptr1 += 1
            counter += 1
        elif string1[ptr1] != string2[ptr2] and string1[ptr1+1] == string2[ptr2+1]:
            ptr1 += 1
            ptr2 += 1
            counter += 1
        else:
            ptr1 += 1
            ptr2 += 1
    
    
    return True


