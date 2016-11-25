units = input("Do you wish to enter metric units or imperial units? Please enter 'metric' or 'imperial': ")

if units == 'metric':
     height = float(input('Please enter your height input meters(decimals): '))
     weight = int(input('Please enter your weight input kg: '))
     bmi = weight/(height*height)

     if bmi <= 18.5:
        print('Your BMI is', bmi,', you are technically underweight.')

     elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,' , a normal BMI.')

     elif bmi > 25 and bmi < 30:
        print('your BMI is', bmi," , so you're technically overweight.")

     elif bmi > 30:
        print('Your BMI is', bmi,' , you are technically obese.')
              
elif units == 'imperial':
    
     height = int(input('Please enter your height input inches(whole number): '))
     weight = int(input('Please enter your weight input pounds(whole number): '))
     bmi = (weight*703)/(height*height)

     if bmi <= 18.5:
        print('Your BMI is', bmi,"you're underweight.")

     elif bmi > 18.5 and bmi < 25:
        print('Your BMI is', bmi,'you have a normal BMI.')

     elif bmi > 25 and bmi < 30:
        print('Your BMI is', bmi,'you are overweight')

     elif bmi > 30:
        print('Your BMI is', bmi,'which means you are obese.')
	
else:
        print('There is an error with your input')
        print('Please check you have entered whole numbers\n'
              'and decimals were asked.')
              
