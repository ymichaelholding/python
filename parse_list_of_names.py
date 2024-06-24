"""
1. Write a function that accepts a list of names and title cases them and removes duplicates.

2. Next, sort the list in alphabetical descending order by surname.

3. Finally, find the shortest first name.

"""


NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    output=[]
    for i in names:
        if (output.count(i)!=1):
            output.append(i.title())
    return output
    
unique_name=dedup_and_title_case_names(NAMES)

print(unique_name)

def sort_surname(names):
    return sorted(names, key=lambda name: name.split(" ")[-1].lower())

print(sort_surname(unique_name))

def shortest_name(names):
    first_name={}
    for row,name in enumerate(names):
        first_name[name.split(" ")[0]]=len(name.split(" ")[0])
    return min(first_name, key=first_name.get)
        

print(shortest_name(unique_name))


            
        



