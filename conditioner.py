house_price = 1
g_credit = 1

buyer = g_credit
if buyer == g_credit:
  print("put down 10%")
else:
  print("put fown 20%")
  
price = 1000000
is_good_credit = True
if is_good_credit:
  down = 0.1 * price
else:
  down = 0.2 * price
print(f"your down payment is ${down}")

characters = 2
if characters < 3:
  msg = "valid name must ne at least three characters long"
elif characters > 49:
  msg = "characters is more than 50"
else:
  msg = "thats a good name"
print(msg)

#assesment
mes = '''
what's is your weight?
(L)lbs   (K)kbs
'''
input1 = int(input(mes))
input2 = input("(L) lbs   (K) kbs? ")
main = input1 * 0.45
sub = input1 / 45
input2.lower()
if input2 == "l":
  print(f"your weight is {main}")
else:
  print(f"your weight is {sub}")



