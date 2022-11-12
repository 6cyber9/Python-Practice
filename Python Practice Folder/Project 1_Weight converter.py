weight = input("Input weight:  ")
unit = input ("Choose unit ()lbs or (K)Kg: ")
K = round(int(weight)/2.205)
P = round(int(weight)*2.205)
if unit == 'K':
    print (f' {int(weight)} Kg = {P} lbs')
elif unit == 'P':
    print (f'{int(weight)} lbs = {K} Kg')
else:
    print("select (K) or (P)")

