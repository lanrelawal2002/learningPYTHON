#!/usr/bin/python3

friends = {'tom': '111-222-333', 'bob': '888-999-666'}

print(friends)

for key in friends:
    print(key, ":", friends[key])

print(len(friends))

print('tom' in friends)

print('bob' not in friends)

print(friends)

print('jerry' not in friends)

print('jerry' in friends)
