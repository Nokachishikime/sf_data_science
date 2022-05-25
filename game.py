"""Guess number game"""

import numpy as np

number = np.random.randint(1,101) #randomly select given number
count = 0

while True:
    count += 1
    predict_number = int(input("Guees number from 1 to 100: "))
    
    if predict_number > number:
        print("Number should be less!")
        
    elif predict_number < number:
        print("Number should be more!")
        
    else:
        print(f"You are right! The number = {number}, with {count} tryes")
        break
    
