#!/usr/bin/python3

friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}

print(friends)

print(friends.popitem())

print(friends)

print(friends.clear())

print(friends)

friends = {'tom': '111-222-333', 'bob': '888-999-666', 'jerry': '666-33-111'}

print(friends.keys())

print(friends.values())

print(friends.get('tom'))

print(friends['tom'])

print(friends.get('lukas', 'podolski'))

print(friends)

print(friends.pop('bob'))

print(friends)
