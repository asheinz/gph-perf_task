import pytest
import powerball as Powerball

# it should capture employee name
 
# it should accept 5 unique numbers in the range of 1 to 69
# it should accept a 6th number in the range of 1 to 26

# it should count duplicates
def test_get_num_totals():
    null_set = []
    numbers_set = [
        ['1', '2', '3', '4', '5'],
        ['1', '2', '3', '4', '5'],
        ['6', '7', '8', '9', '10']
    ]

    null_totals = Powerball.get_num_totals(null_set)
    assert len(null_totals) == 5
    assert len(null_totals[0]) == 0

    num_totals = Powerball.get_num_totals(numbers_set)
    assert len(num_totals) == 5
    assert len(num_totals[0]) == 2
    assert '1' in num_totals[0]
    assert '6' in num_totals[0]
    assert num_totals[0]['1'] == 2
    assert num_totals[0]['6'] == 1

def test_get_pow_totals():
    null_set = []
    pows_set = [
        '1','2','1'
    ]

    null_totals = Powerball.get_pow_totals(null_set)
    assert len(null_totals) == 0

    pow_totals = Powerball.get_pow_totals(pows_set)
    assert len(pow_totals) == 2

# it should retrieve max count per unique duplicate number
def test_get_winning_numbers():
    null_totals = []
    num_totals = [
        {'1': 2, '7': 1},
        {'2': 1, '3': 2},
        {'4': 2, '5': 1},
        {'5': 3},
        {'6': 1, '7': 2}
    ]
    null_win = Powerball.get_winning_numbers(null_totals)
    assert len(null_win) == 0

    winning_numbers = Powerball.get_winning_numbers(num_totals)
    assert len(winning_numbers) == 5
    assert winning_numbers == ['1', '3', '4', '5', '7']

# it should resolve ties between max counts randomly
def test_get_winning_number():
    null_totals = {}
    totals = {'1': 2, '3': 1, '2': 1}

    null_win = Powerball.get_winning_number(null_totals)
    assert null_win == None
    
    winning_number = Powerball.get_winning_number(totals)
    assert winning_number == '1'

# it should display all employees and favorite numbers


# it should display final Powerball number
  
