string = "aaaavvvhhhjjjj"
char= []
for value in string:
    if value not in char:
        char.append(value)

# for str in char:
#     temp = ''
#     temp += str
#     print(temp)

print(' '.join(char))
