import re

def verify_card_number(card_number):
    clean_data = re.sub(r"\D", "", card_number)
    clean_data = list(clean_data)
    clean_data.reverse()
    
    list_number = [int(x) for x in clean_data]

    total_number = 0

    for index, value in enumerate (list_number):
        if index % 2 == 0:
            print(value)
            total_number += value
        else:
            temporary_sum = value * 2
            if temporary_sum > 9:
                temporary_sum -= 9
                total_number += temporary_sum
            else: 
                total_number += temporary_sum

    if total_number % 10 == 0:
        return 'VALID!'
    return 'INVALID!'
    

verify_card_number('4111-1111-1111-1111')