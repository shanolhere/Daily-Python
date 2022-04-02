#BMI Calculator using python
height= int(input("Enter your height(in cms) :"))
weight = int(input("Enter your weight (in kgs) :"))

height = height/100
BMI = weight/(height * height)
print("Your Body Mass Index (BMI) is: ")

if(BMI >0):
    if BMI<=16:
        print("You are severely underweight o_o")
    elif BMI<=18.5:
        print("You are underweight o_o")
    elif BMI<=25:
        print("You are healthy ^-^")
    elif BMI<=30:
        print("You are overweight ;-;")
    else:
        print("You are severely overweight ;-;")
        
else: print("Enter valid details ;-;")