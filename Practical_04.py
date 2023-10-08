'''WAP to accept percentage of a student 
and display its grade accordingly (Practice_04)'''
from emoji import emojize
while True:
   user_input = int(input("Enter your marks===> "))
   if 91 <= user_input <= 100:
       {
           print("A1")
       }
   elif 81 <= user_input <= 90:
       {
           print("A2")
       }
   elif 71 <= user_input <= 80:
       {
           print("B1")
       }
   elif 61 <= user_input <= 70:
       {
           print("B2")
       }
   elif 51 <= user_input <= 60:
       {
           print("C1")
       }
   elif 41 <= user_input <= 60:
       {
           print("C1")
       }
   elif 33 <= user_input <= 40:
       {
           print("D")
       }
   else:
       {
           print("Fail", emojize(":loudly_crying_face:"))
       }
   