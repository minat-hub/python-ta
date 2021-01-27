import sys
import os


def palindrome(s):
    # your code goes here
    first_letter = 0
    last_letter = len(s) - 1

    while last_letter >= first_letter:
        if s[first_letter] == s[last_letter]:
            return True
        first_letter += 1
        last_letter -= 1
    return False


def solution(s):
    return palindrome(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))

