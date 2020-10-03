thisdict = {
    1: 'Orange',
    'Two': 'Cherry'
}
for name in thisdict.values():
    print(f'values:{name}')

# key,value :
for key, val in thisdict.items():
    print(f'Key:{key}, Values:{val}')

print(thisdict.get(3, 'Invalid Option'))
