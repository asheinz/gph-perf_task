import random

# print('collect employee names and numbers')
def get_employees():
    employees = []
    while True:
        employees.append(add_employee())

        proceed = input("Another employee? yes/no > ")
        while proceed.lower() not in ("yes", "no"):
            proceed = input("Invalid input. Another employee? 'yes' or 'no' > ")
        if proceed.lower() == "no":
            break
    return employees

def add_employee():
    min_num, max_num, max_pow = 1, 69, 26
    num_range = " thru ".join([str(min_num), str(max_num)])
    pow_range = " thru ".join([str(min_num), str(max_pow)])
    cap = ") > "
    prompts = [
        "Enter your first name > ", 
        "Enter your second name > ",
        "Select 1st # (" + num_range,
        "Select 2nd # (" + num_range,
        "Select 3rd # (" + num_range,
        "Select 4th # (" + num_range,
        "Select 5th # (" + num_range,
        "Select Power Ball # (" + pow_range + cap
    ]
    employee = {
        'name': [],
        'numbers': [],
        'powerball': 0
    }

    for i, text in enumerate(prompts):
        text = prompts[i]
        # print('capture employee name')
        if i < 2:
            employee['name'].append(input(text))
        # print('accept 5 unique numbers in the range of 1 to 69')
        elif i < 7:
            if len(employee['numbers']) == 0:
                excluding = ""
            elif len(employee['numbers']) == 1:
                excluding = " excluding " + str(employee['numbers'][0])
            elif len(employee['numbers']) == 2:
                excluding = " excluding " + " and ".join([
                    str(i) for i in employee['numbers']])
            else:
                excluding = " excluding " + "and ".join([
                    ", ".join([
                        str(i) for i in employee['numbers']])[:-1], 
                        str(employee['numbers'][-1])])
            num = prompt_user_for_number(text + excluding + cap, 
                                         min_num, 
                                         max_num, 
                                         set(employee['numbers']))
            employee['numbers'].append(num)
            # while True:
            #     try:
            #         a_number = int(input(text + excluding + cap))
            #         if a_number in set(range(1, 70)) - set(employee['numbers']):
            #             employee['numbers'].append(a_number)
            #             break
            #         print("Invalid number, try again.")
            #     except ValueError:
            #         print("Integers only, please. Try again.")
        # print('accept a 6th number in the range of 1 to 26')
        else:
            powball = prompt_user_for_number(text, min_num, max_pow)
            employee['powerball'] = powball
            # while True:
            #     try:
            #         pow_num = int(input(text + cap))
            #         if pow_num in range(1,26):
            #             employee['powerball'] = pow_num
            #             break
            #         print("Invalid number, try again.")
            #     except ValueError:
            #         print("Integers only, please. Try again.")
    
    return employee

def prompt_user_for_number(text, n, x, other_set=()):
    while True:
        try:
            a_number = int(input(text))
            if a_number in set(range(n, x)) - set(other_set):
                break
            print("Invalid number, try again.")
        except ValueError:
            print("Integers only, please. Try again.")
    return a_number

def get_num_totals(employees):
    # print('count duplicates')
    num_totals = [{},{},{},{},{}]
    print('employees: {}'.format(employees))
    for employee in employees:
        for i, v in enumerate(employee['numbers']):
            if v in num_totals[i].keys():
                num_totals[i][v] += 1
            else:
                num_totals[i][v] = 1
        
    return num_totals

def get_pow_totals(employees):
    pow_totals = {}
    for employee in employees:
        powball = employee['powerball']
            
        if employee['powerball'] in pow_totals:
            pow_totals[powball] += 1
        else:
            pow_totals[powball] = 1

    return pow_totals

def get_winning_numbers(num_totals):
    # print('retrieve max count per unique duplicate number')
    # print('resolve ties between max counts randomly')
    winning_numbers = []
    for i, s in enumerate(num_totals):
        # 0, {...}
        winning_numbers.append(get_winning_number(s))
        # if len(s.keys()) == 1:
        #     dups = [list(s.keys())[0]]
        # else:
        #     h_t_l = sorted(s, key=s.get, reverse=True)
        #     dups = [h_t_l[0]]
        #     # [ keys in order of highest to lowest value ]
        #     for j, k in zip(h_t_l, h_t_l[1:]):
        #         if s[k] == s[j]:
        #             dups.append(k)

        # winning_numbers.append(random.choice(dups))
    return winning_numbers

def get_winning_number(totals):
    winning_number = None
    if len(totals) == 1:
        winning_powerball = list(totals.keys())[0]
    else:
        h_t_l = sorted(totals, key=totals.get, reverse=True)
        dups = [h_t_l[0]]
        for j, k in zip(h_t_l, h_t_l[1:]):
            if totals[k] == totals[j]:
                dups.append(k)
        winning_powerball = random.choice(dups)
    return(winning_powerball)

def print_employees(employees):
    # print('display all employees and favorite numbers')
    print('')
    for employee in employees:
        print(' '.join([
            ', '.join(employee['name'][::-1]), 
            ' '.join(str(i) for i in employee['numbers']),
            "Powerball: " + str(employee['powerball'])
        ]))

def print_winning_numbers(winning_numbers, winning_powerball):
    # print('display final powerball number')
    print('')
    print('Powerball winning number:')
    print('')
    print(' '.join(str(i) for i in winning_numbers) + " Powerball: " + str(winning_powerball))


if __name__ == "__main__":
    employees = get_employees()
    num_totals = get_num_totals(employees)
    pow_totals = get_pow_totals(employees)
    winning_numbers = get_winning_numbers(num_totals)
    winning_powerball = get_winning_number(pow_totals)
    print_employees(employees)
    print_winning_numbers(winning_numbers, winning_powerball)
