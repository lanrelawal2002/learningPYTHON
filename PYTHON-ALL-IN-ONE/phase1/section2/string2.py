#!/usr/bin/python3

line1 = "welcome"
line2 = "welcome"

print(id(line1), id(line2))

line1 += " Kane"

print(line1)

print(id(line1))
print(id(line1), id(line2), id(line2), id(line1))
