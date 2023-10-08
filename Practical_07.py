'''WAP to accept a number, find and display whether
it's a Armstrong number or not. (Practical_07)'''
while True:
   num = int(input("Enter a number=====>  "))
   
   sum = 0
   
   number = num
   while number > 0:
      digit = number % 10
      sum += digit ** 3
      number //= 10
   
   if num == sum:
      print(num,"is an Armstrong number")
   else:
      print(num,"is not an Armstrong number")
