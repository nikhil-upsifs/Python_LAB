def change_string(s):
    new_string = s.replace(s[0], "X")
    return new_string
s=input("Enter a string: ")
new_string = change_string(s)
print("Original string:", s)
print("Modified string:", new_string)