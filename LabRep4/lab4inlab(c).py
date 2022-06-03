def reverse(str):
    s = ""
    for ch in str:
        s = ch + s
    return s

#Given String
mystr = "BeginnerBook"
print("Given String: ", mystr)

#Reverse String
print("Reversed String:", reverse (mystr))
