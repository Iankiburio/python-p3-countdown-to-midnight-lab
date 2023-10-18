import time

def countdown(n):
    number = n
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
    print('HAPPY NEW YEAR!')

def countdown_with_sleep(n):
    number = n
    while number > 0:
        print(f'{number} SECOND(S)!')
        number -= 1
        time.sleep(1)
    print('HAPPY NEW YEAR!')
