weather = input("How is the weather like? ")
if weather == "rain" or weather == "snow":
    print("Bring your umbrella")
elif weather == "fine dust":
    print("Bring your mask")
else:
    print("Don't need to bring anything")



tem = int(input("How is the temperature? "))
if tem >= 30:
    print("It's too hot!!!")
elif tem >= 10 and tem < 30:
    print("What a nice weather!")
elif 0 <= tem < 10:
    print("Bring your jacket")
else:
    print("It's too cold!!!")