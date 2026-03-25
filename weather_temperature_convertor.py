def celcius_to_fahrenheit(c):
    return (9/5 * c + 32)


def fahrenheit_to_celcius(f):
    return (5/9 * f + 32)



print("---Temperature Convertor---")
print('1. is celcius to fahrenheit')
print('2. is fahrenheit to celcius')


choice = input('Enter your choice (1 or 2): ')


if choice == '1':
    c = float(input('Enter temperature in Celcius: '))
    f = celcius_to_fahrenheit(c)
    print(f'{c} C = {f:.2f} F')


elif choice == '2':
    f = float(input('Enter temperature in Fahrenheit: '))
    c = fahrenheit_to_celcius(f)
    print(f'{f} F = {c:.2f} c' )


else:
    print('Invalid choice')