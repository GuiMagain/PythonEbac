# Retorne a media de todos os salarios, com exceção do menor e maior

salary = [4000, 3000, 1000, 2000]

novo_array = sorted(salary)

novo_array.remove(novo_array[0])
novo_array.remove(novo_array[-1])

med_salary = 0

for salary in novo_array:
    med_salary += salary

print(med_salary // len(novo_array))

print(med_salary)
print(len(novo_array))