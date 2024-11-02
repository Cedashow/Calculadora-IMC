# Código para gerar IMC
nome = input("Olá, qual seu nome? ")
while True:
# Boas vindas
    print(f'Seja bem-vindo, {nome}, vamos iniciar o cálculo do seu IMC!')

    print()
    
# Realizando a coleta dos dados, Peso e altura, e a opção de sair caso necessario
    peso = float(input("Digite o seu peso em KG (Ou digite 0 para sair): "))
    if peso == 0:
        print("Você escolheu sair.")
        break  # Sai do loop
    print()
    altura = float(input("Digite a sua altura em Metros (Ou digite 0 para sair): "))
    if altura == 0:
        print("Você escolheu sair.")
        break  # Sai do loop
    print()
    print(f'Obrigado {nome}, irei realizar o cálculo para você!')
    
    print()
    print()
    
# Realizando o cálculo IMC, utilizando a formula
    imc = peso / altura**2

# Com o resultado em mãos iremos classificar a saude de acordo com os valores.
    if imc < 18.5:
        saude = "abaixo do peso"
    elif 18.5 <= imc < 24.9:
        saude = "com peso normal"
    elif 25 <= imc < 29.9:
        saude = "com sobrepeso"
    else:
        saude = "com obesidade"

#Exibindo as informações, nome, imc e o estado classificado.
    print(f'{nome} seu IMC é {imc:.2f}, Seu estado é: {saude}')
    
    print()
#Agradecimentos finais, como está dentro do while, gera o loop para o inicio
    print("Obrigado por usar o programa!") 
    print()# Para espaçar a saída