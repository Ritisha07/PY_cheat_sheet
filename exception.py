try:
    lst = ['Alice', 'Bob', 'Carl']
    print(lst[3])
except Exception as e:
    print(e)
finally:
    print('inside finally')

print('Am I executed?')
