weight = input("weight?  ")
unit = input ("unit P(lbs) or K(g)? ")
K = round(int(weight)*0.45)
P = round(int(weight)/0.45)
if unit == 'K':
    print (f'weight is {P}lbs')
elif unit == 'P':
    print (f'weight is {K}Kg')
else:
    print("select conversion (K)g or (P)lbs")
