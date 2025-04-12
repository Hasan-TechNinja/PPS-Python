first_name = input()
fixed_salary = float(input())
bonus = (float(input())*15)/100

fixed = fixed_salary + bonus
print(f"TOTAL = R$ {fixed:.2f}")