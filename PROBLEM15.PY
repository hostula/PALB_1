#Given an array arr[] of positive integers. Return true if all the array elements are 
#palindrome otherwise, return false. 
def isPalindrome(n):
    return str(n) == str(n)[::-1]

def palindromeArray(arr):
    for num in arr:
        if not isPalindrome(num):
            return False
    return True


# Example
arr = [121, 131, 20]
print(palindromeArray(arr))