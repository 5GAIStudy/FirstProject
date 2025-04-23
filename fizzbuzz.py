for i in range(1, 15 +1) :
    if i % 15 == 0 or i % 3 == 0 or i % 5 == 0 :
        print('fizzbuzz' * (i % 15 == 0) + 'Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0))
    else :
        print(f'{i}') 
