"""
['Julian | Pythonista', 'Bob | Nerd', 'PyBites | Coder', 
 'Dante | Pythonista', 'Martin | Nerd', 'Rodolfo | Coder']

names=['Julian','Bob','PyBites','Dante','Martin','Rodolfo']
aliases=['Pythonista','Nerd','Coder','Pythonista','Nerd','Coder']
"""

import itertools

names=['Julian','Bob','PyBites','Dante','Martin','Rodolfo']

def generate_table(name,aliases):
    output=[]
    names_iter=iter(names)
    aliases_iter=iter(aliases)
    for i in range(len(names)):
        output.append(next(names_iter) + ' | ' + next(aliases_iter))
    return output


names=['Julian','Bob','PyBites','Dante','Martin','Rodolfo']
aliases=['Pythonista','Nerd','Coder','Pythonista','Nerd','Coder']
    
print(generate_table(names,aliases))