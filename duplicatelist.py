lists=["hello",10,20,40,20,60,40,30]

from collections import Counter

x=Counter(lists)

print(x)

output=[]
def duplicate_list(input):
    for i in input:
        if (lists.count(i)>1) & (output.count(i)!=1):
            output.append(i)
    return output

print(duplicate_list(lists))


