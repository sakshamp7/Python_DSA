s = input("Enter a string:")
char = list(s)
left = 0
right = len(char) - 1

while left < right:
    char[left], char[right] = char[right], char[left]
    left += 1
    right -= 1

result = "".join(char)
print("Reversed String:", result)

# This is for reversing the words in a string
word = s.split()
word.reverse()
ans = " ".join(word)
print("REversed Word :", ans)
