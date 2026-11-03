def is_armstrong_number(number):
    length_number = len(str(number)) ## This tells us how many digits and this is the number we raise to

    n = 0 
    sum = 0
    while (n < length_number): 
        digit_n = ((int(str(number)[n]))**length_number)
        n = n + 1
        sum = sum + digit_n


    return number==sum