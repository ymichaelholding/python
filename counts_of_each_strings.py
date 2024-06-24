#""""
#Many people eat cereal for breakfast.	subject = people, verb = eat
#Ted goes to the gym and exercises three times a week.
#""""

from collections import Counter

input_string="Ted goes to the gym and exercises three times a week"
print(Counter(input_string))



output={}
def counts_of_each_string(input):
    for i in input_string:
        if output.get(i) is not None:
            values=output.get(i)+1
            output[i]=values
        else:
            output[i]=1
    return output

print(counts_of_each_string(input_string))

