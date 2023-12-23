#!/usr/bin/python

amount=input("what is your amount?")
amount=float(amount)
print(amount)

interest=input("what's the interest?")
interest=float(interest)

years=input("Years?")
years=int(years)

i = 0
while i <= years:
    amount=amount+amount/100*interest
    i = i + 1
    print("The total principle and interest is {} year\t{}".format(i,amount))
