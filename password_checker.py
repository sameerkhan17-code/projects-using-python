password = input('Enter your password: ')

#these are the conditions set for the password to check its strength
length_ok = len(password) >= 8
has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)
has_lower = any(ch.islower() for ch in password)
has_special = any(ch in '`¬@.,;:"£&^$=+-_)/[]{}#~£*!%('  for ch in password)

#this score variable will count its strength
score = 0


if length_ok:
    score += 1

if has_digit:
    score += 1

if has_upper:
    score += 1

if has_lower:
    score += 1

if has_special:
    score += 1

if score == 5:
    print('your password strength: Very strong')

elif score == 4:
    print('your password strength: Strong')

elif score == 3:
    print('your password strength: Medium')

elif score == 2:
    print('your password strength: Weak')

else:
    print('your password strength: Very Weak')






