import os

"""
  hehe haha
  door floor
  haha hehe
  6;8 3-4
  true blue
  hehe bebe
  floor door
  3-4 6;8
  Michael Holding
  haha hehe
"""

#declare the file name
file_name=r'Python\Adventofcode\two.txt'


#read the file contents 
def read_file(file_name):
    with open(file_name, 'r') as file:          # open file for reading
        elements = [line.strip() for line in file]
    return elements

#implement the main logic
def main(file_name):
    element_list=read_file(file_name)
    print('original list' + ' ' + str(element_list))
    for parent_element in element_list:
        for items in element_list:
            if parent_element == items.split(' ')[1] + ' ' + items.split(' ')[0]:
                element_list.remove(items)
    return element_list

if __name__ == "__main__":
    print('output ' + ' ' + str(main(file_name)))
