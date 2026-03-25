num1 =float(input('enter the first number: '))
operators = input('enter the operators (+ , - , * , /): ')
num2 =float(input('enter the second number: '))

if operators == '+':
    print ('result:' , num1 + num2)

elif operators == '-':
    print( 'result:' , num1 - num2)

elif operators == '*':
    print ('result:' , num1 * num2)

elif operators == '/':
    if num2 != '0':
        print ('result:' , num1 / num2)
    else:
        print ('error: cannot divide by zero')

else:
    print('error')
