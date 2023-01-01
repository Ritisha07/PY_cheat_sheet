str = 'Practice Comprehension'

my_dict = {}
for char in str:
    my_dict[char.upper()] = (ord(char), ord(char.swapcase()))

print(my_dict)


print('using comprehension:', {char.upper(): (ord(char), ord(char.swapcase()))  for char in str})