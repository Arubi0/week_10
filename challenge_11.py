gpa = int(input("What is your GPA? "))
serviceHours = int(input("How many service hours do you have? "))


if (gpa >= 3.5): 
       if (serviceHours > 50):
            print ("Eligible for full scholarship. ")
else: print ("Eligiblie for partial scholarship. ")


if (3.0 <= gpa <= 3.5) :
      if (serviceHours > 50):
           print("Eligible for partial scholarship. ")
else: print ("Requires more community service hours for scholarship consideration. ")

if (gpa < 3.0):
      print ("Not eligible for scholarship")