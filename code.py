def ispalindrome(s):
    cleaned = ""

    for ch in s:
        if ch.isalnum():
            cleaned += ch.lower()
    return cleaned == cleaned[::-1]


a = input("Enter the string:")

if ispalindrome(a):
    print("The string is palindrome")
else:
    print("The string is not a palindrome")
