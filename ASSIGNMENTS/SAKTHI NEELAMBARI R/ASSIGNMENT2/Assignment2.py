import random
a=1
while (a!=0):
    temp=random.randint(18,50)
    humid=random.randint(60,100)
    print("Temperature is :",temp)
    print("Humidity is:",humid)
    if((temp>=30) or(humid>=80)):
         if(temp>=30):
             print("Temperature is greater")
         if(humid>=80):
             print("Humidity is greater")
         if ((temp>=30) and (humid>=80)):
             print("Temperatue and Humidity Values are Greater")
         print("Alarm Rings")
    else:
         print("Alarm off")
