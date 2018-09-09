# define a betting function

def betting():
    import random

    originfalFund = 500
    bettingSize = 10

    total = originfalFund

    count = 0
    while total < 2 * originfalFund and total > 0:
        throw = random.randint(1,6)

        if throw > 3:
            total += bettingSize
        else:
            total -= bettingSize

        count += 1

#        print('throw: ' + str(throw))
#        print(" You have $ " + str(total) + " remaining")

    print('After %s throw, you have $%s remaining' % (str(count), str(total)) )

    return(total)
