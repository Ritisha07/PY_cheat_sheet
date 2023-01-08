str = "Practice Comprehension"

my_dict = {}
for char in str:
    my_dict[char.upper()] = (ord(char), ord(char.swapcase()))

print(my_dict)


print(
    "using comprehension:",
    {char.upper(): (ord(char), ord(char.swapcase())) for char in str},
)


SUITE = "H D S C".split()
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

print(SUITE)

li = []
for r in RANKS:
    for s in SUITE:
        li.append((r, s))

print(len(li))
print((r, s) for r in RANKS for s in SUITE)
