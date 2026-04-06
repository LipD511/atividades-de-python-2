idade = int(input("Digite a idade: "))

if idade < 18:
    print("Menor de idade")
elif idade <= 59 and idade >=18:
    print("Adulto")
else:
    print("Idoso")