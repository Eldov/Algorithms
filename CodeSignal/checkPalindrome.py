# Given the string, check if it is a palindrome.
def solution(inputString):
    s = inputString == inputString[::-1]
    return s
