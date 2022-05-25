"""Guess number game
But PC do it itself
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
    return(count)

def score_game(random_predict) -> int:
    """Mean amount of tryes to guess number within 1000 guessing cycles

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: mean amount of tryes
    """
    count_list = [] #list to save tryes amount
    np.random.seed(1) #make the seed stable for reproducibility
    random_array = np.random.randint(1, 101, size=(1000)) #list of numbers
    
    for number in random_array:
        count_list.append(random_predict(number))

    score = int(np.mean(count_list)) #mean amount of tryes calculation
    print(f"Your algorithms mean amount of tryes is: {score}")
    return(score)

#print(f"Number of tryes: {random_predict()}")

if __name__ == '__main__':
    score_game(random_predict)