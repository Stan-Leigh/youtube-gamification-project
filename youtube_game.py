import random

def choose_winning_numbers(choices, winners):
    """
    Input parameters:
        choices, type=list: number of boxes users have chosen
        winners, type=int: number of winning numbers we want  

    Output, type=list:
        winning numbers that determines which user won
    """

    return random.sample(choices, winners) 

def choose_winners(winners, user_dict):
    """
    Input parameters:
        winners, type=int: number of winning numbers we want  

    Output, type=string:
        string containing winning numbers and winners
    """

    # get numbers that have been chosen by a user.
    options_list = []
    for key, value in user_dict.items():
        if value is None:
            continue
        options_list.append(key)

    # Get winning numbers
    winners_list = choose_winning_numbers(options_list, winners)

    # Print winners and winning numbers
    for index, winner in enumerate(winners_list):
        print(f'Winner {index+1} is number {winner}, {user_dict[winner]}')


# dictionary stores the id of each user [I used names as the placeholder]. The keys are the available options the user can choose from.
user_dict = {1: 'Anita', 2: None, 3: 'Cindy', 4: 'David', 5: 'Esther',
             6: 'Francis', 7: 'Gideon', 8: None, 9: 'Isabel', 10: 'Jim',
             11: None, 12: 'Lolade', 13: 'Michael', 14: 'Nancy', 15: None,
             16: 'Paul', 17: 'Queen', 18: None, 19: 'Shola', 20: 'Tope',
             21: 'Ugonna', 22: 'Veronica', 23: 'Wasiu', 24: None, 25: None}

choose_winners(7, user_dict)
