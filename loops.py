i = 0
while i < 5:
  print(i)
  i +=1
print("done")

#guessing game
guess_range = 0
guess_time = 3
secret_digit = 99
while guess_range < guess_time:
  guess= int(input("Guess? "))
  guess_range += 1
  if guess == secret_digit:
    print("you won")
    break
else:
  print("you lost")