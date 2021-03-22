#This program calculates Body Mass Index (BMI)
#author: Angelina Belotserkovskaya


try:
    # Ask to input height in cm and save it into variable 
    # which is converted into int
    height = int(input('Please enter your height in centimetres: '))
    # Convert cm to m2
    heightInM2 = (height**2) / 10000

    # Ask to input weight in kg and save it into variable 
    # which is converted into int

    weight = int(input('Please enter your weight in kg: '))

    # Calculating bmi
    bmi = weight/heightInM2
    print ('Your BMI is {:.2f}'.format(bmi))
except:
    print('Please make sure to enter an integer number')






