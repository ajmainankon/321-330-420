# -*- coding: utf-8 -*-
"""CS50.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sFbwgR2PGyMEuB01rI3ZQ2p1xzO1lbps
"""

4a = input(" input the value " )
x = len (a)
print (x)
for count in a:
  print (count)

# b = input(" input the second value ")
# d = int(a)
# e = int (b)
# c = d+e

#for ascii values


a = input(" input the value " )
x = len (a)
for count in a:
  print (" ascii value for the letter is," , count,":" , ord(count))

a = input(" input the value " )
b = a.isupper()
print (b)
c = a.islower()
print (c)
d = a.upper()
print (d)
e = a.lower()
print (e)

b = input(" input the value of the pyramid from 1 to 8 " )
a = int(b)

for j in range (a):
  for i in range (j+1):
    print ("# ",end="" )
  print(" ")

b = input(" input the value of the pyramid from 1 to 8 " )
a = int(b)

for j in range (a):
  for i in range (a- j):
    print ("# ",end="" )
  print(" ")

amount = float(input(" please enter a non negative amount " ))
while amount<0:
  amount = float(input(" please enter a non negative amount " ))

#print ("good to go")
cents = round(amount * 100)
#print (RoundedRealAmount)
coins = 0

while cents >=25:
    cents = cents - 25
    coins += 1

while cents >=10:
    cents = cents - 10
    coins += 1

while cents >=5:
    cents = cents - 5
    coins += 1

while cents >=1:
    cents = cents - 1
    coins += 1

print(coins)

amount = float(input(" please enter a non negative amount " ))
while amount<0:
  amount = float(input(" please enter a non negative amount " ))

#print ("good to go")
cents = round(amount * 100)
#print (RoundedRealAmount)
coins = 0
pennys = [25,10,5,1]

for count in pennys:
    while cents >= count:
        cents = cents - count
        coins = coins + 1
print (coins)

x = float(input(" x: "))

y = float(input(" y: "))

z = x / y
print(f"x / y = {z:.50f}")

def main():
  for x in range(4):
    cough()
def cough():
  print("cough")

main()

def main():
    cough(3)

def cough(n):
  for x in range(n):
    print("cough")  

main()

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max = 0
    secondMax = 0
for count in arr:
    x = arr[count]
    if x>max:
        max = arr[count]
    print (max)



