"""Guess number game - optimal version
The goal is to minimize amount of tryes
"""

import numpy as np

def random_predict(number:int=1) -> int:
    """Randomly guessing the number

    Args:
        number (int, optional): Given number. Defaults to 1.

    Returns:
        int: Amount of tryes
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count

def wise_predict(number:int=1) -> int:
    """Wisely guessing the number: number seed is stil random, but borders of seed are shrinking

    Args:
        number (int, optional): Given number. Defaults to 1.

    Returns:
        int: Amount of tryes
    """
    
    count = 0
    min_number = 1 #basic minimum border
    max_number = 100 #basic maximum border
    
    while True:
        count += 1
        predict_number = np.random.randint(min_number, max_number+1)
        if number > predict_number:
            min_number = predict_number
        elif number < predict_number:
            max_number = predict_number
        else:
            break
    return count

def exect_predict(number:int=1) -> int:
    """Logicaly guessing the number: shrinking borders catching the number sooner or later

    Args:
        number (int, optional): Given number. Defaults to 1.

    Returns:
        int: Amount of tryes
    """
    
    count = 0
    min_number = 1 #basic minimum border
    max_number = 101 #basic maximum border
    
    while True:
        count += 1
        predict_number = (min_number + max_number) // 2
        if number > predict_number:
            min_number = predict_number
        elif number < predict_number:
            max_number = predict_number
        else:
            break
    return count

def score_game(some_predict) -> int:
    """Mean amount of tryes to guess number within 1000 guessing cycles

    Args:
        some_predict (_type_): Some guessing function

    Returns:
        int: mean amount of tryes
    """
    count_list = [] #list to save tryes amount
    np.random.seed(1) #make the seed stable for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) #list of numbers
    
    for number in random_array:
        count_list.append(some_predict(number))

    score = int(np.mean(count_list)) #mean amount of tryes calculation
    print(f"With function {some_predict.__name__} mean amount of tryes is: {score}")
    return score

if __name__ == '__main__':
    score_game(random_predict)
    score_game(wise_predict)
    score_game(exect_predict)