
listarrays =[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
value = {'1000': 'M', '900': 'CM', '500': 'D', '400': 'CD', '100': 'C', '90': 'XC', '50': 'L', '40': 'XL', '10': 'X',
         '9': 'IX', '5': 'V', '4': 'IV', '1': 'I'}


def convertInttoRoman(input_number):
    roman_number=0
    remainder = 0
    print(input_number)
    for num in listarrays:
        if input_number >=num :
            if input_number % num == 0:
                round_number = round(input_number / num)
                print(round_number)
                for keys, values in value.items():
                    if keys == str(num):
                        print(values)
                        roman_number = round_number *(values)
                        remainder = 0
            else:
                print(num)
                round_number = int(input_number / num)
                print(round_number)
                remainder = input_number % num
                for keys, values in value.items():
                    if keys == str(num):
                        print(values)
                        roman_number = round_number * (values)
                        print(roman_number)
            break

    return roman_number, remainder

def main(input_number):
    final_output=''
    output, remainder = convertInttoRoman(input_number)
    final_output= final_output + output
    print(final_output,remainder)
    while remainder>0:
        output, remainder = convertInttoRoman(remainder)
        print('****',output,'****',remainder)
        final_output= final_output + output

    return final_output

if __name__ == "__main__":
     print(main(3468))



#MMMCDLXVIII
#MMMCDLXVIII
#MMMCDLXXVVIII
