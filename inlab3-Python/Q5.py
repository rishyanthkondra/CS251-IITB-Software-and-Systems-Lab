Str = input()

dictionary = {key: 0 for key in Str}
i = 0
while i < len(Str) :
    dictionary[Str[i]] = dictionary[Str[i]] + 1
    i=i+1

for j,p in sorted(dictionary.items(), key=lambda x: (x[1],x[0]), reverse=True):
    print("%s: %s" %(j,p))

#reference
#https://stackoverflow.com/questions/7742752/sorting-a-dictionary-by-value-then-by-key
