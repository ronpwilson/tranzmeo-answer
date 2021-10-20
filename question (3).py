# *** Question 1 ***
#
# Write a function ‘breakdown()’ that will take an amount and a dictionary as input.
# The amount is the actual money and the dictionary denotes the currency and its count in number.
#
# For example :-
#     Total money = 1256 # The amount as input
#     denominations={2000:10,  500:10,  100:20, 50:0, 20:10, 10:5,  5:10, 2:10, 1:10},
# you have 10 numbers of 2000 rupees and 10 numbers    of 500 rupees and so on.
#
# a. The function should return a dictionary that contains how it will break down the given amount using the currencies available
#    with minimal number of usage.
#        For example, in the above case, it would return {500:2,100:2,20:2,10:1,5:1,1:1}.
#
# b. If the amount cannot be returned from the available currencies, you should raise the exception without modifying the given
# 'denominations'.

def breakdown(amount, denominations):
    newDict = {}

    for k,v in denominations.items():
        counter = 0
        while k <= amount and v > 0:
            amount = amount - k
            counter += 1
            newDict[k] = counter
            v -= 1
        else:
            continue
    return newDict


d = {2000:10,  500:10,  100:20, 50:0, 20:10, 10:5,  5:10, 2:10, 1:10}
print(breakdown(1256, d))
























