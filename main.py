import powerball as Powerball

if __name__ == "__main__":
    employees = Powerball.get_employees()
    num_totals = Powerball.get_num_totals([e['numbers'] for e in employees])
    pow_totals = Powerball.get_pow_totals([e['powerball'] for e in employees])
    winning_numbers = Powerball.get_winning_numbers(num_totals)
    winning_powerball = Powerball.get_winning_number(pow_totals)
    Powerball.print_employees(employees)
    Powerball.print_winning_numbers(winning_numbers, winning_powerball)
