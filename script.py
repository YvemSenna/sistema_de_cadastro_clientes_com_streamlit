nome = input("Digite seu nome: ")
idade = int(input("Digite a sua idade: "))
print(nome)

if idade > 17:
    print("Você pode entrar na festa!")
else:
    print("Você não pode entrar na Festa")

with open("base_dados.csv", "a") as arquivo:
    arquivo.write(f"Seja bem vindo(a) {nome}. \n")