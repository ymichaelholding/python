"""

𝐈𝐧𝐩𝐮𝐭 -
i = [2,3,[50,80,[100,200],90],34]
𝐎𝐮𝐭𝐩𝐮𝐭 -
o = [2, 3, 50, 80, 100, 200, 90, 34]
"""

i = [2,3,[50,80,[100,200],90],34]

print(type(i))

strr=type(i)

print(strr)

output=[]
def flattern_list(input_list):
    for i in input_list:
        if type(i) is list:
            flattern_list(i)
        else:
            output.append(i)

    return output


print(flattern_list(i))