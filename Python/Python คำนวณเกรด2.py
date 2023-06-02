try:
    score=int(input('Input: '))
    if 80 <= score <= 100:
        print ('Grad A')
    elif 70 <= score <=79:
        print ('Grad B')
    elif 60 <= score <= 69:
        print ('Grad C')
    elif 50 <= score <= 59:
        print ('Grad D')
    elif 0 <= score <= 49:
        print ('Grad F')
    else:
        print ('number between 0 - 100')
except ValueError:
    print ("Not a number")